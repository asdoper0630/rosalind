from Bio.Seq import Seq
from Bio import SeqIO

count = 0
for seq_record in SeqIO.parse('rosalind_rvco.txt','fasta'):
    if seq_record.seq == seq_record.seq.reverse_complement():
        count += 1
    else: pass

print (count)
