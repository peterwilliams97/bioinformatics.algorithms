"""
    Word count with mismatches
"""

ALPHABET = 'ACGT'


def word_count(text, pattern):
    """Return number of instance `pattern` in `text`
    """
    cnt = 0
    for i in range(len(text) - len(pattern)):
        if text[i:i + len(pattern)] == pattern:
            cnt += 1
    return cnt


def mutate0(chars, indexes, mutations):
    if not indexes:
        return
    elif len(indexes) == 1:
        n = indexes[0]
        pre = chars[:n]
        post = chars[n + 1:]
        for c in ALPHABET:
            mutations.add(''.join(pre + [c] + post))
    else:
        for n in indexes:
            pre = chars[:n]
        post = chars[n + 1:]


def mutate2(pattern):
    mutations = {pattern}

    for i in range(len(pattern)):
        for j in range(i):
            for ci in ALPHABET:
                for cj in ALPHABET:
                    chars = list(pattern)
                    chars[i] = ci
                    chars[j] = cj
                    mutations.add(''.join(chars))
    return mutations


def word_count2(text, pattern):
    """Return number of instances `pattern` in `text` with up to `n` mismatches
    """
    mutations = sorted(mutate2(pattern))
    return sum(word_count(text, pat) for pat in mutations)


text = 'CATGCCATTCGCATTGTCCCAGTGA'
pattern = 'CCC'

text = 'CATGCCATTCGCATTGTCCCAGTGA'
pattern = 'CCC'


cnt = word_count2(text, pattern)

print text
print pattern
print sorted(mutate2(pattern))
print cnt

for pat in sorted(mutate2(pattern)):
    print '%s %2d' % (pat, word_count(text, pat))
