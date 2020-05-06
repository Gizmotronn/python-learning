# Classification-tree

[Course `link`](https://campus.datacamp.com/courses/machine-learning-with-tree-based-models-in-python/classification-and-regression-trees?ex=1)

* A classification tree is a series of if-else questions about individual features
* Objective - infer class labels
* Able to capture non-linear relationships between features and labels



## Breast Cancer Dataset - 2D

* Program predicts if the tumor is malignant or benign based on certain parameters



## Classification-tree in scikit-learn

```python
# Import DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier

# Import train_test_split
from sklearn.model_selection import train_test_split

# Import accuracy_score
from sklearn.metrics import accuracy_score



# Split the data into 80% train, 20% test - using train_test_split
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.2, stratify=y, random_state=1)

# Use/instatiate decision tree classifier (dt)
dt = DecisionTreeClassifier(max_depth=2, random_state=1 # random_state is set to 1 for reproducability
                            
# Fit dt to the training (80%) set
dt.fit(X_train, y_train)

                            
# Predict test set labels
y_pred = dt.predict(X_test)                            

# Evaluate test-set accuracy
accuracy_score(y_test, y_pred) 
print(accuracy_score)  # 0.903....                          
```

* A classification model divides the features into regions where all instances are assigned to ONE class label (for example, malignant OR benign)
* These regions = decision regions
* Separated by decision boundaries (straight line)



## Evaluating classification tree performance 

[`Datacamp Test`](https://campus.datacamp.com/courses/machine-learning-with-tree-based-models-in-python/classification-and-regression-trees?ex=3)

```python
# Import DecisionTreeClassifier from sklearn.tree
from sklearn.tree import DecisionTreeClassifier

# Instantiate a DecisionTreeClassifier 'dt' with a maximum depth of 6
dt = DecisionTreeClassifier(max_depth=6, random_state=SEED)

# Fit dt to the training set
dt.fit(X_train, y_train)

# Predict test set labels
y_pred = dt.predict(X_test)
print(y_pred[0:5])

>> Returns [0 0 0 1 0]
```

Part 2

```python
# Import accuracy_score
from sklearn.metrics import accuracy_score

# Predict test set labels
y_pred = dt.predict(X_test)

# Compute test set accuracy  
acc = accuracy_score(y_test, y_pred)
print("Test set accuracy: {:.2f}".format(acc))

>>
	<script.py> output:
    Test set accuracy: 0.89
```

