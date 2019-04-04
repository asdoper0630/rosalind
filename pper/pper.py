# partial permutations

f   = open('rosalind_pper.txt','r')
num = f.readline()
n   = int(num.split()[0])
k   = int(num.split()[1])

nlist   = list(range(n-k+1,n+1)[::-1])
result  = 1
for a in nlist: result *= a
result_str = str(result)[-6:]

sv = open('result.txt','w')
sv.write(str(int(result_str)))
sv.close()
