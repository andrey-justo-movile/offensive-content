# -*- coding: utf-8 -*-
'''
Created on Dec 7, 2016

@author: andrey.justo
'''

import codecs
import time
import re

class OffensiveWords():

    def __init__(self, language):
        self.lang_bad_words = set(w for w in [line.strip() for line in codecs.open("./" + language + ".txt", 'r', "utf-8")])
        self.delimiter_regex = ' |\\.|\\?|\\!|,|;'
        
    def badwords(self, words):
        # we should split by any other characters
        for word in re.split(self.delimiter_regex, words):
            if word in self.lang_bad_words:
                yield word
                              
def main():            
    bad_words = list(OffensiveWords("portuguese").badwords("Mas afinal o que é um filho da puta? Não obstante a frequência com que o termo é empregue na classificação axiomática de reconhecidos sociopatas como banqueiros, especuladores financeiros e ministros, não existe ainda consenso bastante para alcançar uma definição acabada. Longe de pretender ser tratado sobre o tema, este artigo é um subsídio para uma definição mínima. Caso o leitor responda afirmativamente a, pelo menos, cinco questões, então é provável que seja um filho da puta."))
                     
    for w in bad_words:
        print(w)
    
    if len(bad_words) > 0:
        print("OFFENSIVE PHRASE")
        
start = time.time()
main()
print()
end = time.time()
print(end - start)