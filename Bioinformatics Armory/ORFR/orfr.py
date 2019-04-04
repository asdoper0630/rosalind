from Bio.Seq import Seq
with open('rosalind_orfr.txt','r') as f: line = f.readline().strip()
seq = Seq(line)
aa_1 = str(seq.translate())
aa_2 = str(seq[1:].translate())
aa_3 = str(seq[2:].translate())
aa_list = [aa_1,aa_2,aa_3]

recording_seq = ''
aa_seq_list = []
record = False
for aa in aa_list:
    each_AAseq = aa.split('*')
    for aaseq in each_AAseq:
        aa_seq_list.append(aaseq)

result_list = list(set(aa_seq_list))
for aa in aa_seq_list:
    if not aa.startswith('M'): result_list.remove(aa)
    else: pass

print (result_list)
