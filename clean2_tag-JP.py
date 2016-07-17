# coding:utf-8
import re
import pprint
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.corpus.reader.wordnet import WordNetError
import sys  
import time
start_time = time.time()

# NOTE: (2016.6.1)
# This is named as "clean2_tag-jp" in order for consistance with
# the text processing of English version. But in fact there is
# no tag-cleaning in this script instead it remove the "stopword"
# according to the stop-word lists defined here.

#ascii error coding, change coding to UTF-8
reload(sys)  
sys.setdefaultencoding('utf8')
wnl = WordNetLemmatizer()

# #Sample File:
# input_filename="sample_cleaned_tag_jp.txt"
# outpu_filename="sample_cleaned2_tag_jp.txt"

# Real File:
input_filename="cleaned_tag_jp.txt"
outpu_filename="cleaned2_tag_jp.txt"

reg=[]
reg.append(r'[ ]た[ ]*')   #When to use r'' When to use u''?
reg.append(r'[ ]ない[ ]*')
reg.append(r'[ ]だ[ ]*')

output=open(outpu_filename,'w')
with open(input_filename) as data_file:
	for (index,line) in enumerate(data_file):

		if index in range(5000,60001,5000):
			print "Now start the line No.:"+str(index)
			print("--- %s seconds ---" % (time.time() - start_time))

		#newData=line
		#This must be run 1st! The order should not be changed!
		for reg1 in reg:
			line=re.sub(reg1,' ',line)

		output.write(line)

output.close()
print("--- %s seconds ---" % (time.time() - start_time))