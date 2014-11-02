# -*- coding: utf-8 -*-
"""
Python cheat sheet
http://www.astro.up.pt/~sousasag/Python_For_Astronomers/Python_qr.pdf?utm_content=buffer88e26&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer
"""
from __future__ import division, print_function
import os


OUTPUT_DIR = 'output'

try:
    os.mkdir(OUTPUT_DIR)
except:
    pass


def make_outpath(filename):
    return os.path.join(OUTPUT_DIR, filename)


def read_file_lines(path):
    with open(path, 'rt') as f:
        lines = [ln.rstrip('\n').strip() for ln in f]
    return [ln for ln in lines if ln]
