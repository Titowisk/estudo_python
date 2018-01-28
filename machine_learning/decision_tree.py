# Requirements:
# python 3.6 or higher
# sklearn (http://scikit-learn.org/stable/)

from sklearn import tree

features = [
            [0,8], [0,9], [0,10], [0,12], [0,14], 
            [0,15], [0,17], [0,18], [0,21], [0,28], 
            [0,40] ,[1,11] ,[1,13] ,[1,16] ,[1,19], 
            [1,20], [1,25], [1,26], [1,29], [1,30], 
            [1,35], [1,36]
            ]

labels = [
    2, 2, 2, 2, 2,
    1, 1, 1, 1, 1, 1,
    2, 2,
    0, 0, 0, 0, 0, 0, 0, 0, 0
     ] # 0 for Action, 1 for Horror and 2 for Fantasy

# the classifier finds patterns in the trainning data
clf = tree.DecisionTreeClassifier() # classifier instance
clf = clf.fit(features, labels) # fit find patterns in the data

# Sample classification (Male, 27 years, Action)
print(clf.predict([[1, 27]])) # Expected [0]