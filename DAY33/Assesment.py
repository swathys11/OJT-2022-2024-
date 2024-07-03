import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, r2_score, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('data.csv')
print(data.head())

# # Handle missing values
missing_value = data.isnull().sum()
print(missing_value)

# # Encode categorical variables
le = LabelEncoder()
for col in data.select_dtypes(include=['object']).columns:
     data[col] = le.fit_transform(data[col])

# # Scale/normalize the features
scaler = StandardScaler()
data[['feature1', 'feature2', 'feature3', 'feature4']] = scaler.fit_transform(data[['feature1', 'feature2', 'feature3', 'feature4']])

# # Exploratory Data Analysis (EDA)
print(data.describe())
sns.pairplot(data)
plt.show()

# # Classification
X = data.drop('target', axis=1)
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

classifiers = [LogisticRegression(), DecisionTreeClassifier(), RandomForestClassifier()]
for clf in classifiers:
     clf.fit(X_train, y_train)
     y_pred = clf.predict(X_test)
     print(f"Classifier: {clf.__class__.__name__}")
     print("Confusion Matrix:")
     print(confusion_matrix(y_test, y_pred))
     print("Accuracy:", accuracy_score(y_test, y_pred))
     print("Precision:", precision_score(y_test, y_pred, average='weighted'))
     print("Recall:", recall_score(y_test, y_pred, average='weighted'))
     print("F1 Score:", f1_score(y_test, y_pred, average='weighted'))
     print()

# # Regression
X = data.drop('target', axis=1)
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

regressors = [LinearRegression(), DecisionTreeRegressor()]
for reg in regressors:
     reg.fit(X_train, y_train)
     y_pred = reg.predict(X_test)
     print(f"Regressor: {reg.__class__.__name__}")
     print("R-squared:", r2_score(y_test, y_pred))
     print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
     print()
     
# # Compute the confusion matrix
cm = confusion_matrix(y_test, y_pred)

# # Plot the confusion matrix
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, cmap='Blues')
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.title('Confusion Matrix')
plt.show()

# # Compute the metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

# # Cross-Validation
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

for clf in classifiers:
     scores = cross_val_score(clf, X, y, cv=kfold)
     print(f"Classifier: {clf.__class__.__name__}")
     print("Cross-Validation Scores:")
     print("Mean:", scores.mean())
     print("Standard Deviation:", scores.std())
     print()

for reg in regressors:
     scores = cross_val_score(reg, X, y, cv=kfold, scoring='neg_mean_squared_error')
     print(f"Regressor: {reg.__class__.__name__}")
     print("Cross-Validation Scores:")
     print("Mean:", -scores.mean())
     print("Standard Deviation:", scores.std())
     print()
     
     
