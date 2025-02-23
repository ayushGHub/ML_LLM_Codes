# Here we will be mostly loading the dataset and doing all the operations on the dataset.

import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from knn import KNN

cmap = ListedColormap(['#FF0000','#00FF00','#0000FF'])

iris = datasets.load_iris()

X, y = iris.data, iris.target
# print(iris.data)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.1, random_state=422)

# plt.figure()
# plt.scatter(X[:,2],X[:,3], c = y, cmap=cmap, edgecolors='k', s=20)
# plt.show()

model = KNN(k=5)
model.fit_knn(X_train, y_train)

predictions = model.predict_knn(X_test)
# print(predictions)

accuracy = np.sum(predictions == y_test) / len(y_test)
print(accuracy)
