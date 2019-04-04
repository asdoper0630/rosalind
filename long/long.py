f = open('rosalind_long.txt','r')
lines = f.readlines()
f.close()
IDseq_list = []
temp_seq = ''
for line in lines:
    if line[0] == '>':
        if temp_seq:
            IDseq_list.append((ID,temp_seq))
            temp_seq = ''
        else : pass
        ID = line.strip()[1:]
    else:
        temp_seq += line.strip()
IDseq_list.append((ID,temp_seq))
seq_list = []
for IDseq in IDseq_list:
    seq_list.append(IDseq[1])

seq_list.sort()
print(seq_list)

# 여기까진 완성

while len(seq_list) > 1:
    seq1 = seq_list[0]
    for seq2 in seq_list[1:]
        for i in range(1,len(seq)):
            
