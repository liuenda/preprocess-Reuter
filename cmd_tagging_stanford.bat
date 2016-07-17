cd C:/Users/liuenda-toshiba/Dropbox/Research/Tools/StandfordNLP/stanford-postagger-2015-12-09/stanford-postagger-2015-12-09

java -cp "*;lib/*" edu.stanford.nlp.tagger.maxent.MaxentTagger -model models/english-left3words-distsim.tagger -textFile "../../../../2016.5.11~Reuter/removed2_en.csv" -outputFile "../../../../2016.5.11~Reuter/tagging_en.csv"