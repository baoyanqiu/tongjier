import csv
import re
file = 'C:/Users/dy/Desktop/access.log'
with open(file,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f) 
    file_ = 'C:/Users/dy/Desktop/haha.txt'
    asd = open(file_,'a',encoding='utf-8')
    for row in csv_reader: 
        q = re.findall(r"\"http(.+?)\"",row[0])
        if q !=[]:
            qwe = 'http{}/'.format(str(q))
            asd.write('\n'+qwe)
    asd.close()