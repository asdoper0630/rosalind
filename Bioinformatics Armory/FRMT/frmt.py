from Bio import Entrez
Entrez.email = 'asdoper0630@naver.com'
from Bio import SeqIO

f = open('rosalind_frmt.txt','r')
GBID = f.readline().strip().split()
f.close()

handle = Entrez.efetch(db='nucleotide',id=GBID,rettype = 'fasta')
records = handle.read()
g = open('result.txt','w')
g.write(records)
g.close()

lenseq = 99999999999

for seq_record in SeqIO.parse('result.txt','fasta'):
    # print(seq_record)
    if len(seq_record.seq)<lenseq:
        lenseq = len(seq_record.seq)
        idmin = str(seq_record.id)
    else: pass

sv = open('result1.txt','w')
sv.write(Entrez.efetch(db='nucleotide',id=idmin,rettype = 'fasta').read())
sv.close()
