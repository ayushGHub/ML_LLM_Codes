# There is one big difference between Logistic and Linear is the final function.
# In logistic we have sigmoid function instead of simple x. z = 1/1+e^-x

import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

class LogisticRegression():

    def __init__(self, lr = 0.01, n_iter = 10):
        self.lr = lr
        self.n_iter = n_iter
        self.weights = None
        self.bias = None

    
    def fit(self, X, y):

        n_samples, n_features = X.shape

        self.weights = np.zeros(n_features)
        self.bias = 0


        for _ in range(self.n_iter):

            
            linear_pred = np.dot(self.weights, X) + self.bias
            y_pred = sigmoid(linear_pred)
            
            dw = (1/n_samples) * np.dot(X.T, (y_pred - y)) # This dot product in numpy includes the summation as mentioned in the equation
                                                            # and gives one number only
            db = (1/n_samples) * np.sum(y_pred - y)

            self.weights = self.weights - self.lr * dw
            self.bias = self.bias - self.lr * db

    def predict(self, x):
        
        linear_pred = np.dot(self.weights, x) + self.bias
        y_pred = sigmoid(linear_pred)

        class_pred = [0 if y <= 0.5 else 1 for y in y_pred]
        return class_pred