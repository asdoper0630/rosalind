# Finding a Spliced Motif

f       = open('rosalind_sseq.txt','r')
lines   = f.readlines()

csdic   = {}
seq     = ''
seq_list= []
for line in lines:
    if line[0] == '>':
        if seq:
            csdic[id] = seq
            seq_list.append(seq)
            seq = ''
        else: pass
        id  = line[1:].strip()
    else:
        seq += line.strip()
csdic[id] = seq
seq_list.append(seq)

s   = seq_list[0]
t   = seq_list[1]
temp_nlist  = []
pref        = 0


while t:
    loc = s.find(t[0])
    if loc == -1:
        break
    temp_nlist.append(loc+pref+1)
    s = s[loc+1:]
    t = t[1:]

    pref += loc+1

sv = open('result.txt','w')
sv.write(str(temp_nlist)[1:-1].replace(',',''))
sv.close()
