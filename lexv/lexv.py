f = open('rosalind_lexv.txt','r')
lines = f.readlines()
f.close()
Tletter_list = lines[0].split() #원본 letter list
num = int(lines[1].strip()) # 최대 길이
title = list('abcdefghijklmnopqrstuvwxyz')[:len(Tletter_list)]

temp_paste = list(title)
count = 1

while count != num:
    count += 1
    real_paste = list(temp_paste)
    for form_let in title: #1글자
        for temp_let in real_paste:
            temp_paste.append(temp_let+form_let)
temp_paste = list(set(temp_paste))
temp_paste.sort()

result = ''
for factor in temp_paste:
    result += factor+'\n'
for number in range(0,len(Tletter_list)):
    result = result.replace(title[number],Tletter_list[number])

sv = open('result.txt','w')
sv.write(result.rstrip())
sv.close()
