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

    # kmer_offsets is a fat (python integer per text character) inverted index
    kmer_offsets = defaultdict(list)
    for i in range(len(text) - k):
        kmer_offsets[text[i:i + k]].append(i)

    print('@@2 %s' % len(kmer_offsets))

    clumps = []
    for kmer, offsets in kmer_offsets.items():
        for i in range(len(offsets) - t + 1):
            if offsets[i + t - 1] < offsets[i] + L:
                clumps.append(kmer)
                break

    return clumps


def skew(text, k):
    """#G - #C for first `k` neucleotides of Genome `text`"""
    return text[:k].count('G') - text[:k].count('C')


def skew_values(text):
    """Return list of len(text) + 1 skew values in `text`"""
    skew = 0
    skew_list = [0]
    for c in text:
        skew += (c == 'G') - (c == 'C')
        skew_list.append(skew)
    return skew_list


def skew_min_max(skew_list):
    min_value = min(skew_list)
    max_value = max(skew_list)
    min_indexes = [i for i, x in enumerate(skew_list) if x == min_value]
    max_indexes = [i for i, x in enumerate(skew_list) if x == max_value]
    return (min_value, max_value), min_indexes, max_indexes


from itertools import izip


def hamming(a, b):
    return sum(x != y for x, y in izip(a, b))
