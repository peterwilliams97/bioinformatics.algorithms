import re

complements = {
    'G': 'C', 'C': 'G',
    'T': 'A', 'A': 'T',
}


def complement(text):
    return re.sub('.', lambda m: complements[m.group(0)], text.upper())


def reverse_complement(text):
    return complement(text)[::-1]

text = 'AAAACCCGGT'
text_c0 = 'ACCGGGTTTT'

text = 'GCACTAAAGCACCAGCGAGACTAGACAGTGCCTTACGCTGTATAGGGATAAAAGTTGTCAAGATGACTTGCGGGAATCGTTAGGCTGACACGCACTAATGCTCGCCTTCCGGGTGTTCTGTGAGTACGGTTGATCACGGTCGCCCTGCGGATGTACTACCATGAAAGTTGATCACGTGCCGCGCGCTCCCTAAGCTTAGAAGTTTGCACAATCTGCATTCTATCCTGCCACGCCTTCAATAATAAGTGGTGTATGCAATTTGGAGTCGATCTGGGAACCAACGATTAACTTGGGAAGTGGCTATATCAAAATACGATGTCTTCAGCGTCGCGGTCGACGCTGCGCAACGAACGAAAAGTCCGATGGACCCGAACTCTGATTATACCGAATCTCCGCTTTTACGACTCGCCACATACCGGCATAAGCCATTCTGGGGCTTTGCCCCCTTAGGTCTAGCCCACCCCCGACCTAGCTTGAGCGTGTCACACCCCAACAGCCGCATTACGCCCGCTCACCGACACTTGGCGGTCGTATAAGAAATCCAAAACCGAGACGAAAACTGAAGAATAAGGTTCATTCAGCATTGTGGAGTTGACAACATCAGTATGAGGGTGAGTTGCGTCAAAGTCGAAGAATATGGAGGGTCAAATCACGAGATGTAACATCCACGCGAACACTTAGCTAGTAATCATTTTTCCGTAAAGAGTCGTTGAGTCCGACCAGTTGAAGCTCAGTGTTTATCCGGTAGGGAATTGTAGGATCAACGATAGGGTCGCGGAACCGCCGTATTATAGAAAGAGATAGTCCCAACGTTCTTTATGCACTTCGCTGAGAGAGGGTGACCGGGCACGCAGAGACTTTGGCTTTGTAGCCCCATTCCGCGGCTCTTCGGATACTGACTGAGCTGTAGTCGGCACATCCTTTACAACAAAAAAGCTCATGTCCGAGATTTTAATGGCGGCGCACGGTCACTCGGAGTTGACGAATGCGCAGCGAATCGTTGGTTCCAGATAAAGGCAAGGCTGTGTTACTGTTTCGGAGGGCAATCGTCAACGAGCAAAGATGTTAGAATAGAAATCGGAGCGAGGCTCCCAGCAAATATGAGTTAGGATCTTTTTTGCGAAAGGGTTGGTCTCCATCTCCTCTCGCCTGCGAGCGAGTCCCCGAAGCACGTTCAACCTATTTGATTCGGTGCAGGACACCCTAGATTAGCATACAGGTATAATATCAGGAAGAGTCACCTTTCATTCCCGACCAGTAGGATGTATAGGAATGAGACTATCCAGTTCTTTGTCAGCTCAAGACAGCGTTGGCAATACGGCCGAGTATTGGGGGGAATACCCCGGAACATAGTATTGTGCCTTAGCTATTGCCCTAGATACCACGCGGCCCTTGAGCATTTGTCTACACTTTGGTGATCCTAGGCACCCCGCGCTCGTGGCAACGTCAGCATCTTGTGATAGCAAAGCGTATGTACCTGTAATGTAACATCAAAGTATATCGGCACCCTAGTGGGGGCGAAGGTTGGATCGCTTATCACTCGGGACGACGGTGGTATCCAGCCACAGTGTTGCTCATTAACGACCACACAGCTCTTGGAATCGAGCCATGGACAGGGGACGCCCCAGGATACATGATGTTCCTGTGAGCACAAGCACTATGGCAGGCTTAGAGCTAATTCTTCCATTGGGCCGGTAAGACGCCAGAGAAAGTCACCGGTGTGAGAAAGGGTTTCGTGTGGGGGAGGCGTCAAACAACAAGGATTTACGTCGAACCGATCAGCCCTTGTCTGATTCATTCCAGGTTTAAGCGAGCCCTGGCGGTGACCTCCCGGGGATTCTTGGTGACGATAAGTGTAGACTGGTTTATGACTGTCTATAAGTGCAAGCAGTCCGCGACTCGGCCGCTCCTCAGATCTCGTCCTCCCAATCCTTACGAGGCACTATTCCGGCCCTAAAAACTTACCTACCAACCGGACATAGCGAACGGTCTAAGTTTTCGGAAATTGAATAACACTCGAACAAAGGAGCCCAATACATGGCACAAGCACACATAAAGCTTGGCGCTGCTGACGGCCGGCCCCCACAGCAGGTGGGTATATCAGGATAATGCTCTACCTCCTCGGGGATGACCAGAGACGAACGTTCGGACGCTATTAGTTAGTGGTCGCCCAGATATTCTCCTAATCAAGCCCTCGAAGGCTAGTCTAAATTTTAGCAAAAACTCGTATAGCAGCACATGCGGTAGACTGGGCCTCAGCCAGGTAGAGCTGTGGCTGCACTCGAGCAATCACTACCGTATAGAGTGGTGTTATTTCGGGGTGAATGTCAGGGGTGGTCCAAAATCACAAACACGTCTATTCGCACCCGGGAATGCTCATGTTCCCACGGCGGGCCTGTACAGATGTGAGAGGCAGCGATCATACAAAGTTGCCTGGCCTCCCCACGAACACACGGCGGCCCATTAGGTCTGAACAGGTTTATCGTTAATATATTTTGCGGTGG'
text_c0 = 'CCACCGCAAAATATATTAACGATAAACCTGTTCAGACCTAATGGGCCGCCGTGTGTTCGTGGGGAGGCCAGGCAACTTTGTATGATCGCTGCCTCTCACATCTGTACAGGCCCGCCGTGGGAACATGAGCATTCCCGGGTGCGAATAGACGTGTTTGTGATTTTGGACCACCCCTGACATTCACCCCGAAATAACACCACTCTATACGGTAGTGATTGCTCGAGTGCAGCCACAGCTCTACCTGGCTGAGGCCCAGTCTACCGCATGTGCTGCTATACGAGTTTTTGCTAAAATTTAGACTAGCCTTCGAGGGCTTGATTAGGAGAATATCTGGGCGACCACTAACTAATAGCGTCCGAACGTTCGTCTCTGGTCATCCCCGAGGAGGTAGAGCATTATCCTGATATACCCACCTGCTGTGGGGGCCGGCCGTCAGCAGCGCCAAGCTTTATGTGTGCTTGTGCCATGTATTGGGCTCCTTTGTTCGAGTGTTATTCAATTTCCGAAAACTTAGACCGTTCGCTATGTCCGGTTGGTAGGTAAGTTTTTAGGGCCGGAATAGTGCCTCGTAAGGATTGGGAGGACGAGATCTGAGGAGCGGCCGAGTCGCGGACTGCTTGCACTTATAGACAGTCATAAACCAGTCTACACTTATCGTCACCAAGAATCCCCGGGAGGTCACCGCCAGGGCTCGCTTAAACCTGGAATGAATCAGACAAGGGCTGATCGGTTCGACGTAAATCCTTGTTGTTTGACGCCTCCCCCACACGAAACCCTTTCTCACACCGGTGACTTTCTCTGGCGTCTTACCGGCCCAATGGAAGAATTAGCTCTAAGCCTGCCATAGTGCTTGTGCTCACAGGAACATCATGTATCCTGGGGCGTCCCCTGTCCATGGCTCGATTCCAAGAGCTGTGTGGTCGTTAATGAGCAACACTGTGGCTGGATACCACCGTCGTCCCGAGTGATAAGCGATCCAACCTTCGCCCCCACTAGGGTGCCGATATACTTTGATGTTACATTACAGGTACATACGCTTTGCTATCACAAGATGCTGACGTTGCCACGAGCGCGGGGTGCCTAGGATCACCAAAGTGTAGACAAATGCTCAAGGGCCGCGTGGTATCTAGGGCAATAGCTAAGGCACAATACTATGTTCCGGGGTATTCCCCCCAATACTCGGCCGTATTGCCAACGCTGTCTTGAGCTGACAAAGAACTGGATAGTCTCATTCCTATACATCCTACTGGTCGGGAATGAAAGGTGACTCTTCCTGATATTATACCTGTATGCTAATCTAGGGTGTCCTGCACCGAATCAAATAGGTTGAACGTGCTTCGGGGACTCGCTCGCAGGCGAGAGGAGATGGAGACCAACCCTTTCGCAAAAAAGATCCTAACTCATATTTGCTGGGAGCCTCGCTCCGATTTCTATTCTAACATCTTTGCTCGTTGACGATTGCCCTCCGAAACAGTAACACAGCCTTGCCTTTATCTGGAACCAACGATTCGCTGCGCATTCGTCAACTCCGAGTGACCGTGCGCCGCCATTAAAATCTCGGACATGAGCTTTTTTGTTGTAAAGGATGTGCCGACTACAGCTCAGTCAGTATCCGAAGAGCCGCGGAATGGGGCTACAAAGCCAAAGTCTCTGCGTGCCCGGTCACCCTCTCTCAGCGAAGTGCATAAAGAACGTTGGGACTATCTCTTTCTATAATACGGCGGTTCCGCGACCCTATCGTTGATCCTACAATTCCCTACCGGATAAACACTGAGCTTCAACTGGTCGGACTCAACGACTCTTTACGGAAAAATGATTACTAGCTAAGTGTTCGCGTGGATGTTACATCTCGTGATTTGACCCTCCATATTCTTCGACTTTGACGCAACTCACCCTCATACTGATGTTGTCAACTCCACAATGCTGAATGAACCTTATTCTTCAGTTTTCGTCTCGGTTTTGGATTTCTTATACGACCGCCAAGTGTCGGTGAGCGGGCGTAATGCGGCTGTTGGGGTGTGACACGCTCAAGCTAGGTCGGGGGTGGGCTAGACCTAAGGGGGCAAAGCCCCAGAATGGCTTATGCCGGTATGTGGCGAGTCGTAAAAGCGGAGATTCGGTATAATCAGAGTTCGGGTCCATCGGACTTTTCGTTCGTTGCGCAGCGTCGACCGCGACGCTGAAGACATCGTATTTTGATATAGCCACTTCCCAAGTTAATCGTTGGTTCCCAGATCGACTCCAAATTGCATACACCACTTATTATTGAAGGCGTGGCAGGATAGAATGCAGATTGTGCAAACTTCTAAGCTTAGGGAGCGCGCGGCACGTGATCAACTTTCATGGTAGTACATCCGCAGGGCGACCGTGATCAACCGTACTCACAGAACACCCGGAAGGCGAGCATTAGTGCGTGTCAGCCTAACGATTCCCGCAAGTCATCTTGACAACTTTTATCCCTATACAGCGTAAGGCACTGTCTAGTCTCGCTGGTGCTTTAGTGC'

