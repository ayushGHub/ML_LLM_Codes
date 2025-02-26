# train i

from sklearn import datasets
from sklearn.model_selection import train_test_split
from DecisionTree import Node
from DecisionTree import DecisionTree

import numpy as np

bc = datasets.load_breast_cancer()
X, y = bc.data, bc.target

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

clf = DecisionTree()
clf.fit(X_train, y_train)

predictions = clf.predict(X_test)

accurary = np.sum(y_test == predictions) / len(y_test)

print(accurary)