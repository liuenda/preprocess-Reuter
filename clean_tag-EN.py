# coding:utf-8
import re
import pprint
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.corpus.reader.wordnet import WordNetError
import sys  
import time
start_time = time.time()

#16/1/28 ADD ascii error coding, change coding to UTF-8
reload(sys)  
sys.setdefaultencoding('utf8')
wnl = WordNetLemmatizer()

# Sample File:
input_filename="sample_tag_nltk_en(pos_sents DEMO).csv"
outpu_filename="sample_cleaned_tag_en.txt"
outpu_filename2="sample_for_phraseDetect_en.txt"

# Real File:
input_filename="tag_nltk_en.csv"
outpu_filename="cleaned_tag_en.txt"
outpu_filename2="for_phraseDetect_en.txt"

reg=[]
#the reference http://www.comp.leeds.ac.uk/amalgam/tagsets/upenn.html
reg.append(r'[^ ]+_CD') #mid-1890 nine-thirty forty-two one-tenth ten million 0.5
reg.append(r'[^ ]+_DT') #all an another any both del each either every half la many
reg.append(r'[^ ]+_EX') #there
reg.append(r'[^ ]+_CC') #& 'n and both but either et for less minus neither nor or plus so 
reg.append(r'[^ ]+_IN') #astride among uppon whether out inside pro despite on by throughou
# reg.append(r'[^ ]+_LS') #A A. B B. C C. D E F First G H I J K One SP-44001 SP-44002 SP-44005 SP-44007 Second Third Three Two
# reg.append(r'[^ ]+_MD') #can cannot could couldn't dare may might must need ought shall 
# reg.append(r'[^ ]+_PDT') #all both half many quite such sure this
# reg.append(r'[^ ]+_PRP') #hers herself him himself hisself 
# reg.append(r'[^ ]+_PRP\$') #her his mine my our ours their thy your
reg.append(r'[^ ]+_SYM') #% & ' '' ''. ) ). * + ,. < = > @ A[fj] U.S U.S.S.R \* \*\* \*\*\*
reg.append(r'[^ ]+_RP') #aboard about across along apart around aside at away back before 
reg.append(r'[^ ]+_TO') #to
# reg.append(r'[^ ]+_UH') #Goodbye Goody Gosh Wow Jeepers Jee-sus Hubba Hey Kee-reist 
# reg.append(r'[^ ]+_WDT') #that what whatever which whichever
# reg.append(r'[^ ]+_WP') #that what whatever whatsoever which who whom whosoever
# reg.append(r'[^ ]+_WP\$') #whose
# reg.append(r'[^ ]+_WRB') #how however whence whenever where whereby whereever wherein whereof why
# reg.append(r'[^ ]+_FW') #Foreign words , here i_FW will be deleted

# Punctuations:
# reg.append(r'[^ ]+_\.') # ?_.
# reg.append(r'#') # #
# reg.append(r'[^ ]+_``') # ``
# reg.append(r'\'\'_\'\'')  # ""
# reg.append(r'[^ ]+_\$') # $
# reg.append(r'[^ ]+_\(') # (
# reg.append(r'[^ ]+_\)') # )
# reg.append(r'[^ ]+_,') # ,
# reg.append(r'[^ ]+_--') # --
# reg.append(r'[^ ]+_\.') # .
# reg.append(r'[^ ]+_--') # --
# reg.append(r'[^ ]+_:') # :
# 2016/6/27
# Omitted by phrase detectio function and will be added in the end
# reg.append(r'[^ \n]+_[^A-Za-z \n]+')
# reg.append(r'[^ ]*[^A-Za-z.]_[Nn][^ \n]+') #*_NN  %_NN -14_NN

#reg.append(r'_[^ \n]+')

# reg.append(r'[^ ]*@[^ ]+')  # remove xxxx@xxxx OR @xxxx component
# reg.append(r'!')
# reg.append(r'%_NN')
# #reg.append(r'[^ ]+-_-[^ ]+') # remove xxxx-_-xxxx mark
# reg.append(r'\bRT+_[^ ]*') #remove RT_NN RTRT_NN 
# reg.append(r'&..;[^ ]+') # &39;_Vxx
# reg.append(r'[^ ]+\.[com]+[^ ]*') #eg： www.trade.
# reg.append(r'[ ]._JJ*[^ ]') # <_JJR  =_JJ
# x=1

#pprint(reg)
output=open(outpu_filename,'w')
output2=open(outpu_filename2,'w')

