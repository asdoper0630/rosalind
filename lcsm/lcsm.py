def substr(str1):
    a = list(set((str1[i:j] for i in range(0,len(str1)) for j in range(i,len(str1)+1))))
    a.sort()
    return a

f = open('rosalind_lcsm.txt','r')
lines = f.readlines()
f.close()

seq_list = []
temseq = ''
while lines:
    if lines[0] == '>':
        try:
            if temseq == '' : raise
            seq_list.append(temseq)
            temseq = ''
        except: pass
    else:
        temseq += lines[0].strip()
        lines = lines[1:]
seq_list.append(temseq)
temseq = ''

temp_list = substr(seq_list[0])
seq_list = seq_list[1:]
for seq in seq_list:
    temp_list = set(temp_list).intersection(set(substr(seq)))

print(temp_list)
# print(max(set(substr('photographs')).intersection(set(substr('autograph')))))
