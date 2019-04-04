f = open('rosalind_fibd.txt','r')
line = f.readline()
f.close()

n = int(line.split()[0])
m = int(line.split()[1])

count = 1

history_list = [(1,0)]

while count < n:

    baby_rabbit = history_list[count-1][1]
    if count>=m:
        matr_rabbit = history_list[count-1][0] - history_list[count-m][0]
        print('yet')
    else:
        matr_rabbit = history_list[count-1][0]
        print('ok')
    history_list.append((baby_rabbit,matr_rabbit))
    count += 1
    print (history_list)
