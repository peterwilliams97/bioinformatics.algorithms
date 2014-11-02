# -*- coding: utf-8 -*-
"""
Python cheat sheet
http://www.astro.up.pt/~sousasag/Python_For_Astronomers/Python_qr.pdf?utm_content=buffer88e26&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer
"""
from __future__ import division, print_function
from utils import all_offsets, write_offsets, frequent_kmers


def find_in_genome(genome_path, pattern):
    text = open(genome_path, 'rt').read()
    print('-' * 80)
    print('find_in_genome: genome_path="%s",size=%d,pattern="%s" %d' % (genome_path, len(text),
          pattern, len(pattern)))
    offsets = all_offsets(text, pattern)
    out_path = make_outpath('%s.%s.offsets' % (genome_path, pattern[:10]))
    print('out_path="%s",%d offsets %s' % (out_path, len(offsets), offsets[:10]))
    write_offsets(out_path, offsets)


print('=' * 80)
find_in_genome('Vibrio_cholerae.txt', 'CTTGATCAT')
find_in_genome('Vibrio_cholerae.txt', 'ATGATCAAG')

find_in_genome('Thermotoga-petrophila.txt', 'CTTGATCAT')
find_in_genome('Thermotoga-petrophila.txt', 'ATGATCAAG')


def frequent_9mers(genome_path, start, end):
    text = open(genome_path, 'rt').read()[start: end]
    print('!' * 80)
    print('frequent_9mers: genome_path="%s",(start=%d,end=%d),size=%d' % (genome_path,
          start, end, len(text)))
    frq9mers = frequent_kmers(text, 9, 3)
    print('Frequent 9-mers=%d %s' % (len(frq9mers), frq9mers[:10]))


start = 786685
end = start + 540
frequent_9mers('Vibrio_cholerae.txt', start, end)
frequent_9mers('Thermotoga-petrophila.txt', start, end)

print('$' * 80)
text = 'aactctatacctcctttttgtcgaatttgtgtgatttatagagaaaatcttattaactga aactaaaatggtaggtttggtggtaggttttgtgtacattttgtagtatctgatttttaa ttacataccgtatattgtattaaattgacgaacaattgcatggaattgaatatatgcaaa acaaacctaccaccaaactctgtattgaccattttaggacaacttcagggtggtaggttt ctgaagctctcatcaatagactattttagtctttacaaacaatattaccgttcagattca agattctacaacgctgttttaatgggcgttgcagaaaacttaccacctaaaatccagtat ccaagccgatttcagagaaacctaccacttacctaccacttacctaccacccgggtggta agttgcagacattattaaaaacctcatcagaagcttgttcaaaaatttcaatactcgaaa cctaccacctgcgtcccctattatttactactactaataatagcagtataattgatctga'
text = text.replace(' ', '').upper()
frq9mers = frequent_kmers(text, 9, 3, include_rc=False)
print('Frequent 9-mers=%d %s' % (len(frq9mers), frq9mers[:10]))
find_in_genome('Thermotoga-petrophila.txt', text.upper())
