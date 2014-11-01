import re
from collections import defaultdict
from operator import mul

def product(a_list):
    return reduce(mul, a_list, 1)

# From http://www.hgvs.org/mutnomen/codon.html
CODON_SOURCE = '''
    One letter
    code    Three letter
    code    Amino acid  Possible codons
    A   Ala Alanine GCA, GCC, GCG, GCT
    B   Asx Asparagine or Aspartic acid AAC, AAT, GAC, GAT
    C   Cys Cysteine    TGC, TGT
    D   Asp Aspartic acid   GAC, GAT
    E   Glu Glutamic acid   GAA, GAG
    F   Phe Phenylalanine   TTC, TTT
    G   Gly Glycine GGA, GGC, GGG, GGT
    H   His Histidine   CAC, CAT
    I   Ile Isoleucine  ATA, ATC, ATT
    K   Lys Lysine  AAA, AAG
    L   Leu Leucine CTA, CTC, CTG, CTT, TTA, TTG
    M   Met Methionine  ATG
    N   Asn Asparagine  AAC, AAT
    P   Pro Proline CCA, CCC, CCG, CCT
    Q   Gln Glutamine   CAA, CAG
    R   Arg Arginine    AGA, AGG, CGA, CGC, CGG, CGT
    S   Ser Serine  AGC, AGT, TCA, TCC, TCG, TCT
    T   Thr Threonine   ACA, ACC, ACG, ACT
    V   Val Valine  GTA, GTC, GTG, GTT
    W   Trp Tryptophan  TGG
    X   X   any codon   NNN
    Y   Tyr Tyrosine    TAC, TAT
    Z   Glx Glutamine or Glutamic acid  CAA, CAG, GAA, GAG
    *   *   stop codon  TAA, TAG, TGA
'''

PATTERN = r'([A-Z\*])\s+(\S+)\s+(.+?)\s+((?:\s*[ATCGN]{3}\s*,?\s*)+)$'
RE_LINE = re.compile(PATTERN)
RE_CODON = re.compile('([ATCGN]{3})\s*(?:,|$)')


if False:
    line = 'AAA, TTT, GGG'
    m = RE_RLINE.search(line[::-1])
    print line
    print m.group(0)
    print m.groups()
    exit()


if False:
    for line in CODON_LINES:
        m = RE_LINE.search(line)
        if m:
            print line

DNA_CODONS = {}
CODONS_DNA = defaultdict(set)

print '=' * 80

for line in CODON_SOURCE.split('\n'):
    m = RE_LINE.search(line)
    if m:
        #print m.groups(),
        sym, name, desc, codons_str = m.groups()
        codons = RE_CODON.findall(codons_str)
        print sym, name, desc, codons
        for cdn in codons:
            DNA_CODONS[cdn] = sym
            CODONS_DNA[sym].add(cdn)

        #print [s[::-1] for s in r.groups()]


RNA_CODONS = {k.replace('T', 'U'): v for k, v in DNA_CODONS.items()}


AMINO_ACID_SOURCE = '''
    1-letter code   3-letter code   Chemical formula    Monoisotopic    Average
    A   Ala C3H5ON  71.03711    71.0788
    R   Arg C6H12ON4    156.10111   156.1875
    N   Asn C4H6O2N2    114.04293   114.1038
    D   Asp C4H5O3N 115.02694   115.0886
    C   Cys C3H5ONS 103.00919   103.1388
    E   Glu C5H7O3N 129.04259   129.1155
    Q   Gln C5H8O2N2    128.05858   128.1307
    G   Gly    C2H3ON    57.02146    57.0519
    H   His C6H7ON3 137.05891   137.1411
    I   Ile C6H11ON 113.08406   113.1594
    L   Leu C6H11ON 113.08406   113.1594
    K   Lys C6H12ON2    128.09496   128.1741
    M   Met C5H9ONS 131.04049   131.1926
    F   Phe C9H9ON  147.06841   147.1766
    P   Pro C5H7ON  97.05276    97.1167
    S   Ser C3H5O2N 87.03203    87.0782
    T   Thr C4H7O2N 101.04768   101.1051
    W   Trp C11H10ON2   186.07931   186.2132
    Y   Tyr C9H9O2N 163.06333   163.1760
    V   Val C5H9ON  99.06841    99.1326
'''

RE_AA = re.compile(r'([A-Z])\s+(\S+)\s+(\S+)\s+(\d+\.\d+)\s+(\d+\.\d+)')

