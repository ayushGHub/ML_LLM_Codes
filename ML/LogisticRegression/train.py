import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

from LogisticRegression import LogisticRegression
import matplotlib.pyplot as plt

# Load dataset cancer dataset

bc = datasets.load_breast_cancer()

X, y = bc.data, bc.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = LogisticRegression()
clf.fit(X_train, y_train)

predictions = clf.predict(X_test)

accuracy = np.sum(predictions == y_test) / len(y_test)
print(accuracy)