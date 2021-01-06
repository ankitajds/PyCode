params =  {"column" :''}
_helper.tablename='my new filename'

import pandas as pd
import re
from pandas import read_csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json
import _helper

def main():
    try:
        df = _helper.data()
        #clean html
        def cleanhtml(sent):
            clean = re.sub(r'<*?>', r' ', sent)
            return clean

        #clean punctuation
        def cleanpunc(word):
            cleanr = re.sub(r'[?|!|\'|"|#]', r' ', word)
            cleaned = re.sub(r'[)|(|\|/]', r' ', cleanr)
            return cleaned

        lst_of_sent = []
        str1 = ''
        final_str = []

        if params['column'] in df:
            for sent in df[params['column']].values:
                filtered_sent = []
                sent          = cleanhtml(sent)
                for word in sent.split():
                    for clean_words in cleanpunc(word).split():
                        if (clean_words.isalpha()):
                            filtered_sent.append(clean_words.lower())
                lst_of_sent.append(filtered_sent)
        else:
            print("Column does not exist ")

        for lst in lst_of_sent:
            str1 = ' '.join(lst)
            final_str.append(str1)

        df['clean_Text'] = final_str

        #Extract sentiment from text
        
        analyzer = SentimentIntensityAnalyzer()
        lst_of_sent = []
        for sentence in final_str:
            vs = analyzer.polarity_scores(sentence)
            for item in vs.items():
                for key in item:
                    if key == 'compound':
                        lst_of_sent.append(vs[key])
                    else:
                        pass

        df['compound'] = lst_of_sent
        _helper.status(fileid,2,'')
        return _helper.publishbot(df)
        
    except Exception as e:
      
        _helper.status(fileid,-2,e)
        
        
