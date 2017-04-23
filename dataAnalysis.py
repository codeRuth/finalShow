import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1
from keywordr import keywordr as k
from textblob import TextBlob

import csv
import sys

speech_to_text = SpeechToTextV1(
    username='298642e9-d4e8-4505-96f6-da9f8e25f2fc',
    password='AOA0YiqZZxbi',
    x_watson_learning_opt_out=False
)

def speechAnalysis(filename):
    text 
    for i in range(1, 16):
        with open(join(dirname(__file__), filename+''), 'rb') as audio_file:
            obj = json.loads(json.dumps(speech_to_text.recognize(
                audio_file, content_type='audio/wav', timestamps=True,
                word_confidence=True),
                indent=2))
            text = obj['results'][0]['alternatives'][0]['transcript']
            textKey = k.get_keywords(obj['results'][0]['alternatives'][0]['transcript'])
            analysis = TextBlob(text)
    return {'text': text, 'keyword': textKey, 'sentiment': analysis.sentiment}

def tweetAnalysis(filename):
    f = open(filename, 'rb')

    rowData = list()
    data = list()

    reader = csv.reader(f)
    for row in reader:
        rowData.append(row)

    for r in rowData:
        try:
            textKey = k.get_keywords(r[0])
            analysis = TextBlob(r[0])
            data.append({'text': r[0], 'keyword': textKey, 'sentiment': analysis.sentiment})
        except UnicodeDecodeError:
            print "cant decode"
    f.close()
    return data
#
# if __name__ == '__main__':
#
#         print speechAnalysis('speechData/floyd.wav')
#         print tweetAnalysis('tweetData/tweet2.csv')
