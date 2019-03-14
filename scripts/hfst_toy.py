import csv
from pathlib import Path
import sys

import hfst


def read_from_csv():
    datafile = open('test.csv', 'r')
    datareader = csv.reader(datafile, delimiter=',')
    data = []
    for row in datareader:
        data.append((row[0], row[1]))
    return data


def test_RPT(words):
    src = Path('g2p.twolc')
    raw = Path('rawg2p_from_py.hfst')
    final = Path('g2p_from_py.hfst')
    if not raw.exists() or (src.stat().st_mtime > raw.stat().st_mtime):
        hfst.compile_twolc_file(src.name, raw.name)
    test = hfst.HfstInputStream(raw.name)
    fsts = []
    fst = None
    if not test.is_eof():
        fst = test.read()
    while not test.is_eof():
        fsts.append(test.read())
    for fstrans in fsts:
        fst.intersect(fstrans)
    # fst.invert()  # This gives `Segmentation fault: 11`
    out = hfst.HfstOutputStream(filename=final.name)
    out.write(fst)
    out.flush()
    out.close()
    output = []
    print('Processing test words...', file=sys.stderr)
    for inword in words:  # for inword, outword in words:
        outwords = fst.lookup(inword)
        output.append(f'{inword}\n{", ".join([w for w, wt in outwords])}\n\n')
        # fst_word = fst.lookup(inword)
        # good_fst = (outword == fst_word)
        # if not good_fst:
        #     print(f'Failed: {word[0]} :==> {word[1]} != {fst_word}')
    return output


if __name__ == '__main__':
    # text = read_from_csv()
    in_file = Path('/tmp/g2p_lex-test.txt')
    with in_file.open() as f:
        test_words = [line.strip() for line in f]
    text = ['ся́ду', 'твёрдый', 'ю́бка', 'ба́юшки', 'опя́ть', 'съе́сть', 'жи́ть']  # noqa
    out_file = Path('/tmp/output_g2p_hfst_from_py.txt')
    with out_file.open('w') as f:
        print(''.join(test_RPT(test_words)), file=f)
    print(f'Output can be viewed using `less {out_file}`')
