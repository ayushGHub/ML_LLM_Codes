import numpy as np

# Here we will calculate the prediction value as y_hat = W*x + B - where we have to calculate W and B. 
# There are two ways to do that- 
    # 1. We can calculate W and B using a Standard Deviation Formular
    # 2. Or we can calculate MSE for each data point and take a derivative to find the mimimm where we get the W and B with 
    # minimum Error using technique call gradient Descent. 
    # Learning rate is also decided to move the point towards minima while - Basically it tells us how fast or slow to in the 
    # direction gradient tell it to go.
    # calculating gradient descent. w = w - alpha*dw and same goes for b. 
# Once we calculate W and B, we will put the X_test in the predict function to get the value
# Initialize W and B as zero
# Predict result by function y_har = W*x + b
# Caldulate Error
# Use Gradient Descent to figure ot new weights and biases.
# Repeat n times 
# Or stop when error stops moving less than a threshold in certain steps - called early stopping.
# Function for gradient descent is - dJ/dW = 1/N sum(2*x(y_hat - y))    dJ/dB = 1/N sum(2*(y_hat - y))


class LinearRegression:

    def __init__(self, lr = 0.001, n_iter = 100):
        self.lr = lr
        self.n_iter = n_iter
        self.weights = None # we are initializing the 
        self.bias = None


    def fit(self, X, y):
        n_samples, n_features = X.shape  # To make it generic function We need to find our the number of 
                                         # features as that will determin the spahe of W.
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iter):
            y_pred = np.dot(X, self.weights) + self.bias

            dw = (1/n_samples) * np.dot(X.T, (y_pred - y)) # This dot product in numpy includes the summation as mentioned in the equation
                                                        # and gives one number only
            db = (1/n_samples) * np.sum(y_pred - y)

            self.weights = self.weights - self.lr * dw
            self.bias    = self.bias - self.lr * db

    def predict(self, X_test):
        
        predicted_value = np.dot(X_test, self.weights) + self.bias
    
        return predicted_value