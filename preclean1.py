# coding:utf-8
import json
import re
import pandas as pd

# preclean S1: Remove lines from data frame from DataFrame basing on the keywords
# If there is a matched keywords, the whole row from DF will be removed
# The dataFrame include both Japanese and English Reuter News
# And the output will split those two languages text resources
# keyword：Operational Communications
# keyword：following data
# Keyword: following seasonally adjusted data
# Keyword: data on, data in, data for

# input input_data:"en_jp_text_2014_64079.csv"
# output1 "removed_en.csv" 
# output2 "removed_jp.csv"


import time
start_time = time.time()

input_data="en_jp_text_2014_64079.csv"

reg=[]
reg.append(r'following[^\\]+data for')
reg.append(r'following[^\\]+data on')
reg.append(r'following[^\\]+data in')
reg.append(r'operational communications')
reg.append(r'Overall PMI')
reg.append(r'follows: ')
reg.append(r'Traders report: ')

match=[]

# def removelines(input_filename, output_filename):
# 	output_file=open(output_filename,'w')
# 	with open(input_filename) as file_text:
# 		for index,line in enumerate(file_text):
# 			if index in match:
# 				newLine="\n"
# 			else:
# 				newLine=line
# 			output_file.write(newLine)
# 	output_file.close()
# 	return

def matchLines(line):
	for reg1 in reg:
		match_flag=re.search(reg1, line, re.IGNORECASE)
		if match_flag != None:
			return False
	return True

# def regExpListSub(line,reg):
# 	for reg1 in reg:
# 		match_flag=re.search(reg1, line, re.IGNORECASE)
# 		if match_flag != None:
# 			return False
# 	return newLine

df=pd.read_csv(input_data)
mask=df.en_text.map(matchLines)
df_removed=df.loc[mask]

# S2: Remove useless for Japanese and English text respectively
# reg_en_front=[]
# reg_en_front.append(r'[^"]*\(Reuters\) ')

#df_removed_en=df_removed.en_text.str.replace(r'[^"]*\(Reuters\)[ -]*','')
#df_removed_en=df_removed_en.str.replace(r'\([^\(^"]*Reporting.*(?=""")','')

#df_removed_en.to_csv('removed_en.csv',index=False )

df_removed.en_text.to_csv('removed_en.csv',index=False )
df_removed.jp_text.to_csv('removed_jp.csv' ,index=False)




# with open('en_text_2014_64079.csv') as file_text_en:
# 	for index,line in enumerate(file_text_en):
# 		for reg1 in reg:
# 			match_flag=re.search(reg1, line, re.IGNORECASE)
# 			if match_flag != None:
# 				match.append(index)
	
# print "the matched lines number: ", match
# print "removed line: ", len(match)

# removelines('en_text_2014_64079.csv','removed_en.txt')
# removelines('jp_text_2014_64079.csv','removed_jp.txt')



# output_en=open('removed_en.txt','w')
# output_en.close()

# output_jp=open('removed_jp.txt','w')
# with open('jp_text_2014_64079.csv') as file_text_jp:
# 	for index,line in enumerate(file_text_jp):
# 		if index in match:
# 			newLine_jp=""
# 		else:
# 			newLine_jp=line
# 		output_jp.write(newLine_jp)
# output_jp.close()

print("--- %s seconds ---" % (time.time() - start_time))
