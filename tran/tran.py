f = open('rosalind_tran.txt','r')

lines = f.readlines()
lineli = []

f.close()

for line in lines:
    if line[0] == '>':
        pass
    else:
        lineli.append(line.strip())

lenli = (len(lineli)/2)



a = lineli[:int(lenli)]
b = lineli[int(lenli):]

seq1 = ''
seq2 = ''

for x in a:
    seq1 += x.strip()
for y in b:
    seq2 += y.strip()


print(seq1)
print(seq2)

si = 0
ver= 0

while seq1:
    if seq1[0] == seq2[0]:
        pass
    else:
        if seq1[0] == 'A':
            if seq2[0] == 'G':
                si += 1
            else:
                ver += 1

        elif seq1[0] == 'G':
            if seq2[0] == 'A':
                si += 1
            else:
                ver += 1
                
        elif seq1[0] == 'C':
            if seq2[0] == 'T':
                si += 1
            else:
                ver += 1
                        
        elif seq1[0] == 'T':
            if seq2[0] == 'C':
                si += 1
            else:
                ver += 1

    seq1 = seq1[1:]
    seq2 = seq2[1:]

        
g = open('result.txt','w')
g.write(str(float(si)/float(ver)))
g.close()