CODON_INTEGER_MASS = {}
print '-' * 80
for line in AMINO_ACID_SOURCE.split('\n'):
    m = RE_AA.search(line)
    if m:
        sym, name, formula, m1, m2 = m.groups()
        m1 = float(m1)
        m2 = float(m2)
        print m.groups(), m1, m2
        assert abs(m1 - round(m1)) < 0.3
        assert abs(m2 - round(m2)) < 0.3
        assert m1 >= round(m1)
        assert m2 >= round(m2)
        assert sym in CODONS_DNA, sym
        CODON_INTEGER_MASS[sym] = int(round(m1))


from itertools import chain, combinations


def all_subsets(ss):
    return chain(*map(lambda x: combinations(ss, x), range(len(ss) + 1)))


def all_substrings(text):
    return {text[i:j] for j in range(len(text) + 1) for i in range(j + 1)}


def all_substrings_cyclic(text):
    return {s for i in range(len(text)) for s in all_substrings(text[i:] + text[:i])}


def mass_protein(protein):
    return sum(CODON_INTEGER_MASS[p] for p in protein)


def mass_spectrum_linear(protein):
    return sorted({mass_protein(p) for p in all_substrings(protein)})


def mass_spectrum_cyclic(protein):
    return sorted({mass_protein(p) for p in all_substrings_cyclic(protein)})


def score_linear(protein, spectrum):
    p_spec = mass_spectrum_linear(protein)
    return len(set(p_spec) & set(spectrum))


def score_cyclic(protein, spectrum):
    p_spec = mass_spectrum_cyclic(protein)
    return len(set(p_spec) & set(spectrum))


def triplets(rna):
    return [rna[i: i + 3] for i in range(0, len(rna), 3)]


def rna_to_protein(rna):
    return ''.join(RNA_CODONS[s] for s in triplets(rna))


def protein_to_dna(protein):
    for c in protein:
        print len(CODONS_DNA[c]), sorted(CODONS_DNA[c])
    print

    return product(len(CODONS_DNA[c]) for c in protein)


rna_candidates = [
    'CCCAGGACUGAGAUCAAU',
    'CCCAGUACCGAGAUGAAU',
    'CCUCGUACAGAAAUCAAC',
    'CCAAGUACAGAGAUUAAC',
]

rna_complements = {
    'G': 'C', 'C': 'G',
    'U': 'A', 'A': 'U',
}


def reverse_complement(text):
    return re.sub('.', lambda m: rna_complements[m.group(0)], text)[::-1]

print '-' * 80
for rna in rna_candidates:
    for r in rna, reverse_complement(rna):
        protein = rna_to_protein(r)
        print rna, triplets(rna), protein

print '-' * 80
protein = 'LEADER'
n_dnas = protein_to_dna(protein)
print protein, n_dnas

print '-' * 80
protein_list_cyclic = [
    'IAMT',
    'TLAM',
    'ALTM',
    'TMIA',
    'TALM',
    'MTAL',
]
actual_ms = [0, 71, 113, 101, 131, 184, 202, 214, 232, 285, 303, 315, 345, 416]

print '%5s %5s %s' % ('', '', sorted(actual_ms))
for protein in protein_list_cyclic:
    ms = mass_spectrum_cyclic(protein)
    ok = all(i in ms for i in actual_ms) and all(i in actual_ms for i in ms)
    print '%5s %5s %s' % (protein, ok, ms)


print '-' * 80
protein_list_linear = [
    'TCE',
    'TCQ',
    'AQV',
    'CTQ',
    'ETC',
    'VAQ',
]

actual_ms_linear = [0, 71, 99, 101, 103, 128, 129, 199, 200, 204, 227, 230, 231, 298, 303, 328,
                    330, 332, 333]

print '%5s %5s %s' % ('', '', sorted(actual_ms_linear))
for protein in protein_list_linear:
    ms = mass_spectrum_linear(protein)
    #ok = all(i in ms for i in actual_ms_linear)
    ok = all(i in actual_ms_linear for i in ms)
    print '%5s %5s %s' % (protein, ok, ms)

print '-' * 80
peptide = 'MAMA'
spectrum = [0, 57, 71, 71, 71, 104, 131, 202, 202, 202, 256, 333, 333, 403, 404]
print peptide, sorted(mass_spectrum_cyclic(peptide))
print sorted(set(spectrum))
print sorted(set(mass_spectrum_cyclic(peptide)) & set(spectrum))
print score_cyclic(peptide, spectrum)

print '-' * 80
peptide = 'PEEP'
spectrum = [0, 97, 97, 97, 100, 129, 194, 226, 226, 226, 258, 323, 323, 355, 393, 452]
print peptide, sorted(mass_spectrum_cyclic(peptide))
print sorted(spectrum)
print sorted(set(mass_spectrum_cyclic(peptide)) & set(spectrum))
print score_cyclic(peptide, spectrum)

