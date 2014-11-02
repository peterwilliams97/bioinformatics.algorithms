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


def find_clumps(text, k, L, t):
    """Clump Finding Problem: Find patterns forming clumps in a string.
     Find all `k`-mers that occur `t` or more time in substring of length `L` in `text`

     Input: A string `text', and integers k, L, and t.
     Output: All distinct k-mers forming (L, t)-clumps in Genome.

     """

if __name__ == '__main__':

    text = 'GCACAAGGCCGACAATAGGACGTAGCCTTGAAGACGACGTAGCGTGGTCGCATAAGTACAGTAGATAGTACCTCCCCCGCGCATCCTATTATTAAGTTAATT'
    patterns = ['GACG', 'CCCC', 'AGTA', 'TCCT']

    text = 'CCGACAGGCTAGTCTATAATCCTGAGGCGTTACCCCAATACCGTTTACCGTGGGATTTGCTACTACAACTCCTGAGCGCTACATGTACGAAACCATGTTATGTAT'
    patterns = ['TACC', 'TTTT', 'CTAC', 'CTCT']

    for pat in patterns:
        cnt = clump(text, 30, pat)
        sym = '***' if cnt >= 3 else ''
        print '%s: %d %s' % (pat, cnt, sym)


