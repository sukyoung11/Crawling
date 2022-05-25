#csv파일에서 속보만 찾아서 가져오기
import csv
f=open('./covid19_articles.csv','r')
rdr=csv.reader(f)

a=0
for row in rdr:
   if '[속보]' in row[2]:
       print(row[2])
       a+=1

f.close()
print(f'속보기사개수: {a}')


