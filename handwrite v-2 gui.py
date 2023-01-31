import numpy as np
import tkinter as tk
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from tkinter import filedialog
from tkinter import messagebox

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

# Create a GUI
root = tk.Tk()
root.title("Handwritten Digit Classifier")

# Create a function to open a file dialog and predict the digit
def predict_digit():
    file_path = filedialog.askopenfilename()
    if file_path:
        # Load the image and reshape it
        image = ... # load the image data from the file
        image = image.reshape(1, -1)

        # Predict the digit
        prediction = knn.predict(image)
        messagebox.showinfo("Prediction", "The digit is: " + str(prediction[0]))

# Create a button to open a file dialog and make a prediction
predict_button = tk.Button(root, text="Predict Digit", command=predict_digit)
predict_button.pack()

# Start the GUI event loop
root.mainloop()