with open(input_filename) as data_file:
	for (index,line) in enumerate(data_file):

		if index in range(5000,60001,5000):
			print "Now start the line No.:"+str(index)
			print("--- %s seconds ---" % (time.time() - start_time))

		#newData=line
		#This must be run 1st! The order should not be changed!
		for reg1 in reg:
			line=re.sub(reg1,'',line)

		#start to remove un-tagged word and rebind them
		#Nomalize(change to lowercase) is necessary for the following processing
		wordList=line.lower().split()

		# #TOO complicated, NEED modification to switc case type
		# #Here the change of string to lower cases are necessary!
		# newList=[word for word in wordList 
		# if '-_-' not in word and '~' not in word 
		# and '<' not in word and '_' in word and ':-'not in word]
		# delList=[word for word in wordList 
		# if not ('-_-' not in word and '~' not in word 
		# and '<' not in word and '_' in word and ':-' not in word)]

		#print "remove word includes:",delList

		#16/1/20 Add: Normalize the ADJ and ADV
		finalList=[]
		for i,w in enumerate(wordList):
			# ADD 16/1/26 Transform ADV to ADJ
			# ADD 16/1/28 ('_JJ' in w) to resovle words like "only_JJ"
			#if ('_RB' in w) or ('_JJ' in w):
			if ('_rb' in w):
				advset=w[:w.find('_')]+".r.1"
				try:
					adj=wn.synset(advset).lemmas()[0].pertainyms()[0].name()
					w=w.replace(w,adj+'_jjr')
				except (IndexError,WordNetError):
					w=w.replace(w,w[:w.find('_')]+'_jjr')
			

			if ('_jjr' in w) or ('_jjs' in w):
				# newADJ=wnl.lemmatize(w[:-4], 'a')
				newADJ=wnl.lemmatize(w[:w.find('_')], 'a')
				w=w.replace(w,newADJ+'_jj')
				#print "JJR replacement,the NewList:",w,"To",newADJ

			# HERE the ('_nn' in w) is to remedy the ERROR of Tagging('weaker_NN')
			if  '_nn' in w:
				old=w[:w.find('_')]
				newADJ=wnl.lemmatize(w[:w.find('_')], 'a')
				w=w.replace(w,newADJ+'_nn')
				if old!=newADJ:
					print "NN--ADJ error: "+old+" "+newADJ

			# CODE:W1
			# Here is a big hazard, since _p can refer to '_pos'!!which will also be converted to nn!!
			# PDT Predeterminer POS Possessive ending PRP Personal pronoun PRP$ Possessive pronoun
			# convert 'its' to 'it'
			if ('_nn' in w or '_pr' in w):
				newNoun=wnl.lemmatize(w[:w.find('_')], 'n')
				w=w.replace(w,newNoun+'_nn')

			if ('_v' in w):
				newNoun=wnl.lemmatize(w[:w.find('_')], 'v')
				w=w.replace(w,newNoun+'_vb')


			# # change endofblock notation into a return
			# if  "endofblock" in w:
			# 	w=w.replace(w,'\n')
			# else:
			# 	# ADD 2016/1/27 debug: line 7: happy_jj new_nnp year_nntime_nnp
			# 	w=w.replace(w,w+' ')

			#w=re.sub(r'_[^ \n]+','',w)
			# for reg1 in reg:
			# 	w=re.sub(reg1,'',w)

			finalList.append(w)

		#print "finished the line",index+1

		# Re-combine into a string and remove all the POS-tags
		newLine=" ".join(finalList)+'\n'

		# Output for normal tagging
		newLine1=newLine
		# Remove punctuations and other symbols
		newLine1=re.sub(r'[^ \n]+_[^A-Za-z \n]+','',newLine1)
		# Remove unknown nouns xxx_nn
		newLine1=re.sub(r'[^ ]*[^A-Za-z.]_[Nn][^ \n]+','',newLine1) # Here is the reason that the ' are deleted!!! CODE:W1
		# Remove all the tagger notatation "_xxx"
		newLine1=re.sub(r'_[^ \n]+','',newLine1)
		# Reshape the string by removing continuous space
		newLine1=re.sub(r' [ ]+',' ',newLine1)
		output.write(newLine1)

		# Output for pharse detecetion
		newLine2=newLine
		# Replace punctuations and other symbols with enter
		newLine2=re.sub(r'[^ \n]+_[^A-Za-z \n]+','\n',newLine2)
		# Replace unknown nouns xxx_nn with enter
		newLine2=re.sub(r'[^ ]*[^A-Za-z.]_[Nn][^ \n]+','\n',newLine2)
		# Remove all the tagger notatation "_xxx"
		newLine2=re.sub(r'_[^ \n]+','',newLine2)
		# Reshape the string by removing continuous space
		newLine2=re.sub(r'[\n][\s]+','\n',newLine2)
		output2.write(newLine2)
	

output.close()
output2.close()
print("--- %s seconds ---" % (time.time() - start_time))