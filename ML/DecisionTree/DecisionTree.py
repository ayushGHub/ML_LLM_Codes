#DecisionTree Code
# Split Feature
# Split Point
# When to stop splitting
# STEPS:
# 1. We start with calculaton "Information Gain" for each possible splot which has which feature to split and at what value to split
# 2. Divide set with the feature and value that gives maximum information gain.
# 3. Divide tree and do the same for all created branches
# 4. .... until a "Stopping Criteria" is achieved
#  
# IG = E(parent) - [weighted average] . E(children)
# Entropy = E = -SUM( p(X).log2(p(X))) - 
# p(X) = #x/n is the numbr of times a class has occured in the node divided by total number of data points at that noode
# Stopping Criteria - max depth, min of samples (a nnode can have if less thenn divide), min impurity decrease (min entropy change to happend split)

# Keep Node and Tree Separate
import numpy as np
from collections import Counter

class Node():
    def __init__(self, feature=None, threshold=None, left=None, right=None, *, value=None): # reason of adding  '*'
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

    def is_leaf_node(self):
        return self.value is not None
    

class DecisionTree():
    def __init__(self, min_sample_split = 2, max_depth = 10, n_features = None, min_impurity_decrease = 0.05):
        self.min_sample_split = min_sample_split
        self.max_depth = max_depth
        self.n_features = n_features
        self.root = None
        self.min_impurity_decrease = min_impurity_decrease
        

    def fit(self, X, y):
        self.n_features = X.shape[1] if not self.n_features else min(X.shape[1], self.n_features)
        self.root = self._grow_tree(X,y) # helper function to return the root of the tree at the end

    
    def _grow_tree(self, X,y,depth=0):
       
       n_samples, n_feats = X.shape
       n_labels = len(np.unique(y))

       # first check the stopping criteria
       if (depth >= self.max_depth or n_labels == 1 or n_samples < self.min_sample_split):
           # if all the criteria above is fullfilled it means there is no need to split the node again and return the leaf noe
           leaf_value = self._most_common_label(y)
           return Node(value=leaf_value)
       

       feat_idxs = np.random.choice(n_feats, self.n_features, replace=True ) # involve randomness among the features and shape of features
        # how many feature you want to consider
       # if above criteria is not fulfilled then we have to find the best split.

       # find the best split
       best_feature, best_threshold = self._best_split(X,y, feat_idxs) # another helper function
        
       # Create child node and call the _grow_tree function again to create new subtree and will be recursive in nature.  
       left_idxs, right_idxs = self._split(X[:,best_feature], best_threshold)

       left = self._grow_tree(X[left_idxs, :], y[left_idxs], depth+1)
       right = self._grow_tree(X[right_idxs, :], y[right_idxs], depth+1)

       return Node(best_feature, best_threshold, left, right)


    def _best_split(self, X, y, feat_idxs):
        # What we are going to do here is to find a threshold among all the possible thresholds, 
        # all possible split that are out there and chose the best one.
        best_gain  = -1
        split_idx, split_threshold = None, None

        for feat_idx, in feat_idxs: # all featurs in feature indices
            X_column = X[:,feat_idx]
        
            thresholds = np.unique(X_column)

            for threshold in thresholds:
                # calculate the information gain
                gain = self._information_gain(y,X_column, threshold) # Another helper function

                if gain > best_gain:
                    best_gain = gain
                    split_idx = feat_idx
                    split_threshold = threshold
        return split_idx, split_threshold 

    def _information_gain(self,y, X_column, threshold):
        # parent entropy

        parent_entropy = self._entropy(y)

        # children entropy
        left_idx, right_idx = self._split(X_column, threshold)

        if len(left_idx) == 0 or len(right_idx) == 0:
            return 0
        # calculate wieghted entropy of children

        n = len(y)
        n_l, n_r = len(left_idx), len(right_idx)
        e_l,e_r = self._entropy(y[left_idx]), self._entropy(y[right_idx])
        child_entropy = (n_l/n) * e_l + (n_r/n)*e_r
        # calculate the IG.

        information_gain = parent_entropy - child_entropy
        return information_gain

    def _split(self, X_column, split_thresh):
        left_idxs= np.argwhere(X_column <=split_thresh).flatten()
        right_idxs = np.argwhere(X_column > split_thresh).flatten()

        return left_idxs, right_idxs

    def _entropy(self, y):
        hist = np.bincount(y)
        ps = hist/len(y)

        return -np.sum([p * np.log(p) for p in ps if p >0])
        # pass

    def _most_common_labels(self, y):
        counter = Counter(y)
        value =  counter.most_common(1)[0][0]
        return value


    def predict(self, X):
        np.array([self._traverse_tree(x, self.root) for x in X])

    def _traverse_tree(self,x,node):
        if node.is_leaf_node():
            return node.value
    
        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x, node.left)
        
        return self._traverse_tree(x, node.right)