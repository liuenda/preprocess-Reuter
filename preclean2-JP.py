# coding:utf-8
import re
import sys
import time
start_time = time.time()
import pandas as pd

reload(sys)  
sys.setdefaultencoding('utf8')

# running time on linux-liuenda:
# preclean S2: Remove the matched partition from lines basing on the regular expression
# only for Japanese
# input input_filename='removed_jp.csv'
# output output_filename='removed2_jp.csv'

# input_filename='sample_removed_jp.csv'
# output_filename='sample_removed2_jp.csv'
input_filename='removed_jp.csv'
output_filename='removed2_jp.csv'


# output=open('sample_removed2_en.csv','w')
output=open(output_filename,'w')
reg=[]

# Is unicode expression need escape the backslash"\"?
reg.append(r'http://[^ \n]*') # http address
reg.append(u'※[^\n]*')  # ※※英文参照番号
reg.append(u'.*ロイター[］\]]') #［香港　６日　ロイター］
reg.append(r'\\n[ ]*') # \n
reg.append(u'詳細は以下[^\n＊]+')
reg.append(u'[0-9A-Za-z<>.()]+') #  <.FTSE> 21286.48

# with open('sample_removed_en.csv') as data_file:
with open(input_filename) as data_file:
	for (index,line) in enumerate(data_file):
		newLine=line.decode('utf-8','ignore')
		for reg1 in reg:
			#print "reg1=",reg1
			newLine=re.sub(reg1,'',newLine)
			#print newLine
		if '\n' not in newLine:
			print index,"Warning: This line has no \\n!"   # this is very important!
		#newLine+="endofblock\n"
		output.write(newLine)

		# Progross o Processing
		if index in range(5000,60001,5000):
			print index
			
output.close()
print("--- %s seconds ---" % (time.time() - start_time))