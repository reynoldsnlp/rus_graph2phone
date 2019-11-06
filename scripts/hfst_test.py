from pathlib import Path
import sys
import hfst
import csv
import re

def get_fst(start_rule, end_rule, *args):
    src = Path('g2p.twolc')
    tmp = Path('g2p_test_from_py.tmp.hfst')
    hfst.compile_twolc_file(src.name, tmp.name,
                                resolve_left_conflicts=True)
    print('Preparing rule transducers for composition...', file=sys.stderr)
    rule_fsts_stream = hfst.HfstInputStream(tmp.name)

    rule_numbers = set()
    rule_numbers.add(0)
    for i in range(start_rule, end_rule + 1):
        rule_numbers.add(i)
    if (len(args) > 0):
        for i in range(args[0], args[1]+1):
            rule_numbers.add(i)

    rule_fsts = []
    for index, rule in enumerate(rule_fsts_stream):
        if index in rule_numbers:
            rule_fsts.append(rule)

    print('Creating universal language FST...', file=sys.stderr)
    output = hfst.regex('?* ;')
    print('Compose-intersecting rules with universal FST...',
          file=sys.stderr)
    output.compose_intersect(rule_fsts)
    print('Optimizing for fast lookup...', file=sys.stderr)
    output.lookup_optimize()
    return output


def test(text, truth, start_rule, end_rule, *args):
    fst = get_fst(start_rule, end_rule, *args)
    print('Processing test words...', file=sys.stderr)
    for index, inword in enumerate(text):  # for inword, output in words:
        outputs = fst.lookup(inword)
        output = [w for w, wt in outputs][0]
        if (output != truth[index]):
            print("\n" + inword + " => " + output + " != " + truth[index])
        else:
            print('.', end='', flush=True, file=sys.stderr)


def test_words():
    datafile = open('test.csv', 'r')
    datareader = csv.reader(datafile, delimiter=',')
    text = []
    truth = []
    for row in datareader:
        text.append(row[0])
        truth.append(row[1])
    start_rule = 0
    end_rule = 24
    test(text, truth, start_rule, end_rule)

if __name__ == '__main__':
    test_words()
