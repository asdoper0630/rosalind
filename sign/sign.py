f = open('rosalind_sign.txt','r')
line = f.readline()
num = int(line.strip())
f.close()

basic_num = []
result_list = []

for a in range(1,num+1):
    basic_num.append(a)

# basic num = ex : [1,2,3]

temp_num = basic_num

for a in range(1,num+1):
    # for seed_num in basic_num:
    #     for add_num in temp_num:
    #         if len(seed_string+letter) > num: break
    #         string_list.append(seed_string+letter)
