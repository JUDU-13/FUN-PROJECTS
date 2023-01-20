import numpy as np
import cv2
from sklearn import svm
from sklearn.metrics import accuracy_score

# Load the pre-trained model
clf = svm.SVC()
clf.fit(X_train, y_train)

# Start the webcam
cap = cv2.VideoCapture(0)

while True:
    # Get a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Use OpenCV to detect shapes in the frame
    shapes = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    shapes = shapes[0] if len(shapes) == 2 else shapes[1]

    for shape in shapes:
        # Get the shape's bounding rectangle
        x, y, w, h = cv2.boundingRect(shape)

        # Use the model to classify the shape
        shape_data = [[w, h]]
        shape_type = clf.predict(shape_data)[0]

        # Draw the shape's bounding rectangle on the frame
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

