# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 15:22:22 2023

@author: Umar Ali
"""

#Import Libraries
import nltk
import re

from nltk.corpus import stopwords

#Data
paragraph = "I know there are people who do not quite agree with the division of Indian and the partition of the Punjab and Bengal. Much has been said against it, but now that it has been accepted, it is the duty of every one of us to loyally abide by it and honourably act according to the agreement which is now final and binding on all. But you must remember, as I have said, that this mighty revolution that has taken place is unprecedented. One can quite understand the feeling that exists between the two communities wherever one community is in majority and the other is in minority. But the question is whether it was possible or practicable to act otherwise than has been done. A division had to take place. On both sides, in Hindustan and Pakistan, there are sections of people who may not agree with it, who may not like it, but in my judgment there was no other solution and I am sure future history will record its verdict in favour of it. And what is more it will be proved by actual experience as we go on that that was the only solution of India’s constitutional problem. Any idea of a United India could never have worked and in my judgment it would have led us to terrific disaster. May be that view is correct; may be it is not; that remains to be seen. All the same, in this division it was impossible to avoid the questions of minorities being in one Dominion or the other. Now that was unavoidable. There is no other solution. Now what shall we do? Now, if we want to make this great State of Pakistan happy and prosperous we should wholly and solely concentrate on the well-being of the people, and especially of the masses and the poor. If you will work in co-operation, forgetting the past, burying the hatchet, you are bound to succeed. If you change your past and work together in a spirit that every one of you, no matter to what community he belongs, no matter to what community he belongs, no matter what relations he had with you in the past, no matter what is his colour, caste or creed, is first, second and last a citizen of this State with equal rights, privileges and obligations there will be no end to the progress you will make."


#Preprocessing the data

text = re.sub(r'\[[0-9]*\]',' ',paragraph)
text = re.sub(r'\s+',' ',text)
text = text.lower()
text = re.sub(r'\d',' ',text)
text = re.sub(r'\s+',' ',text)

#Preparing the data

sentences = nltk.sent_tokenize(text)

words = [nltk.word_tokenize(sentence) for sentence in sentences]

for i in range(len(words)):
    sentences[i] = [word for word in words[i] if word not in stopwords.words('english')]
    

#Training the Word2Vec Model

from gensim.models import Word2Vec
model = Word2Vec(sentences, min_count=1)


vector = model.wv['judgment']

#Similar words

similar = model.wv.most_similar('judgment')








