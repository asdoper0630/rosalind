f = open('rosalind_dbpr.txt','r')
ID = f.readline().strip()

from urllib.request import urlopen

URL = urlopen('http://www.uniprot.org/uniprot/'+ID+'.txt')

result = ''

for a in URL.readlines():
    decode_line_list = a.decode("utf-8").strip().split(';')
    try:
        if decode_line_list[0] == 'DR   GO' and decode_line_list[2][1] == 'P':
            result += decode_line_list[2][3:] + '\n'
        else: pass
    except: pass

sv = open('result.txt','w')
sv.write(result)
sv.close()
