f = open('rosalind_revp.txt','r')
lines = f.readlines()
f.close()
seq = ''

def revseq(a):
    ctseq = a[::-1]
    ctseq = ctseq.replace('A','t').replace('G','c').replace('C','g').replace('T','a').upper()
    return ctseq

for line in lines:
    if line[0] == '>':
        pass
    else:
        seq += line.strip()

result_list = []

present_index = 1

while seq:
    present_len = len(seq)
    for prelen in range(4,present_len+1):
        preseq = seq[0:prelen]
        if preseq == revseq(preseq):
            result_list.append(str(present_index)+' '+str(len(preseq)))
    seq = seq[1:]
    present_index += 1

result = ''

for line in result_list:
    result += line+'\n'

sv = open('result.txt','w')
sv.write(result)
sv.close()
