import operator


def skew(text, k):
    """#G - #C for first `k` neucleotides of Genome `text`"""
    return text[:k].count('G') - text[:k].count('C')


def skew_values(text):
    return [skew(text, k) for k in range(len(text) + 1)]


text = 'CATTCCAGTACTTCATGATGGCGTGAAGA'
skews = skew_values(text)
min_index, min_value = min(enumerate(skews), key=operator.itemgetter(1))
max_index, max_value = max(enumerate(skews), key=operator.itemgetter(1))

for i, sk in enumerate(skews):
    c = text[i - 1] if i > 0 else ' '
    is_min = '---' if i == min_index else ''
    is_max = '+++' if i == max_index else ''
    print '%3d: %s %3d %s%s' % (i, c, sk, is_min, is_max)
