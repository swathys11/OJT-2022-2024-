import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Dummy dataset (replace this with your actual dataset loading)

df = pd.read_csv('housing_price.csv')

# Separate features (X) and target (y)
X = df[['size', 'bedrooms']].values
y = df['price'].values

# Initialize the model
model = LinearRegression()

# Create a categorical variable to use with StratifiedKFold (not typical for regression)
# Here, we create 3 bins for demonstration purposes
num_bins = 3
df['price_bin'] = pd.qcut(df['price'], q=num_bins, labels=False)

# Initialize Stratified KFold cross-validation
skf = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)

mean_scores = []

# Perform cross-validation
for train_index, test_index in skf.split(X, df['price_bin']):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    
    # Train the model
    model.fit(X_train, y_train)
    
    # Predict on the test set
    y_pred = model.predict(X_test)
    
    # Calculate mean absolute error
    mean_error = mean_absolute_error(y_test, y_pred)
    mean_scores.append(mean_error)

# Calculate average mean absolute error
average_mean = np.mean(mean_scores)
print("Average Mean Absolute Error:", average_mean)
