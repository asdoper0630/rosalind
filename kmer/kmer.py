f = open('rosalind_kmer.txt','r')
lines = f.readlines()[1:]
f.close()

seq = ''
for line in lines:
    seq += line.strip()

numseq = seq
dic_4mer = {}
count = 1

base_list = ['A','C','G','T']

for a in base_list:
    for b in base_list:
        for c in base_list:
            for d in base_list:
                dic_4mer[a+b+c+d] = 0

result = ''
while len(numseq) >=4:
    for Amer in dic_4mer:
        if numseq[0:4] == Amer:
            dic_4mer[Amer] += 1
    numseq = numseq[1:]
result_list = dic_4mer.values()
for num in result_list:
    result += str(num)+' '

sv = open('result.txt','w')
sv.write(result.rstrip())
sv.close()
