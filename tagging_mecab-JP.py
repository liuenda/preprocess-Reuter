# coding:utf-8
import re
import pprint
import sys  
import time
import MeCab
start_time = time.time()
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

import nltk
from nltk.corpus.reader import *
from nltk.corpus.reader.util import *
from nltk.text import Text

# # Sample:
# input_filename=r'sample_removed2_jp.csv'
# output_filename1=r'sample_tag_mecab_jp.txt'
# output_filename2=r'sample_cleaned_tag_jp.txt'

# Real:
input_filename=r'removed2_jp.csv'
output_filename1=r'tag_mecab_jp.txt'
output_filename2=r'cleaned_tag_jp.txt'

output1=open(output_filename1,'w')
output2=open(output_filename2,'w')

tagger = MeCab.Tagger("-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/")


with open(input_filename) as data_file:
	for (index,line) in enumerate(data_file):
		#line=line.encode('utf-8','ignore')  # NO NEED!
		node = tagger.parseToNode(line)
		#index=0
		line_tagged=[]
		newLine=[]
		while node:
			word_tagged=(node.surface,node.feature)
			line_tagged.append(word_tagged)
			list_feature=node.feature.split(',')
			if '動詞' in list_feature[0] or '名詞' in list_feature[0] or '接頭詞' in list_feature[0]:
				if '数' not in list_feature[1] and '接尾' not in list_feature[1]:
					if '*' not in list_feature[6]:
						newLine.append(list_feature[6])
			# if index==999:
			# 	print list_feature[0]
			node=node.next

		output2.write(' '.join(newLine)+'\n')
		
		if index in range(5000,60001,5000):
			# print mecab_result+'\n\n'
			print index

		# output1.write('\n'.join('_'.join(t) for t in line_tagged))
		# output1.write('\n\n\n')

		# if index==999:
		# 	print '\n'.join('_'.join(t) for t in line_tagged)
		# # print index

output1.close()
output2.close()

# mecab = MeCab.Tagger('-Ochasen')
# sent = u"かれのくるまでまつ".encode('utf-8')
# node = mecab.parseToNode(sent)
# node = node.next
# while node:
# 	print node.surface, node.feature
# 	node = node.next

# reader = PlaintextCorpusReader("./", input_filename,
#                                 encoding='utf-8',
#                                 para_block_reader=read_line_block,
#                                 sent_tokenizer=jp_sent_tokenizer,
#                                 word_tokenizer=jptokenizer.JPMeCabTokenizer())
# print ' '.join(reader.words()[20:80])

print("--- %s seconds ---" % (time.time() - start_time))