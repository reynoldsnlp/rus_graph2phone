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
    tmp = Path('g2p_from_py.tmp.hfst')
    final = Path('g2p_from_py.hfst')
    if not tmp.exists() or (src.stat().st_mtime > tmp.stat().st_mtime):
        print('Compiling twolc rules...', file=sys.stderr)
        hfst.compile_twolc_file(src.name, tmp.name, resolve_left_conflicts=True)

    print('Preparing rule transducers for composition...', file=sys.stderr)
    rule_fsts_stream = hfst.HfstInputStream(tmp.name)
    rule_fsts = []
    while not rule_fsts_stream.is_eof():
        next_fst = rule_fsts_stream.read()
        next_fst.determinize()
        next_fst.remove_epsilons()
        print(type(next_fst), next_fst.get_name())
        rule_fsts.append(next_fst)
    rule_fsts = tuple(rule_fsts)

    print('Creating universal language FST...', file=sys.stderr)
    universal = hfst.regex('?* ;')
    print('Compose-intersecting rules with universal FST...', file=sys.stderr)
    universal.compose_intersect(rule_fsts)

    print('Writing out final FST...', file=sys.stderr)
    out = hfst.HfstOutputStream(filename=final.name)
    out.write(universal)
    out.flush()
    out.close()

    output = []
    print('Processing test words...', file=sys.stderr)
    for inword in words:  # for inword, outword in words:
        outwords = universal.lookup(inword)
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
