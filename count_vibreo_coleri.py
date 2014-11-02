# -*- coding: utf-8 -*-
"""
Python cheat sheet
http://www.astro.up.pt/~sousasag/Python_For_Astronomers/Python_qr.pdf?utm_content=buffer88e26&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer
"""
from __future__ import division, print_function
from utils import all_offsets, write_offsets


path = 'Vibrio_cholerae.txt'
text = open(path, 'rt').read()


def find_in_vibreo_coleri(pattern):
    print('-' * 80)
    print('path=%s,size=%d,pattern="%s"' % (path, len(text), pattern))
    offsets = all_offsets(text, pattern)
    out_path = '%s.%s.offsets' % (path, pattern)
    print('out_path="%s",%d offsets' % (out_path, len(offsets)))
    write_offsets(out_path, offsets)


find_in_vibreo_coleri('CTTGATCAT')
find_in_vibreo_coleri('ATGATCAAG')

