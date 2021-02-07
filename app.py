# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from textblob import TextBlob
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np
import tensorflow as tf
physical_devices = tf.config.list_physical_devices('GPU') 
tf.config.experimental.set_memory_growth(physical_devices[0], True)

stop_words=set(stopwords.words('english'))
stop_words.remove('not')

app = Flask(__name__)

# Load the Bidirectional LSTM model and Tokenizer object from disk
model = load_model('model.h5')

with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

def cleantxt(text):
    text=re.sub('@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+',' ',text)
    text=text.lower()
    text = re.sub(re.compile('<.*?>'), '', text)
    text=text.split()
    text=[word for word in text if not word in stop_words]
    text=' '.join(text)
    text = WordNetLemmatizer().lemmatize(text)
    return text

def predict_text(text):
    #clean text
    text = cleantxt(text)
    # Tokenize text
    x_test = pad_sequences(tokenizer.texts_to_sequences([text]), maxlen=100)
    # Predict
    score = model.predict(x_test)
    if score>0.5:
        return [(1.0-float(score))*100,float(score)*100]
    else:
        return [(1.0-float(score))*100,float(score)*100]

# Create a function to get the subjectivity
def getSubjectivity(text):
   return TextBlob(text).sentiment.subjectivity

# Create a function to get the polarity
def getPolarity(text):
   return  TextBlob(text).sentiment.polarity

# Create a function to compute negative (-1), neutral (0) and positive (+1) analysis
def getAnalysis(score):
    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.form['text']
        print(text)
        prediction = predict_text(text)
        bar_labels=['Not Sarcasm','Sarcasm']
        bar_values=[prediction[0],prediction[1]]
        sub = getSubjectivity(text)
        pol = getPolarity(text)
        sentiment = getAnalysis(pol)
        print(bar_values)
        return render_template('index.html',labels=bar_labels, values=bar_values,text=text,sub=sub,pol=pol,sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)
