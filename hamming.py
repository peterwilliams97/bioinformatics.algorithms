# -*- coding: utf-8 -*-
from __future__ import division, print_function
import sys
from utils import read_file_lines
from algos import hamming


a = 'TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC'
b = 'GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA'

a = 'CAGAAAGGAAGGTCCCCATACACCGACGCACCAGTTTA'
b = 'CACGCCGTATGCATAAACGAGCCGCACGAACCAGAGAG'

h = hamming(a, b)
print(len(a), a)
print(len(b), b)
print(h)
print(float(h) / float(len(b)))

from collections import defaultdict
from itertools import product
A = 'atcg'

a = 'atcg'
a = 'cccc'


all_4mers = product(A, repeat=4)
distances = {x: hamming(x, a) for x in all_4mers}
distance_counts = defaultdict(int)
for x, d in distances.items():
    distance_counts[d] += 1

for d, n in sorted(distance_counts.items()):
    print('%2d: %4d' % (d, n))

path = sys.argv[1]
print(path)
lines = read_file_lines(path)
print(len(lines))
a, b = lines
print(a[:10])
print(b[:10])
print(hamming(a, b))
