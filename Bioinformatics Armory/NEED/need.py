def MtoD(lines):
    main_dic = {}
    for line in lines:
        if line[0] == '\t': # 첫 라인일때
            row = line.split()
        else:
            column = line.split()
            for AA in row:
                for i in range(len(row)):
                    main_dic[(column[0]),row[i]] = int(column[i+1])
    return main_dic

from Bio import Entrez
Entrez.email = 'asdoper0630@naver.com'
from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.SubsMat import MatrixInfo as matlist

f= open('rosalind_need.txt','r')
GBID = f.readline().strip().split()
f.close()

matrix = open('matrix.txt','r')
linesM = matrix.readlines()
matrix_DNAfull = MtoD(linesM)

handle = Entrez.efetch(db='nucleotide',id=GBID,rettype = 'fasta')
records = handle.read()
g = open('need.fasta','w')
g.write(records)
g.close()

seq_list = []
for seq_record in SeqIO.parse('need.fasta','fasta'):
    seq_list.append(str(seq_record.seq))
align = pairwise2.align.globalds(seq_list[0],seq_list[1],matrix_DNAfull,-10,-1)

sv = open('result.txt','w')
sv.write(format_alignment(*align[0]))
sv.close()
