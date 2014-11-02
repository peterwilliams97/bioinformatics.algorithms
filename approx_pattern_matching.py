# -*- coding: utf-8 -*-
from __future__ import division, print_function
import sys
from utils import read_file_lines
from algos import all_offsets_approximate, write_offsets


path = sys.argv[1]
print(path)
lines = read_file_lines(path)
print(len(lines))
pattern, text, k = lines
k = int(k)
print('text = %d "%s...%s"' % (len(text), text[:10], text[-10:]))
print('pattern = %d "%s"' % (len(pattern), pattern[:10]))
print('k=%d' % k)
offsets = all_offsets_approximate(text, pattern, k)
out_path = path + '.offsets'
print(out_path)
write_offsets(out_path, offsets)

