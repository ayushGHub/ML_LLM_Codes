- #### Supervised
1. **Regression** - Linear Regression Model - Supercised Learning
2. **Logistic Regression** - - Instead of fitting line, we fit Sigmoid function - 1/1+e^(x^(-1))
3. **K-Nearest Neighbor** - Used both for Regression and Classification - Non-Parametric Algo - any given new data point we predict the average of it's k-nearest neighbor, 
4. **Support vector Machine** -  Mostly for classification but can be used for Regression - decision boundary maximizing space between separate classes - support Vectors are data that sits on the edge of the margin - Less sensitive to noise or outliers - Powerful in high-dimensions - feature is large - kernel functions that are used to find the non-liunear decision boundaries, they use to trandform original features to more new complex features - Possible kernel functions are - RBF, Sigmoid, Polynomial, Dot Product.
5. **Naive Bias Classifier** - Spam Filter 
6. **Decision Trees** - Supervised - Series of yes/No questions - 
7. **Random Forest** - Which is bagging fashion of lots of decision trees - Powerestimator - classification and regression both- Running Decision Trees in Parallel
8. **Boosting** - Running decision tress in sequential fashion.Each model are focussed on fixxing error from previous models in the next steps- collection of weak learners are converted into strong learners - Series of week models - Slower to train coz of sequential nature - more prone to overfitting - AdaBoost, Gradient Boosting, XGBoost
9. **Neural Networks** - layers of unknown variables - hidden layers - predict hidden from input and output from hidden layers-
- #### Unsupervised
10. **K-Means** - No labels so more like clsuters - K is hyperparameter - Start with randomly selecting centers for K clusters - And assing all data that are closest to the centers to this cluster - Calcuate the cluster center again on the basis of data points assigned to the current cluster - Then center will keep moving to the actual cluster center - Assign the data points again - Repeat until center is stablized.
11. **PCA** - 