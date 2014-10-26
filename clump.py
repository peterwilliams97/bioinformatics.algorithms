def word_count(text, pattern):
    cnt = 0
    for i in range(len(text) - len(pattern)):
        if text[i:i + len(pattern)] == pattern:
            cnt += 1
    return cnt


def clump(text, L, pattern):
    """clump aka frequent words
        Return max # times `pattern` occurs within a length `L` substring of `text`
    """
    return max(word_count(text[i:i + L], pattern) for i in range(len(text) - L))


text = 'GCACAAGGCCGACAATAGGACGTAGCCTTGAAGACGACGTAGCGTGGTCGCATAAGTACAGTAGATAGTACCTCCCCCGCGCATCCTATTATTAAGTTAATT'
patterns = ['GACG', 'CCCC', 'AGTA', 'TCCT']

text = 'CCGACAGGCTAGTCTATAATCCTGAGGCGTTACCCCAATACCGTTTACCGTGGGATTTGCTACTACAACTCCTGAGCGCTACATGTACGAAACCATGTTATGTAT'
patterns = ['TACC', 'TTTT', 'CTAC', 'CTCT']

for pat in patterns:
    cnt = clump(text, 30, pat)
    sym = '***' if cnt >= 3 else ''
    print '%s: %d %s' % (pat, cnt, sym)
