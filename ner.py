import nltk
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

# nltk.download()

st = StanfordNERTagger('/home/coderuth/syneHack/finalShow/stanford-ner/classifiers/ner-eng-ie.crf-3-all2008-distsim.ser.gz',
                       '/home/coderuth/syneHack/finalShow/stanford-ner/stanford-ner.jar',
                       encoding='utf-8')

text = 'While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.'

tokenized_text = word_tokenize(text)
classified_text = st.tag(tokenized_text)

print(classified_text)
