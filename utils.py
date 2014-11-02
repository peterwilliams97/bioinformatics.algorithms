# -*- coding: utf-8 -*-
"""
Python cheat sheet
http://www.astro.up.pt/~sousasag/Python_For_Astronomers/Python_qr.pdf?utm_content=buffer88e26&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer
"""
from __future__ import division, print_function
import re
import os
from collections import defaultdict


OUTPUT_DIR = 'output'

try:
    os.mkdir(OUTPUT_DIR)
except:
    pass


def make_outpath(filename):
    return os.path.join(OUTPUT_DIR, filename)


complements = {
    'G': 'C', 'C': 'G',
    'T': 'A', 'A': 'T',

    'g': 'c', 'c': 'g',
    't': 'a', 'a': 't',
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


def word_count(text, pattern):
    cnt = 0
    for i in range(len(text) - len(pattern)):
        if text[i:i + len(pattern)] == pattern:
            cnt += 1
    return cnt


def all_kmers(text, k):
    return {text[i:i + k] for i in range(len(text) - k)}


def frequent_kmers(text, k, min_cnt=None, include_rc=False):
    kmer_cnt_dict = defaultdict(int)
    for i in range(len(text) - k):
        kmer_cnt_dict[text[i:i + k]] += 1
    if include_rc:
        text_rc = reverse_complement(text)
        for i in range(len(text_rc) - k):
            kmer_cnt_dict[text_rc[i:i + k]] += 1

    if min_cnt is not None:
        freq_kmers = [(kmer, cnt) for kmer, cnt in kmer_cnt_dict.items()
                      if cnt >= min_cnt]
    else:
        max_cnt = max(kmer_cnt_dict.values())
        freq_kmers = [(kmer, cnt) for kmer, cnt in kmer_cnt_dict.items()
                      if cnt == max_cnt]

    freq_kmers.sort()
    return freq_kmers


def find_clumps(text, k, L, t):
    """Clump Finding Problem: Find patterns forming clumps in a string.
     Find all `k`-mers that occur `t` or more times in substrings of length `L` in `text`

     Input: A string `text', and integers k, L, and t.
     Output: All distinct k-mers forming (L, t)-clumps in Genome.

    """
    freq_kmers = [kmer for kmer, _ in frequent_kmers(text, k, t)]
    #print('@@1 %s' % freq_kmers)
    clumps = []
    for kmer in freq_kmers:
        offsets = all_offsets(text, kmer)
        print('%s %s' % (kmer, offsets))
        for i in range(len(offsets) - t + 1):
            if offsets[i + t - 1] <= offsets[i] + L:
                clumps.append(kmer)
                break
    return clumps
