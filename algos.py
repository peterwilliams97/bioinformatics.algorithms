# -*- coding: utf-8 -*-
"""
Python cheat sheet
http://www.astro.up.pt/~sousasag/Python_For_Astronomers/Python_qr.pdf?utm_content=buffer88e26&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer
"""
from __future__ import division, print_function
import re
from collections import defaultdict
from itertools import izip


DNA_COMPLEMENTS = {
    'G': 'C', 'C': 'G',
    'T': 'A', 'A': 'T',

    'g': 'c', 'c': 'g',
    't': 'a', 'a': 't',
}

T_U = {'t': 'u', 'T': 'U'}

RNA_COMPLEMENTS = {T_U.get(k, k): T_U.get(v, v) for k, v in DNA_COMPLEMENTS.items()}

RE_CHAR = re.compile('.')


def complement(text, is_rna=False):
    complement_dict = RNA_COMPLEMENTS if is_rna else DNA_COMPLEMENTS
    return RE_CHAR.sub(lambda m: complement_dict[m.group(0)], text)


def reverse_complement(text, is_rna=False):
    return complement(text, is_rna)[::-1]


def all_offsets(text, pattern):
    """Return list of all offsets of `pattern` in `text`"""
    offsets = []
    start = 0
    while True:
        ofs = text.find(pattern, start)
        if ofs < 0:
            break
        offsets.append(ofs)
        start = ofs + 1
    return offsets


def all_offsets_approximate(text, pattern, d):
    """Return list of all offsets of patterns with hamming distance `d` of `pattern` in `text`"""
    offsets = []
    for i in xrange(len(text) - len(pattern) + 1):
        if sum(text[i + j] != c for j, c in enumerate(pattern)) <= d:
            offsets.append(i)
    return offsets


def write_offsets(path, offsets):
    open(path, 'wt').write(' '.join(str(x) for x in offsets))


def word_count(text, pattern):
    cnt = 0
    for i in xrange(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            cnt += 1
    return cnt


def all_kmers(text, k):
    return {text[i:i + k] for i in xrange(len(text) - k + 1)}


def frequent_kmers(text, k, min_cnt=None, include_rc=False):
    kmer_cnt_dict = defaultdict(int)
    for i in xrange(len(text) - k + 1):
        kmer_cnt_dict[text[i:i + k]] += 1
    if include_rc:
        text_rc = reverse_complement(text)
        for i in xrange(len(text_rc) - k + 1):
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


def most_frequent_approximate_kmers(text, k, d, add_rc=False):
    """Frequent Words with Mismatches Problem: Find the most frequent k-mers with mismatches in a string.
     Input: A string Text as well as integers k and d. (You may assume k ≤ 12 and d ≤ 3.)
     Output: All most frequent `k`-mers with up to `d` mismatches in `text`.
    """

    kmer_set = all_kmers(text, k)
    # if add_rc:
    #     kmer_set = kmer_set | {reverse_complement(kmer) for kmer in kmer_set}

    approx_kmer_set = kmer_set.copy()

    for _ in xrange(d):
        print('@@1', len(approx_kmer_set))
        approx_kmer_set0 = approx_kmer_set.copy()
        for kmer in approx_kmer_set0:
            for j in xrange(k):
                for c in 'ATCG':
                    approx_kmer_set.add(''.join(kmer[:j] + c + kmer[j + 1:]))

    kmer_cnts = defaultdict(int)
    #kmer_cnts_rc = defaultdict(int)
    for i in xrange(len(text) - k + 1):
        kmer = text[i:i + k]
        kmer_cnts[kmer] += 1
        if add_rc:
            kmer_rc = reverse_complement(kmer)
            kmer_cnts[kmer_rc] += 1 # WE double count self-complements

    print('@@2', len(kmer_cnts))
    max_cnt = 0

    if False:
        #approx_kmer_dict = {}
        approx_kmer_cnts = {}

        for kmer in approx_kmer_set:
            neighbors = {kmer}
            for _ in xrange(d):
                neighbors0 = neighbors.copy()
                for kmer2 in neighbors0:
                    for j in xrange(k):
                        for c in 'ATCG':
                            neighbors.add(''.join(kmer2[:j] + c + kmer2[j + 1:]))
            #approx_kmer_dict[kmer] = neighbors
            if not neighbors:
                continue
            total = sum(kmer_cnts.get(n, 0) for n in neighbors)
            if total > max_cnt:
                approx_kmer_cnts[kmer] = total
                #print((kmer, total))
                max_cnt = total

        max_cnt = max(approx_kmer_cnts.values())

    else:
        max_cnt = max(kmer_cnts.values())
        approx_kmer_cnts = {}
        for kmer in approx_kmer_set:
            cnt = 0
            for kmer2, cnt2 in kmer_cnts.items():
                # About twice as fast to short circuit as to sum()
                matched = True
                mismatches = 0
                for i in xrange(k):
                    if kmer2[i] != kmer[i]:
                        mismatches += 1
                        if mismatches > d:
                            matched = False
                            break
                if matched:
                #if sum(c2 != c for c2, c in izip(kmer2, kmer)) <= d:
                    cnt += cnt2
            # for kmer2, cnt2 in kmer_cnts_rc.items():
            #     if sum(c2 != c for c2, c in izip(kmer2, kmer)) <= d:
            #         cnt += cnt2
            if cnt >= max_cnt:
                approx_kmer_cnts[kmer] = cnt
            if cnt > max_cnt:
                max_cnt = cnt

    frequent_kmers = [kmer for kmer, cnt in approx_kmer_cnts.items() if cnt == max_cnt]

    # WE include complements in results
    if add_rc and False:
        frequent_kmers_uniq = set()
        for kmer in frequent_kmers:
            if kmer not in frequent_kmers_uniq and reverse_complement(kmer) not in frequent_kmers_uniq:
                frequent_kmers_uniq.add(kmer)
        frequent_kmers = list(frequent_kmers_uniq)

    frequent_kmers.sort()
    print('***', max(kmer_cnts.values()), len(text) - k + 1, len(kmer_cnts), len(approx_kmer_cnts))
    for kmer in sorted(approx_kmer_cnts.keys(), key=lambda k: -approx_kmer_cnts[k])[:5]:
        cnt = approx_kmer_cnts[kmer]
        print(kmer, cnt, kmer in kmer_set)
    return frequent_kmers


def find_clumps(text, k, L, t):
    """Clump Finding Problem: Find patterns forming clumps in a string.
        Find all `k`-mers that occur `t` or more times in substrings of length `L` in `text`

        Input: A string `text', and integers k, L, and t.
        Output: All distinct k-mers forming (L, t)-clumps in Genome.
    """

    # kmer_offsets is a fat (python integer per text character) inverted index
    kmer_offsets = defaultdict(list)
    for i in xrange(len(text) - k + 1):
        kmer_offsets[text[i:i + k]].append(i)

    clumps = []
    for kmer, offsets in kmer_offsets.items():
        for i in xrange(len(offsets) - t + 1):
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


def hamming(a, b):
    return sum(x != y for x, y in izip(a, b))
