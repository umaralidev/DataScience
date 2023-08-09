# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 12:47:27 2023

@author: Umar Ali
"""

#Read The Data
import pandas as pd

df = pd.read_csv('SMSSpamCollection', sep='\t',names=['label', 'message'])

#Data Cleaning

import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


WordNet = WordNetLemmatizer()
corpus = []

for i in range(len(df)):
    review = re.sub('[^a-zA-Z]',' ',df['message'][i])
    review = review.lower()
    review = review.split()
    
    review = [WordNet.lemmatize(word) for word in review if word not in stopwords.words('english')]
    review = ' '.join(review)
    corpus.append(review)
    
    

#Apply BagofWords Model -- Independent Variables

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000)
X = cv.fit_transform(corpus).toarray()


#Get Dependent Variables

y = pd.get_dummies(df['label'])
y = y.iloc[:,1].values


# Train Test and Split the data

from sklearn.model_selection import train_test_split
X_train, X_test, y_train,y_test = train_test_split(X,y, test_size=0.3, random_state=0)


# Training Model Using Naive Bayes Classifier
from sklearn.naive_bayes import MultinomialNB
spam_detect_model = MultinomialNB().fit(X_train, y_train)

y_pred = spam_detect_model.predict(X_test)


#Comparing Prediction and Test Data -- Confusion Matrix

from sklearn.metrics import confusion_matrix

Confustion_M = confusion_matrix(y_test, y_pred)


# Check the Accuracy

from sklearn.metrics import accuracy_score
Accuracy = accuracy_score(y_test, y_pred)



