# -*- coding: utf-8 -*-
from __future__ import division, print_function
from utils import skew_values, skew_min_max


text = 'CATTCCAGTACTTCATGATGGCGTGAAGA'
text = 'GATACACTTCCCAGTAGGTACTG'
text = 'GAGCCACCGCGATA'
text = 'CATGGGCATCGGCCATACGCC'

skew_list = skew_values(text)
(min_value, max_value), min_indexes, max_indexes = skew_min_max(skew_list)

for i, x in enumerate(skew_list[:20]):
    c = text[i - 1] if i > 0 else ' '
    is_min = '---' if x == min_value else ''
    is_max = '+++' if x == max_value else ''
    print('%3d: %s %3d %s%s' % (i, c, x, is_min, is_max))

print(' '.join(str(x) for x in skew_list[:20]))
print('min=%d %s,max=%d %s' % (min_value, min_indexes, max_value, max_indexes))
