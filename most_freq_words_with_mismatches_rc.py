# -*- coding: utf-8 -*-
"""
https://stepic.org/lesson/Some-Hidden-Messages-are-More-Elusive-than-Others-9/step/8?course=Bioinformatics-Algorithms&unit=407
"""
from __future__ import division, print_function
import sys
import time
from utils import read_file_lines
from algos import most_frequent_approximate_kmers


path = sys.argv[1]
print(path)
lines = read_file_lines(path)
print(len(lines))
text, kd = lines
k, d = kd.split()
k, d = int(k), int(d)
print('text = %d "%s...%s"' % (len(text), text[:10], text[-10:]))
print('k=%d' % k)
print('d=%d' % d)
t0 = time.clock()
frequent_kmers = most_frequent_approximate_kmers(text, k, d, add_rc=True)
t1 = time.clock()
print(' '.join(frequent_kmers))
print('time=%.1f sec' % (t1 - t0))
