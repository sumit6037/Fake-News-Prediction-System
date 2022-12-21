# Fake-News-Prediction-System
App that detect whether the news is fake or not. 


## Project Summary
According to an MIT study, falsehood diffuses significantly farther, faster, deeper, and more broadly than the truth, 
in all categories of information, and in many cases by an order of magnitude. This is done mainly by clickbaits which 
lure users and entice curiosity with flashy headlines or designs and trick them into clicking the links to increase 
the ad revenues. Hence it is crucial to determine the integrity of the information available on the internet in order to keep the prevalence of fake news in check.

So we’ll now try to build a simple Machine Learning Model using **Logistic Regression** to detect whether a news article is fake or not.

Covering the importance of each library/module/function that we imported:

- **NumPy** : It is a general-purpose array and matrices processing package.
- **Pandas** : It allows us to perform various operations on datasets.
- **re** : It is a built-in RegEx package, which can be used to work with Regular Expressions.
- **NLTK** : It is a suite of libraries and programs for symbolic and statistical natural language processing (NLP).
- **nltk.corpus** : This package defines a collection of corpus reader classes, which can be used to access the contents of a diverse set of corpora.
- **stopwords** : The words which are generally filtered out before processing a natural language are called stop words. These are actually the most common words in any language (like articles, prepositions, pronouns, conjunctions, etc) and does not add much information to the text. (Example-and, of, are etc.)
- **PorterStemmer** : A package to help us with stemming of words. (More about stemming in the Data Preprocessing section)
- **Sci-kit Learn (sklearn)** : It provides a selection of efficient tools for machine learning and statistical modeling including classification, regression, clustering and dimensionality reduction via a consistence interface in Python.
- **feature_extraction.text** : It is used to extract features in a format supported by machine learning algorithms from datasets consisting of text.
- **TfidfVectorizer** : It transforms text to feature vectors that can be used as input to estimator. (More about TfidfVectorizer in the Data Preprocessing section)
- **train_test_split** : It is a function in Sklearn model selection for splitting data arrays into two subsets - for training data and for testing data.
- **LogisticRegression** : A pretty self explanatory part of the code, used to import the Logistic Regression Classifier.
- **metrics and accuracy_score** : To import Accuracy classification score from the metrics module.


 
## Dataset Used

The dataset for the data analysis can be obtained via [kaggle](https://www.kaggle.com/c/fake-news/data?select=train.csv). 


## Deployment/Demo

The project is live/deployed on Streamlit and can be accessed via this [link](https://fake-news-prediction-system.onrender.com)


