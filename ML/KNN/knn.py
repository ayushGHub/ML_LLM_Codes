# Supervised Learning It is.
# Given a new data point - We need to classify or predict which class it belongs to
# What we have to do is, we have to calcuate the euclidian distance of the new data point 
    # with all the points in the dataspace and then we will select the nearest K data points and 
    # majority of them will decide the class it belongs to in case of CLASSIFICATION or 
    # average of their values in case of REGRESSION.
# The number of K points we will consider will depend on the value of K.

# We will need 1 euclidian distance function
# Activate VENV .\Scripts\Activate.ps1

import numpy as np
from collections import Counter

def euclidian_distance(X1, X2): # This Euclidian function is the global function.
    # Find out why we did not use "self" here 
    return np.sqrt(np.sum((X1-X2)**2))

#declare a class called KNN
class KNN: # it should have an init function the class.
    def __init__(self, k=3):
        self.K = k

    # Then Each of the Class of an algorithm should have FIT function and PREDIT FUNCTION - In case of supervised Learning.
    def fit_knn(self, X, y): # This is where we will pass the data for training which is basically X and y 
        self.X_train = X
        self.y_train = y
        # pass
    # In this function we will be doing all the calculation, find the distance with all the data points, 
    # and find the K most closest points. 
    def predict_knn(self,X):

        predicted_label = [self._predict(x) for x in X]

        return predicted_label

    def _predict(self,x): # This is basically the helper function for predict_knn where calculation will happen
        # For global functions we do not need to use Self.

        distances = [euclidian_distance(x,x_train) for x_train in self.X_train] 
        
        # Now we need to sort the distance for finding the nearest one.
        # To sort we will use argsort from numpy which will also gives us the indices.

        k_indices = np.argsort(distances)[:self.K]
        k_nearest_labels = [self.y_train[i] for i in k_indices]

        # Now we need to find the most common one from k_indices, so for that we will use Couter Library function most_common()
        majority_label = Counter(k_nearest_labels).most_common()

        return majority_label[0][0]
