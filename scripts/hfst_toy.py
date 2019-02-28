import csv
from pathlib import Path

import hfst


def read_from_csv():
    datafile = open('test.csv', 'r')
    datareader = csv.reader(datafile, delimiter=',')
    data = []
    for row in datareader:
        data.append((row[0], row[1]))
    return data


def test_RPT(words):
    if Path('g2p.twolc').stat().st_mtime > Path('g2p.hfst').stat().st_mtime:
        hfst.compile_twolc_file('g2p.twolc', 'g2p.hfst')
    test = hfst.HfstInputStream('g2p.hfst')
    fsts = []
    fst = None
    if not test.is_eof():
        fst = test.read()
    while not test.is_eof():
        fsts.append(test.read())
    for fstrans in fsts:
        fst.intersect(fstrans)
    for inword in words:  # for inword, outword in words:
        outwords = fst.lookup(inword)
        print(inword, ', '.join([w for w, wt in outwords]), sep='\t')
        # fst_word = fst.lookup(inword)
        # good_fst = (outword == fst_word)
        # if not good_fst:
        #     print(f'Failed: {word[0]} :==> {word[1]} != {fst_word}')


if __name__ == '__main__':
    # text = read_from_csv()
    text = ['ся́ду', 'твёрдый', 'ю́бка', 'ба́юшки', 'опя́ть', 'съе́сть', 'жи́ть']
    test_RPT(text)
