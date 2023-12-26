import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
path = "/content/drive/MyDrive/spam.csv"
df = pd.read_csv(path, encoding = 'latin-1')
df.head()
df = df.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"],axis=1)
df.head()
df = df.rename(columns= {"v1":"label","v2":"text"})
df.head()
df.describe()
df.info()
df.label.value_counts()
df['length'] = df['text'].apply(len)
df.head()
df.hist(column='length',by='label',bins=60,figsize = (10,10))
df.loc[:,'label'] = df.label.map({'ham':'0', 'spam':'1'})
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

count=CountVectorizer()
input=['REMINDER FROM O2: To get 2.50 pounds free call credit and details of great offers pls reply 2 this text with your valid name, house no and postcode']

text=count.fit_transform(df['text'])

x_train, x_test, y_train, y_test= train_test_split(text, df['label'], test_size=0.20, random_state=1)
text
print(x_train.shape)
print(x_test.shape)

input=text[5571]
from sklearn.neural_network import MLPClassifier

model=MLPClassifier()
model.fit(x_train, y_train)
prediction=model.predict(x_test)
print(prediction)
input
model.predict(input)
data=df['text']
data=df['text']
data.loc[len(data.index)]=" "
data
text=count.fit_transform(data)
text
input=text[5571]
model.predict(input)
