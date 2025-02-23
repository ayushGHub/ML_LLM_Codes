import numpy as np

from sklearn.model_selection import train_test_split
from sklearn import datasets

import matplotlib.pyplot as plt
from LinearRegression import LinearRegression

X, y = datasets.make_regression(n_samples=100, n_features=1, noise=20, random_state=345)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=456)

# fig = plt.figure(figsize=(8,6))

# plt.scatter(X[:,0], y, s=20, color= 'b', marker="o")
# plt.show()

clf = LinearRegression(lr=0.01, n_iter=500)
clf.fit(X_train,y_train)

predictions = clf.predict(X_test)
# print(predictions)

errors =  np.mean((predictions - y_test)**2)
print(errors)

y_pred_line = clf.predict(X)

cmap = plt.get_cmap('viridis')

fig = plt.figure(figsize=[8,6])
m1 = plt.scatter(X_train, y_train, color=cmap(0.9), s = 10)
m2 = plt.scatter(X_test, y_test, color=cmap(0.3), s = 10)

plt.plot(X, y_pred_line, color='b', linewidth = 2)
plt.show()