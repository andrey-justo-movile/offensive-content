# -*- coding: utf-8 -*-
'''
Created on Dec 7, 2016

@author: andrey.justo

Here we are using NLP to count all bad words from text
Also we use OneClassSVM to classify if the text belongs to the offensive phrase categorization or not. 

You can see more about this classifier in http://scikit-learn.org/stable/auto_examples/svm/plot_oneclass.html

'''

import codecs
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import OneClassSVM


class OffensiveWords():

    def __init__(self, language):
        self.lang_bad_words = set(w for w in [line.strip() for line in codecs.open("./" + language + ".txt", 'r', "utf-8")])
        self.delimiter_regex = ' |\\.|\\?|\\!|,|;'
        
        # init classifier algorithm
        self.load_data(language)
        
        
    def load_data(self, language):
        self.vectorizer = CountVectorizer()
        words = list(self.lang_bad_words)
        counts = self.vectorizer.fit_transform(words)
        targets = ['bad_words', 'not_bad_words']

        self.classifier = OneVsRestClassifier(OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1))
        self.classifier.fit(counts, targets)
        
    def badwords(self, words):
        # we should split by any other characters
        for word in re.split(self.delimiter_regex, words):
            if word.lower() in self.lang_bad_words:
                yield word
                
    def classify(self, text):
        counts = self.vectorizer.transform(text)
        yield self.classifier.predict(counts)
