def word_count(text, pattern):
    cnt = 0
    for i in range(len(text) - len(pattern)):
        if text[i:i + len(pattern)] == pattern:
            cnt += 1
    return cnt


def all_kmers(text, k):
    return {text[i:i + k] for i in range(len(text) - k)}


def frequent_kmers(text, k):
    kmer_set = all_kmers(text, k)
    kmer_cnt_dict = {kmer: 0 for kmer in kmer_set}
    for i in range(len(text) - k):
        kmer_cnt_dict[text[i:i + k]] += 1
    return sorted((kmer, cnt) for kmer, cnt in kmer_cnt_dict.items()
                  if cnt == max(kmer_cnt_dict.values()))

if __name__ == '__main__':
    text = 'atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaacctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgaccacggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtttccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc'

    for k in range(3, 10):
        print k, frequent_kmers(text, k)
