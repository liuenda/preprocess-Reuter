# coding:utf-8
import re
import sys
import time
start_time = time.time()
import pandas as pd

# running time on linux-liuenda: 32s
# preclean S2: Remove the matched partition from lines basing on the regular expression
# only for English
# input input_filename='removed_en.csv'
# output output_filename='removed2_en.csv'

input_filename='removed_en.csv'
output_filename='removed2_en.csv'


# output=open('sample_removed2_en.csv','w')
output=open(output_filename,'w')
reg=[]
#reg.append(r'[^"]*\([rR]euters\)[ -]*')
reg.append(r'^.*\([rR][eE][uU][tT][eE][rR][sS]\)[ -]*')
reg.append(r'\([^\(^"]*[rR]eporting.*')
#reg.append(r'\(.[^\[^"]*Editing by.*') 
reg.append(r'\([Ee]diting [BbDd][yYeE].*') # remove 1st
reg.append(r'\(.[^\[^"]*[Ee]diting [BbDd][yYeE].*') # remove 2nd  both 2 reg is needed!
reg.append(r'\([Cc]ompil.*') # remove compiled by
reg.append(r'\\n[ ]*') # \n
reg.append(r'\[.*?\]') #[ID:nL2N0KC0D9]
reg.append(r'<.*?>') # <005380.KS> version-1
#reg.append(r'<\^.*\^>') # remove <-xxxxx-> version-2
reg.append(r'http://[^"^\n]*')
reg.append(r'[^.]*click[^\n]*') #remove table
#reg.append(r'http://[^(^"]*')
#reg.append(r'\([^\(^"]*reporting.*(?=")')
#reg.append(r'[^"]*Keywords.*') #这个特别花时间，不知为何 this line cost a least 5s, why?
reg.append(r'[^ ]*@[^ ^\n]+')
reg.append(r'\(*Keywords.*')
reg.append(r'\([^(]*\+.*?\)') #This cleaining order should not be changed


# with open('sample_removed_en.csv') as data_file:
with open(input_filename) as data_file:
	for (index,line) in enumerate(data_file):
		newLine=line
		for reg1 in reg:
			#print "reg1=",reg1
			newLine=re.sub(reg1,'',newLine)
			#print newLine
		if '\n' not in newLine:
			print index,"Warning: This line has no \\n!"   # this is very important!
		#newLine+="endofblock\n"
		output.write(newLine)

output.close()

# Alternative method but not fully verified yet!
# df=pd.read_csv("sample_removed_en.csv",header=None,names=["en_text"])
# df_removed_en=df.en_text.str.replace(r'\([^\(^"]*Reporting.*','')
# df_removed_en=df.en_text.str.replace(r'\([^\(^"]*reporting.*','')
# df_removed_en.to_csv('sample_removed2_en.csv',index=False )

print("--- %s seconds ---" % (time.time() - start_time))