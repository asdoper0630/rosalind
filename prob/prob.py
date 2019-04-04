import math
f = open('rosalind_prob.txt','r')
lines = f.readlines()
f.close()

seq = lines[0].strip()
prob_list = lines[1].strip().split()
ATcount = seq.count('A') + seq.count('T')
GCcount = seq.count('G') + seq.count('C')
result = ''
for prob in prob_list:
    GCprob = float(prob)/2
    ATprob = 0.5-GCprob
    logprob = math.log10((GCprob**GCcount)*(ATprob**ATcount))
    result += str("{0:.3f}".format(logprob))+' '

sv = open('result.txt','w')
sv.write(result.strip())
sv.close()
