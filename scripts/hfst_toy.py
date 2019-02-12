import hfst
import csv

def read_from_csv():
    datafile = open('../scripts/words.csv', 'r')
    datareader = csv.reader(datafile, delimiter=',')
    data = []
    for row in datareader:
        data.append((row[0],row[1]))
    return data

def test_RPT(words):
    hfst.compile_twolc_file('g2p.twolc','g2p.hfst')
    test = hfst.HfstInputStream('g2p.hfst')
    fsts = []
    fst = None
    if not (test.eof()):
        fst = test.read()
    while not (test.is_eof()):
        fsts.append(test.read())
    for fstrans in fsts:
        fst.intersect(fstrans)
    for word in word:
        fst_word = fst.lookup(word[0])
        good_fst = (word[1] == fst_word)
        if not good_fst:
            print('Failed: {} :==> {} != {}'.format(word[0],word[1],fst_word))

text = read_from_csv()
test_RPT(text)
