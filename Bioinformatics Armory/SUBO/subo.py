from Bio import SeqIO
from Bio import pairwise2

# f = open('rosalind_subo.txt','r')

seq_list = []
for seq_record in SeqIO.parse('rosalind_subo.txt','fasta'):
    seq_list.append(str(seq_record.seq))

align = pairwise2.align.localxx(seq_list[0],seq_list[1])

from Bio.pairwise2 import format_alignment
for a in align:
    print(format_alignment(*a))
