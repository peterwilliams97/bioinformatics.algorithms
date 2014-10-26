def word_count(text, pattern):
    cnt = 0
    for i in range(len(text) - len(pattern)):
        if text[i:i + len(pattern)] == pattern:
            cnt += 1
    return cnt


def clump(text, n, pattern):
    """clump aka frequent words"""
    return max(word_count(text[i:i + n], pattern) for i in range(len(text) - n))


text = 'GCACAAGGCCGACAATAGGACGTAGCCTTGAAGACGACGTAGCGTGGTCGCATAAGTACAGTAGATAGTACCTCCCCCGCGCATCCTATTATTAAGTTAATT'
patterns = ['GACG', 'CCCC', 'AGTA', 'TCCT']
for pat in patterns:
    cnt = clump(text, 30, pat)
    sym = '***' if cnt >= 3 else ''
    print '%s: %d %s' % (pat, cnt, sym)
