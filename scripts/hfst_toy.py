import hfst

input = 'сло́во'

test = hfst.HfstInputStream('g2p.hfst')
fsts = []
while not (test.is_eof()):
    fsts.append(test.read())
fsts[0].intersect(fsts[1])
print(fsts[0].lookup(input))
