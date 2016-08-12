2016/8/12 
疑问和以后处理点：
. 前处理的phrase detection怎么处理，并没有找到phrase检测和合并的文件，日语或者英语，请求检查

Procedures for preprocessing
1. For English:
	preclean1.py
		IN:
			"en_jp_text_2014_64079.csv"
		OUT:
			output1 "removed_en.csv" 
			output2 "removed_jp.csv"
	preclean2-EN.py
		IN:
			'removed_en.csv'
		OUT:
			'removed2_en.csv'
	tagging_nltk-EN.py
		IN:
			"removed2_en.csv"
		OUT: 
			"tag_nltk_en.csv"
	clean_tag-EN.py (No JP version)
		IN:
			"tag_nltk_en.csv"
		OUT:
			"cleaned_tag_en.txt"
	clean2_tag-EN.py
		IN:
			"cleaned_tag_en.txt"
		OUT:
			"cleaned2_tag_en.txt"

2. For Japanese:
	preclean1.py
		IN:
			"en_jp_text_2014_64079.csv"
		OUT:
			output1 "removed_en.csv" 
			output2 "removed_jp.csv"
	preclean2-JP.py
		IN:
			'removed_jp.csv'
		OUT:
			'removed2_jp.csv'
	tagging_mecab-JP.py
		IN:
		OUT:
	clean2_tag-JP.py
		IN:
		OUT:

