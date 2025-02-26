# Principal Component Analysis
# What PCA does it transforms the features/dimension into multiple features which are orthogonal to each other 
# (hence linearly independent) and then we select dimensions with the axis which has maximum variance, also the number of dimensions we choose depends 
# on the amount of variance (eigenvalue threshold or a cumulative variance percentage) we want to capture or the 
# nature of the task (like plotting in 2D or 3D).
# UPdated : There are a few grammatical and clarity issues in your explanation. Here's a corrected and clearer version:

# Principal Component Analysis (PCA)
# PCA transforms the original features into a new set of orthogonal features (principal components). 
# These components are ranked by the amount of variance they capture, with the first principal component
#  having the highest variance. The number of dimensions we select depends on how much 
# variance we want to retain or the specific task requirements (e.g., reducing dimensions for visualization in 2D or 3D).
#  

import numpy as np

# Variance = 1/n SUM(x_i - x_mean)^2
# Covariance (X,Y) = 1/n SUM(x_i - x_mean)(y_i - y_mean)^T
# Eigenvectors and Eigenvalues - Eigenvectors point in the direction of the maximum variance and 
# the corresponding eigenvalues indicate the importance of it's corresponding eigenvectors.
# Av = Lambda.v

# Steps
# Subtract the mean frmo X
# Calculate Cov(X, X)
# Calculate eigenvectors and eigenvalues of the covariance matrix
# Sort the eigenvectors according to their eigenvalues in their descending order
# Choose first K eigenvectors that will be the new K dimensions
# Transform the original n-dimensional data points into k dimensions (Projections with dot product)
#  

class PCA():
    def __init__(self, n_components):
        self.n_components = n_components
        self.components = None
        self.mean = None

    def fit(self, X):
        self.mean = np.mean(X, axis=0) # clarify later about axis = 0 or axis = 1 thing.
        X = X - self.mean
        # covariance
        cov = np.cov(X.T) 

        # Eigenvectors , Eigenvalues

        eigenvectors, eigenvalues = np.linalg.eig(cov) # np.linalg.eig -- Look into this also

        # eigenvectors v = [:, i] column vector and transpose for easy calculation
        eigenvectors = eigenvectors.T

        # sort eigenvectors
        idxs = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[idxs]
        eigenvectors = eigenvectors[idxs]

        self.components  = eigenvalues[:self.n_components]

    def transform(self, X):
        # pass
        # self.mean = np.mean(X, axis=0) # clarify later about axis = 0 or axis = 1 thing.
        X = X - self.mean

        return np.dot(X, self.components.T)
    

    # testing

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from sklearn import datasets

    data = datasets.load_iris()
    X, y = data.data, data.target

    pca = PCA(2)
    pca.fit(X)
    X_project = pca.transform(X)
    # print(X_project)

    x1 = X_project[:,0]
    x2 = X_project[:,1]

    plt.scatter(x1, x2, c=y,edgecolors='none', alpha=0.8, cmap=plt.cm.get_cmap('viridis',3))
    plt.colorbar()
    plt.show()