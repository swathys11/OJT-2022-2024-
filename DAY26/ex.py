import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#load the dataset sample_dataset.csv
df = pd.read_csv('sample_dataset.csv')
print(df.head())

#mean and standard deviation of the Sepal Length
mean_sepal_length = df['Sepal Length (cm)'].mean()
std_sepal_length = df['Sepal Length (cm)'].std()
print("Mean Sepal Length: ",mean_sepal_length)
print("Standard Deviation Sepal Length: ",std_sepal_length)


# Check for any missing values in the dataset. How would you handle them if there were any?
print("Checking for missing values:")
print(df.isnull().sum())

# Convert the species labels to numerical values using a mapping dictionary.
species_mapping = {'FlowerA': 0, 'FlowerB': 1, 'FlowerC': 2}
df['Species'] = df['Species'].map(species_mapping)
print("Dataset with numerical species labels:")
print(df.head())

#  Split the dataset into training and testing sets with 70% training data and 30% testing data. Ensure that the split is stratified based on the species.
X = df.drop('Species', axis=1)
y = df['Species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)
# print("Training and testing data split:")
# print("Training set size: ",X_train.shape[0])
# print("Testing set size: ",X_test.shape[0])

#  Train a decision tree classifier on the training data. What parameters would you use for the decision tree?
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Visualize the trained decision tree.
plt.figure(figsize=(10, 5))
tree.plot_tree(clf, feature_names=X.columns, class_names=list(species_mapping.keys()), filled=True)
plt.title("Decision Tree")
plt.show()

#  Predict the species for the testing data and compute the accuracy.
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy of the decision tree classifier: ",accuracy)

#  Generate a classification report and a confusion matrix for the predictions.
print("Classification Report:", classification_report(y_test, y_pred, target_names=list(species_mapping.keys())))
print("Confusion Matrix:",confusion_matrix(y_test, y_pred))
