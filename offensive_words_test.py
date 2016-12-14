'''
Created on Dec 13, 2016

@author: andrey.justo
'''

import time
from offensive_words import OffensiveWords

def main():      
    offensive_words = OffensiveWords("portuguese")   
    offensive_text = "Mas afinal o que é um filho da puta? Não obstante a frequência com que o termo é empregue na classificação axiomática de reconhecidos sociopatas como banqueiros, especuladores financeiros e ministros, não existe ainda consenso bastante para alcançar uma definição acabada. Longe de pretender ser tratado sobre o tema, este artigo é um subsídio para uma definição mínima. Caso o leitor responda afirmativamente a, pelo menos, cinco questões, então é provável que seja um filho da puta."
    offensive_text2 = "Oi, tudo bem? Seu filho da puta"  
    not_offensive_text = "Mas afinal o que estamos fazendo aqui?."
    not_offensive_text2 = "Oi, tudo bem?"
    not_offensive_text3 = "Negro na universidade."
    offensive_text4 = "Negrinho, fedido"
       

    texts_to_classify = [offensive_text, not_offensive_text, not_offensive_text2, offensive_text2, not_offensive_text3, offensive_text4]
    classifications = offensive_words.classify(texts_to_classify)   
    print(list(classifications))

    bad_words = list(offensive_words.badwords(offensive_text))
                      
    for w in bad_words:
        print(w)
     
    if len(bad_words) > 0:
        print("OFFENSIVE PHRASE")    
        
start = time.time()
main()
print()
end = time.time()
print(end - start)