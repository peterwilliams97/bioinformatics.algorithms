def hamming(a, b):
    return sum(x != y for x, y in zip(a, b))


a = 'TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC'
b = 'GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA'

h = hamming(a, b)
print len(a)
print len(b)
print h
print float(h) / float(len(b))
