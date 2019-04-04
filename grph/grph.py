def presuf_list(ISlist):
    result_list = []
    for i in ISlist:
        for j in ISlist:
            if i[1][-3:] == j[1][:3]:
                if i!=j: result_list.append(i[0]+' '+j[0])
                else: pass
    return result_list

f = open('rosalind_grph.txt','r')
lines = f.readlines()
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

result = ''
for IDs in presuf_list(IDseq_list):
    result += IDs.strip()+'\n'

sv = open('result.txt','w')
sv.write(result.rstrip())
sv.close()
