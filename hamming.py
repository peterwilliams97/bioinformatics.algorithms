def hamming(a, b):
    return sum(x != y for x, y in zip(a, b))


a = 'TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC'
b = 'GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA'

h = hamming(a, b)
print len(a)
print len(b)
print h
print float(h) / float(len(b))

from collections import defaultdict
from itertools import product
A = 'atcg'
a = 'atcg'

all_4mers = product(A, repeat=4)
distances = {x: hamming(x, a) for x in all_4mers}
distance_counts = defaultdict(int)
for x, d in distances.items():
    distance_counts[d] +=1

for d, n in sorted(distance_counts.items()):
    print '%2d: %4d' % (d, n)
