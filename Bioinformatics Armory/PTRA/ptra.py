from Bio.Seq import translate

f = open('rosalind_ptra.txt','r')
lines = f. readlines()
DNAseq = lines[0].strip()
PRTseq = lines[1].strip()

for i in range(1,16):
    if PRTseq == translate(DNAseq,table=i,to_stop=True):
        result = str(i)
        break
    else:continue

print (result)
