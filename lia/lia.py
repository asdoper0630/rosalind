import math

f = open('rosalind_lia.txt','r')
line = f.readline()
k = int(line.split()[0])
N = int(line.split()[1])
gs = [1]

count = 0

while count != pow(2,k):
    print (count)
    print (gs)
    gs_end = list(gs)
    gs_st = list(gs)
    gs.append(0)
    gs_end.append(0)
    gs_st.insert(0,0)
    for a in range(0,len(gs)):
        gs[a] = gs_end[a] + gs_st[a]
    count += 1

percent_list = []

for gs_num in gs:
    atari = pow(0.25,len(percent_list))
    hazure= pow(0.75,len(gs)-len(percent_list)-1)
    percent_list.append(atari*hazure*gs_num)

print (percent_list)
c = 0
for a in percent_list[N:]:
    c += a
print (c)
