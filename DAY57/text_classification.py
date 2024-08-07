#create a model with logistic regression and BOW for the text classification
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

#create sample data
review = [
    "I love the movie, it was good",
    "the movie was boring",
    "excellent movie , actors done well",
    "It was a normal movie, nothing special"
]
#positive = 1, negative = 0, neutral = 2
labels = [1, 0, 1, 2]

#create vectorization for the above

vectorizer = CountVectorizer()
x = vectorizer.fit_transform(review)
y = np.array(labels)
#splitted the trains sets and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#create our model
model = LogisticRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy", accuracy)

#crete a sample reviesw for the prediciton
new_review = ["i really enjoyed the movie"]
new_review_vectorized =vectorizer.transform(new_review)
prediction = model.predict(new_review_vectorized)
print("prediction: ", prediction)