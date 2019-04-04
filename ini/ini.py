f = open('rosalind_ini.txt','r')
seq = f.readline()
f.close()

Acount = seq.count('A')
Ccount = seq.count('C')
Gcount = seq.count('G')
Tcount = seq.count('T')

g = open('result.txt','w')
g.write(str(Acount)+' '+str(Ccount)+' '+str(Gcount)+' '+str(Tcount))
g.close()
