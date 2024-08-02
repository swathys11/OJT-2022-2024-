from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

sample = ["I love the concept of NLP ","It was  difficult for me to understand","Sentiment analysis was much easier","ML is hard to understand"]
labels = ["Positive","Negative","Positive","Negative"]

#initialize the count vectorizer
vectorizer = CountVectorizer() 

x = vectorizer.fit_transform(sample)
x_train, x_test, y_train, y_test = train_test_split(x, labels, test_size=0.25, random_state=42)

#initializing the navie bayes classifier
nb = MultinomialNB()
nb.fit(x_train,y_train)

y_pred = nb. predict(x_test)
accuracy = accuracy_score(y_test,y_pred)
print("Accuracy score: ", accuracy)