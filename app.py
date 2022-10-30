from flask import Flask,render_template,request
from flask_cors import CORS

import pandas as pd
import pickle

app= Flask(__name__)
CORS(app)
data=pd.read_csv("fake_news.csv")

fake_df=pickle.load(open("FakeNewsDF.pkl",'rb'))
tfidf=pickle.load(open("tfidf_v.pkl",'rb'))
model=pickle.load(open("LRegModel.pkl",'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect',methods=['POST'])

def detect():
    title=request.form.get('title')
    news_content=fake_df[fake_df['title'] == title]['content']
    X=tfidf.transform(news_content).toarray()
    prediction=model.predict(X)
    #print(prediction)
    if(prediction[0]==0):
        return 'Real News'
    else:
        return 'Fake News'

if __name__=="__main__":
    app.run(debug=True)
