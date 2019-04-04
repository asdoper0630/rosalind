import random
import time

st = time.time()

f = open('rosalind_perm.txt','r')
num = int(f.readline())
f.close()

perm_list = []

total_n = 1

for n in range(1,num+1):
    perm_list.append(n)
    total_n *= n

total = []
while len(total) != total_n:
    random.shuffle(perm_list)
    total.append(str(perm_list)[1:-1])
    total = list(set(total))
    total.sort()


result = str(len(total))+'\n'
for a in total:
    b = a.replace(',','')
    result += b+'\n'

sv = open('result.txt','w')
sv.write(result.rstrip())
sv.close()

end = time.time()
print('걸린시간 : '+str(end-st))
