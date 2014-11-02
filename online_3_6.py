# -*- coding: utf-8 -*-
"""
Python cheat sheet
http://www.astro.up.pt/~sousasag/Python_For_Astronomers/Python_qr.pdf?utm_content=buffer88e26&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer
"""
from __future__ import division, print_function
from utils import all_offsets


if __name__ == '__main__':
    text = 'GATATATGCATATACTT'
    pattern = 'ATAT'
    offsets = all_offsets(text, pattern)
    print('-' * 80)
    print('text="%s",pattern="%s",offsets=%s' % (text, pattern, offsets))

