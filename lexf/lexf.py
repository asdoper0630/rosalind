f = open('rosalind_lexf.txt','r')
lines = f.readlines()
letter_list = lines[0].strip().split()
num = int(lines[1].strip())
f.close()
count = 1
temp_list = letter_list
string_list = []

for a in range(0,num):
    for seed_string in temp_list:
        for letter in letter_list:
            if len(seed_string+letter) > num: break
            string_list.append(seed_string+letter)
    temp_list = string_list

result_list = []
for a in string_list:
    if len(a) == num:
        result_list.append(a)
        print(a)

result = ''

for b in result_list:
    result += b+'\n'

sv = open('result.txt','w')
sv.write(result)
sv.close()
