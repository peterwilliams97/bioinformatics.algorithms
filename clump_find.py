# -*- coding: utf-8 -*-
"""
Python cheat sheet
http://www.astro.up.pt/~sousasag/Python_For_Astronomers/Python_qr.pdf?utm_content=buffer88e26&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer
"""
from __future__ import division, print_function
from utils import find_clumps


if __name__ == '__main__':
    if True:
        text = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
        k, L, t = 5, 50, 4
    if True:
        text = open('E-coli.txt', 'rt').read()
        k, L, t = 9, 500, 3

    clumps = find_clumps(text, k, L, t)
    clumps_set = sorted(set(clumps))
    print('-' * 80)
    print('text=%d,k=%d,L=%d,t=%d' % (len(text), k, L, t))
    print('%d %d %s' % (len(clumps), len(clumps_set), ' '.join(clumps_set[:20])))
