# coding:utf-8
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

# Alternative way of tagging a sentence! too slow!
from nltk import *
import nltk
import time
from nltk.tag.perceptron import PerceptronTagger
start_time = time.time()

# input_filename="removed2_en.csv"
input_filename="sample_removed2_en.csv"
output_filename="sample_tag_nltk_en.csv"
output=open(output_filename,'w')

# WAY-1 200s/1000
# with open(input_filename) as data_file:
# 	for (index,line) in enumerate(data_file):
# 		line=line.decode('utf-8','ignore') # you have to decode the line using the corresponded coding!
# 		sents = nltk.sent_tokenize(line)
# 		nltk.pos_tag_sents(sents) # WRONG!!!!
# 		print index

# WAY-2: Faster  20s/1000
tagger = PerceptronTagger() 
with open(input_filename) as data_file:
	for (index,line) in enumerate(data_file):
		line=line.decode('utf-8','ignore') # you have to decode the line using the corresponded coding!
		# sents = nltk.sent_tokenize(line)
		# print sents
		# sentences_pos=tagger.tag_sents(sents)
		word_list=nltk.word_tokenize(line)
		line_tagged=tagger.tag(word_list)
		if index in range(5000,60001,5000):
			print index
		# print line_tagged
		for t in line_tagged:
			output.write('_'.join(t)+' ')
		output.write('\n')


# # WAY-3: More precise but slower  21s/1000
# tagger = PerceptronTagger() 
# with open(input_filename) as data_file:
# 	for (index,line) in enumerate(data_file):
# 		line=line.decode('utf-8','ignore') # you have to decode the line using the corresponded coding!
# 		sents = nltk.sent_tokenize(line)
# 		tokenized_sents = [nltk.word_tokenize(i) for i in sents]
# 		sents_tagged=tagger.tag_sents(tokenized_sents)
# 		if index in range(5000,60001,5000):
# 			print index
# 		for l in sents_tagged:
# 				for t in l:
# 					output.write('_'.join(t)+' ')
# 		output.write('\n')

output.close()
print("--- %s seconds ---" % (time.time() - start_time))