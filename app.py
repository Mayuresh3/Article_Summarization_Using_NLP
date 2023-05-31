st.title('Article_Summarization_Using_NLP')

!pip install textblob==0.9.0
!pip install nltk
!pip install newspaper3k

import streamlit as st
import tkinter as tk
import nltk 
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt') #model that we can use for nlp

url = st.text_input('Give URL :')

article = Article(url)

article.download() #download the url data

article.parse() #parse the data the parse dissect the article that is need

article.nlp() #using natural language processing it does everything for you

st.header('Summary')
st.write(article.summary)
