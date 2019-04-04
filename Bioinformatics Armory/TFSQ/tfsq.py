f = open('rosalind_tfsq.txt','r')
lines = f.readlines()
f.close()
result = ''
while lines:
    result += '>'+lines[0].strip()[1:]+'\n'
    seq = lines[1].strip()
    while seq:
        result += seq[:60]+'\n'
        seq = seq[60:]
    result += '\n'
    lines = lines[4:]

sv = open('result.txt','w')
sv.write(result)
sv.close()
