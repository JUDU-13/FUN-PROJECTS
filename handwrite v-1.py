import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

# Load the digits dataset
digits = datasets.load_digits()

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(digits.images, digits.target, test_size=0.25, random_state=0)

# Flatten the images into a single feature vector
X_train = X_train.reshape(X_train.shape[0], -1)
X_test = X_test.reshape(X_test.shape[0], -1)

# Train a KNeighborsClassifier on the training data
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Evaluate the classifier on the test data
accuracy = knn.score(X_test, y_test)
print("Accuracy:", accuracy)

# Predict the digit for a given handwritten image
image = ... # your image data
image = image.reshape(1, -1)
prediction = knn.predict(image)
print("Prediction:", prediction)
