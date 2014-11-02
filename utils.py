# -*- coding: utf-8 -*-
"""
Python cheat sheet
http://www.astro.up.pt/~sousasag/Python_For_Astronomers/Python_qr.pdf?utm_content=buffer88e26&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer
"""
from __future__ import division, print_function
import re


complements = {
    'G': 'C', 'C': 'G',
    'T': 'A', 'A': 'T',
}

RE_CHAR = re.compile('.')


def complement(text):
    return RE_CHAR.sub(lambda m: complements[m.group(0)], text)


def reverse_complement(text):
    return complement(text)[::-1]


def all_offsets(text, pattern):
    offsets = []
    start = 0
    while True:
        ofs = text.find(pattern, start)
        if ofs < 0:
            break
        offsets.append(ofs)
        start = ofs + 1
    return offsets


def write_offsets(path, offsets):
    open(path, 'wt').write(' '.join(str(x) for x in offsets))
