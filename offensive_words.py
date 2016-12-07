# -*- coding: utf-8 -*-
'''
Created on Dec 7, 2016

@author: andrey.justo
'''

import codecs
from nltk.stem.snowball import SnowballStemmer

class OffensiveWords():

    def __init__(self, language):
        self.stemmer = SnowballStemmer(language)
        self.lang_bad_words = set(self.stemmer.stem(w) for w in [line.strip() for line in codecs.open("./" + language + ".txt", 'r', "utf-8")])
        print(self.lang_bad_words)
        
    def badwords(self, words):
        
        for word in words:

            if self.stemmer.stem(word).lower() in self.lang_bad_words:
                yield word
                              
def main():            
    bad_words = list(OffensiveWords("portuguese").badwords("adoro esse programa, vai se FoDer".split(" ")))
    for w in bad_words:
        print(w)
    
    if len(bad_words) > 0:
        print("OFFENSIVE PHRASE")
        
main()
    