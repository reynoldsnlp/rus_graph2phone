import hfst
import csv
import sys

def read_from_csv():
    datafile = open('test.csv', 'r')
    datareader = csv.reader(datafile, delimiter=',')
    data = []
    for row in datareader:
        data.append([row[0],row[1]])
    return data

def test_RPT(words, rule1, rule2):
    hfst.compile_twolc_file('g2p.twolc', 'g2p.hfst')
    test = hfst.HfstInputStream('g2p.hfst')
    fsts = []
    fst = None
    while not test.is_eof():
        fsts.append(test.read())
    fst = fsts[rule1]
    for rule_num in range(rule1+1,rule2+1):
        fst.intersect(fsts[rule_num])
    for inword in words:  # for inword, outword in words:
        outwords = fst.lookup(inword)
        print(inword, ', '.join([w.replace('@_EPSILON_SYMBOL_@', '') for w, wt
                               in outwords]), sep='\t')
        # fst_word = fst.lookup(inword)
        # good_fst = (outword == fst_word)
        # if not good_fst:
        #     print('Failed: {} :==> {} != {}'.format(word[0],word[1],fst_word))


if __name__ == '__main__':
    text = read_from_csv()
    test_RPT(text, int(sys.argv[1]), int(sys.argv[2]))