text = 'TCCGCCGGGTCATTGAATCACCACAACTCATTAGTAGACTTGCGGTTACTGAGCGTCGTAATACTTTTTCTTGTTGAGAACGGGTCACGCAGGGGATGGTAGGGGTAAAGGGGTTCCTTAAGCCGATGCTAAGAAGAAGGTTCACGTTATCGTTCAGTGTCTTGACAATCTCTAGCTAGAGTGCCTGTCGGCGGCCGTACCGTAGTTGGGGGGATCGGAGGCCGTCACCCACATTAACTACTATCTTGGCACTTCGACTATTTGAGGGCTCCACGGTCCAACGCGGTCCCGTTCCTTCCGGGTAGTCAGCGCATATCTATGTTACAAACTGTCGCGCTTCTGACTCAGACCGGATATGTGGCCAGCAGCTAACGTTCACAATAGTTACTTTCTCATTGGCGACTCCTAGAAATACGTTTTGGCCCACTTACCTTCGGTGCAGTGGGAACGGCCAAGTTTGTCCTACACGTTAGCAAATACACTTGTTCCCCCAGTTATGCCGGGGTCTATACCAAGCTCACAGGAAAACTGGGGGGTGCGTAGACGGCGAAACAAAGAAGTTAACTTTGGCCCGAACAGTGTCAGTCACAGGTGACAATCGGCACGATGTTAAAAACGCGTATTCACCTACCAGTTATGTTTCGCTACTTATACCCCGGGTTCTCGCCGGCGATGACCAGAGTAACTTCCCTGGCTGGTGGCTATATAAGGCGCTCAATTTTGCTGGCCGCGCACAGTTATGGAATCTCATGAGGATACCGTAAAATTAACCCATGCAGGCTATCTTGTACCTGATGCGCGATAACGCCGTGACGCAACTGAACAGATTATTTGTTCATCTACGCCCGGGGCTCCATCCTAATGACCTCGTGTCCCAACGCAGATGTAGTTGCTTTCAAGCAAGTCCTGTCTCTACTGTGGGTTCTGGGGCCGTTCGTAATTCGTCTGTAAAAAACCGACAAAGCCTTCAGCAGTCTTATGTATGGACGGAGGGTATCTGTAGACCCTTTCAGCGGACGGCGTCGTAAAGCGTTACCCAGATCTATAACGGAAGTGTTGTCGGCCAATAGGGCGCCTAAGATGCGCCGCACTATGCAAGCTGTAGGAGCTCTCTGGCCTTTATCAGCTGGGGGCATTCCCGGGGGACCCTTCCCAACAACGGTGTGTCGGAGAGGCAAGGTCTTCCGCCGAAATGGTTGAAGCGGCCATCTCGACATGAAGTGTGCGTGTCTATCTTGTGCCATCTTTTGGAGAGGCTCACAACTATTTAAGAACTCGAGACTGTCATTCTATAAGCACAATCTTGCAAGTTCGTAGCACAAGCATGATCATGTCTACATACTACTTTAAAGTCATTGCCGATGTGAGACACAGCCCTCTAGGCATTTTGAAGTAGGTGTTATCGCGAAACGACCGGGCGCAAACGTACCAACAGCTGGTGCATAATCAGGGCCTATGTGATTGCTCAGACCGTTAAACTTATCGGGACCTGCCGCTCTAGGATCTGGCCCCGGAAAATATCTGACTTTCTCAGCTTCCCATTCACCATACATTGAAGGCCTATCAAGAGGAGGAATCGAAGCAAGAAACGAGATACGCCGCTGGGACTCCTTTCAGGTTGGTGGTGTCCGTGTGCACGTCCCTATGTCACCGGCAAACGCTAATTTACGGCTTACTGATGGCGTCTGGAACTACCCACGCGGGCCAAGCCCCCTTAAAAAAAGGATGCGTAACCAAATAGTAGCATTGTAACCTGCCCCTACACAACATAGTTGGGACACGCTTACGAGCACCAGACGTTTAGAAGAGGGCAGTCTCAAGCTGTATCTAGTACAATCCAATAACGAAGGACCCTATGTTCGGTGGCGACACTCGCAGCGAGAAATACCTGGTTGCACGATATTAAGCCGCCCTAGTTCCGCTTCAGTAGGAGCATTCCAGAGTGTCATTGAGCAGTAGTTCCTCGCTTTTATATGCACGCGCTTCCATCTTTTTCAATATGGAACTTGTTAAAGGATACACTTTGACCATTCACCGAATGCCCTCGTCTCTCGTAGCCGGCGCCTTTCGACCACTCGTTGTCGGGTTTAGTGTTGTATGTGGGAGGCCGACAGCTGTCAAGGCCGTAAACCCGAAATGATGACAAGCTGACGTTCACCCGGGAGGGAATATTGATTGTGATGCTAAGGCGCTAAGACTGCTTGCCTACGGTGTGGTCATAACCCGGAATTGGACATCTAGGGGTGGCATTGAAGACGCTCCCCTCATGCACAGCTTCACCGATCACCTGCACGCTCTACCGATTATCTTTTACTCTGCTAGACCATGACCCTGATGGCCAGAGTTGATACTGTCTCTCAGGACCCTAACCATTCGGCGTAAAACAGGGGAATTACCCTGAAAGACAAACAGCTTTGGTTCGCCGCCAAATACCAGACCGTGGGCCACTAGGGGAAGGCCGCATCGCTGAATCTACTTAAGGTCCGCGCCATGCCCGCAGCAGAGATATGTATCCTCAGGTGTGATCCCGAGCCTGGACCCACACCTATGTACGAAGTGCCGCTTACTCATCCGTTCAAATCCAAGCGCGAGAGTTCACAGGAACGGCATAGTCTTGGTAGGGCGGCTTGCTGGTACCTCCTCGGGATACAATGCGACCACTCTAGACGAACGTCCGAGGGCACGCATTTCGGCACATATGTCGCCCGGATCGAATATGAGGTGGCGCTGATCGGTTAGCGAGACTCTATCCCAATCTAATGGTTGCGAGCATCTCCGAAGTACTTTCGCCGACTCACAACTCGTACGGAAGTCCAGGCTGCTGATGAAGGTAACATTGTTTAACCTTAGACGGATACTCGTTGACTGCTACTCTAATTCTAAAAGCAAATTCCCCGGAAAACTGCTTGGAAAAGCATCACCTAGGCTTAGATCCTCATCCCAGCATGAGACTGCTGTACAAACATCAGTTGAAGGCACCTATTCTACGCATGAATGTAGAGGTGTGCGGTTACATACAGTAAGCATGGGTCCGTTAGCTGATAAGGTCAATCTAGACCAGCAGTCGAATTAGGTGGTTATCCCGGCGCGGGCACAAGGGTGGCTAGATTGCTAGGTAATAACAGGTGCTACTCACGTGGGGCATAAGGAACAAGTGCAGGATTAGCGTGGACTAGCACAAGGTTGCGGTCCCGTTTATTGTCGGATTGAATGCGCCCTTCGAAAGAGGATCATGAACACGCCTGCGCAACGTCACAGGGTTGTTTGTGCTTAGTTATTACTGTAACAGTATCTATATCTAGTGAATACCGACAGGTCTGGCGTTATCTTTCCCGGTCTCTACACAGAGCCGTACCTATCAAACTTGATCCGTGTGTCCATAAGCTTCTTTGCACGTGTACTCTCAAGGGGGAACGTGCCGTCGCGATACATTGCGATGTTATCGGTCGTAGTGACCAACTGCGACTCACAGGAGTTTATAGCGTAACCAACTGATGATGGCGCAATACGTACGTCCTGGCAACATGAATGTGGTTCACGATAGCACTATTGGGGCGACGAACAGGATCCACTTAGTGAGTTGAAGAGCCCAGCTACAAGGCAATCCCGCGGCTGACTTGGTTTGAGGGTGTTCCTCGTTCGGTAATGCGCTTATCGGCCCGACTACGCTGCTCCGACAATGGGAGGAACATTACACGTTTAGAATCCACGGTGAAGGCGAGTCCTCCGCTTCTGAAGACGTTTGTAGCGAAGGCGTGGTAGTTCACTTACGCTTACAGTCCAAATCAGTTGGCCGAAGCCCATCCGTCTCGTTTACGCCAGGCAATGCTGTTGGTCCGAATTGCTAGTTTCCGTAACTGACCATTAATCTAGATCTTGTTGGGATACCGGTTACGGTATCCTACCGAGCCCGTCTGAAAGGGTGCCGGAGTCTGCTGCGTCGCCTGCAGTCGCGCCTTCCGACCCGAAGTAGCTGGTGGAACACGAAGGTAGAGGAAAGACTCTGGTGCGACCTGAATCTCGGACCGATAAGAGGTCCGCGTGGCAAGCTCGCGCATAGTCCGAGTTGCATTGTACCGGGCTGCTCGAGCCCAAATCAGTACCTAAGCTGCTTCAGGAACATCGCGTTCATAAGCGCGAGTACAGTTATAAAGATTTGTTTTGAGTACGCTGAGACGGCTGCTGTAACTGCAGTGTGGGGATCGCGGTCTTATATAAGGGAAGGTTTCGGGCTGCAAAGGGTCTTAAGAGGGAAATACCACCATACAACTCTAGGCAAAACGGTTCGGCCATGATCGCGGGCTGTAGACAGGATTGAAAGTCTATCATGCCATGATAATTCCGGATATTCATCGACGTTATTGAATGGCACCCCAATGATTCATAGAGGACCCCCTGTTACACGGCTAGACACCGTCCACCCTTTTTAAAGTCGGCTGGGTTATGGAAGCAAATGAACGCCCATAATTATTGTTAGGAAAGACCCCACTATATACCAACAGGAGCGTGATCCTCAAATACCAATCAGCGGGGGACGTAAAGCCGCCCCGCTCCTGCCTACCAATTTCGTCCCTGGATGCCTGCCTCCGCCCTTAACGCACCGTACGGAGCTTAGATCTCACGGCCGATTAATGCGGAGACCTTGTTGCCAATGACTGCCTCCGATAGGAAACGATAGCGGGGATAAATAGTTGAGATGTATGGCGAGCTCCTCTTGCTGTAATTATTCGCCGGTCCTCCGACCACGGTAGACGTTCCCTTAGGGCTGAGGGACACATGAGCGCCTCGTCCTAAAAGCATTATTGTCATGGAGAAACTCCTATCCTAAGCATCATGAATCATGCGCATAATACTTTAATGGTAGGGCGATCACCCGGTCTTGCGGGGATTCTAAGAACATGAAGGTTCCGACTAGCAGTAAGTTTATTCGATCGAACAGACTTTGTACCTTACCAGTAGCGACGGGTGGATCATAGTGCTTGCAGCAACGTAGTGACTTGGGTCAAAACCGGGTGCAGTGGCGGTCTGCTAGGGAAAGGACCTGTCTTGGCAGTGCACCGACATTTGTCCTCCTCGACATTCGAATGCTCCTGTCTCAGTGATTCGTTGATAGGCTATAGACCGTGGTGTCGAAGACAATGCTCAAAACAAAGCAGCTTGCACGTCGCATCAAGAGGAGGTTGTCTGTCCGCTTAGAGGGGGCAGATATGAAATGGCTACGAGGTCAAGAAAGGTAAATGGAGCTAACACTTACCACTGTCTCCTTTGACCTAATCGTCATAGGAATCAGGCGTCGACCTCAGGTAATGCGAACCCGTGCGCCCACCGTTGATCATCCAGGCGTAGTAGATAAAACAGTAATAGTTTAAATGGTGTAACTATCCAGCCAGCTTTGGCATCCGATGGCGACAAATCCGAGCGCAATGCCCTAACGGCTAAAGGAGACATACACTAGCGTGACAGCTCAGTAGAATCTACTCATCTGCATAAGGCTTTATGGCGGTGGTAAGAGACGTCCGCATCAGCACTTCACGCTTGTAGACTGAAGAACAGGGCTAAAAGGGTGGACCGTCCGACCTGTTTTGCTCGCGTTAGGCCTGAATGGATAGGGGGGTTATTAGTGTCCGAGATGTAACCACTAACCCGACCCCTGGAAGCTGAGATATGGTCTTCGGCCCCGGCAACGGGCGTCCCCAGGTGGGTCATGCGGAATTCGCAAGACTTTAAGTACCGTTGCAGAGAGATATTCAATGAACTAGCATAAAGAAGGGGGCTGGCCCCTCTTGGCTAACAGCGGCATAGATTGAACTTATGGAGTATGTTAGATATACCTCACGGCCATATGGGTGGTTAACCACCGGCGCGGATATCACTACCGATGGAATGGCTTGTGCGATCCCTCGACTTAGTGGCAGGTCCCTGCGGTTATTCTTGCAGTCTCGCGTGGAGTCTGAGCAGGCTTGGTGGCAGTTTAGAGTTTGGCCAGGTGAACGAAGGTACCCTCCGATCGATATGATACTAGCAGTGGCTAGAGATTCTATACGGTGGGCTATAAGGTCTAGTGCGATCCTCGTGCAAGTGACTATAGTCGCGAAGCAAAGCAGCCCCATTTCTCGCTAATAATGGCACATGCGGGCAAATCACCGGGGGATTACTAAATTGGTAAACTCTTGGGGGCAGTTAAAATGTTATAGGACAGAGCTCTGCTACCTTCGTCATCTGCCGTCCCACGATCACGCTCATGCTTCCTGACACACATATCGTTTATCGGGCGGACTCGGCATAGCGAACGGAACACGACCATGAGAACTTTAGGGTCTACGAAACTCGTTCATGGGAACGTGGGAGGTCTATTGATATATCCGGGATTAAGTGTATCCAACAGCAAGTACAGATTCGATGGTCCCTGCAGGCGCCCGCTTACGTGGTTCACAGGTGGGTCGATTACTCTTGTCGAGGGTGTACATAGCTGGGACAATTAAATATTAGCCTAGGCGCAGAACCGGTGACATTCACCCCAGCAGCAATGCGGCGGCGCTCGATGGATTTTCCTGCGGAGATCCGACCGCTTATCATTGGAGTGGGGCCATCTCGGTTCCAACCGTGTTAGTGATCACGGAAACTCCAGCTGTTTTAACGACGTTTGAGAAGGGCTCGTCACTCAGGCCCAGATCCTTGCACGCGGAAGAGCCCGTGTATTAGTGGTCTCAAGTGGTGAAACGTACCACATCCCCGTCAATCAGTTAAAACACGGGCGCCAACCTTGAGTACTTTCTGTCCGGGGTTCCTAACTGTAGTATAGCACTTGCACAGCTTGAATCCCTATCGCCCTTATCTACTTGATTCGCCGGAGCCCTAGTACCGTCGAGTATCTACTTCTTAGCCCGTTAGAAGGTCGGTACTAATATAAGCGCCGTCTTGGTCCCGATTGGATGTCAAGCCCGCTATGTACGGCGAGTTCTCCGTCCGTACATAGGTTGACCGCCTCGAGACGCCAGATGACCCGAGTAGGTCAACAAATAAAGGAGTCCCCGGTACTTAAACACGGGGCGTGCATCCCGATGAACCGGGGTTAATTATAGCTGGTGTCGTTGAAAGCGCTTTCAGATAACTTGCGTGGCAGATTTCAGGGATGTATGCTTGGTCCGCAACCGACCCGCGCGACGCACCTTCTGCGATGAATACATATGTTCTTGAGTCCCCTGCAGATAACTTTCGGGTGCTAAGGCGCTAATCATGAATTTTATCACTCGTACCGCAACTCGGGCGCTAAGCATGGTATAGCACGGTACATCCGATGCTACTTGAAGCATACTATCATATGTATGGGTGGTTCTTAAGATCACTGGATACTTGGAAGACAAACTAACAAGGGATTAGGCCGGAATTTGATATACAACTGTACAGCAGGTACTCTCTCCATAAAGACGCCTCCGAATACACTTAATTTCAAGTCGCCCGGCGGAATTAGATGCCGGGCTATAAGGATTATGATGCTGCCCGAATGAAGCGGCGGTACCGGTATTGAATTGCCTTATGAACGACTCCAGGCCCGGTGAATAGAGCGCAGAAATCGGCTTACAGTTAACTTTTAAAGAGCTCAACTAGAACTAAAGGCGACATTCGGTCTAATCGACTCGCGAATGTCGTAAAAGTCCGGAAGCTGTCCAATATGCTCACCCGACGAGCGGAAGTGAATACATTATGAGCACCATCGTGGTCGATTCCATTATGACAGCAGGCCGTCTAACGTCAGACATATCCCGGTGCGCAGCCGTTCTCAGAGGTAAGAGGCTGCCTCGATAGACTAACAATCGATGTACGACCGGAAGGTGGCCCCAACCAGTTTGCAAACAGCGAGACGTCGCAGTTTGCCTTACTGGTCATCGAGATTCCGAATTGGTAAATTTCGTCAGAGCGGACCCATAACGAACCAAAACGGTGCCGGTTTTGCACCTTATTCTTGGTGGCGCATGACTATTGGTCAATTTTTTCTAAAATATCCACTAGACCATAATCCATGAGAATTAGGGGGGTTCGGCCGTAAGGTTTTGGACCAATTCACTATGCAACAGTCATGCCCGCTCCTTGGCAACTAGAATGGACCAGACCAGCGGAGGTTTCATTTCCTCCCTCCCGTCTATCCCAGGACTTTTGCCGCACGAACCGCCACAGATTTCGTTAATGGTCTAGATACACTAGATAGCGTTGATAATGGAGTAACTTATGAACAACTCCCAGAGGATCTTATCGAATGGGAAATTCTTACGACCCTTTCCCATACCAGATGAAATAAAAATTACGACCGGGGTTGCGTGACGAGTGAGAAGTGCTAACGTATACCTACCTTACCAGAGCTGGACTCGTACTCGGCATACGCTGCGTGAATTTCCGGTCCATATGGAGCGTATACTGTCGCTCATGTAGTTCACGTTTCTGCGTCAGATCTCACACATAGGGTATACATCATGAGGGGTTTCGATGGCTTGGGTTCGAAATTGGGAGGATAATCCGAACGTGCAGCTATCACAGAGCGCTTCTAGATACTATCGTTCGATCGGAGACTGCAGCAGGACGCCCCATAGTGTAGTCAACCTAGGCGCGCCTTTTGATGTCCCTTTGGCGTCTGTGAGTGCAAATTGACTGATTAGCGCAGTTGGTCTCTAGCGTAACAGGGCGACCAACTATCCCGCTAGGTAGGCAGTCTTACCCGGCAAGTGTTTAGGTGCAAACAAGATCAAAGCTCGCCACCGCAGTACGTCTATTCTCGCTCAGAGGCTATATGAAGCAGGATTATACTTTCGCTTAACGAATAGCAATCATGGTCTGTCGCTGTTTCTTATCTATTGATAAAGAGCCCACTATTTCCCCGCCTCAGAGACATACAGCAACTTGGACAACGTGAGGCATTCGGAACGGCGGGATCTCGACTCGGGGCGCGCTATAATGTTCGACCCAAACTATGCGGCTTGATCACATAACCGTAACCCTCCAGCCCTGTGAGGATAGGTTCACGCGATCGGTGAAAGCTTGGGTAACACTTTTGGCGGATCGGCTTGTTTATTGGCGATTCAAGTGTGATCCAAGACAATGCCTGC'
text_c0 = None

text_c = reverse_complement(text)

print '=' * 80
print text
print '-' * 80
print text_c
print '+' * 80

if text_c0:
    print text_c0
    assert text_c == text_c0