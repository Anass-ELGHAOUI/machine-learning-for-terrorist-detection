from sklearn import  cross_validation
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import data
def action():
       """
           load the data from a file(data.data)
       """
       X,Y,vect=data.load()

       """
           split the data into a training set and test set
       """
       X_train,X_test,Y_train,Y_test=cross_validation.train_test_split(X,Y,test_size=0.5)

       """
                 Build our classifier or our model 
       """
       clf= DecisionTreeClassifier(criterion=’gini’, splitter=’best’, max_depth=None, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0,
                                   max_features=None,random_state=None, max_leaf_nodes=None, min_impurity_decrease=0.0, min_impurity_split=None, class_weight=None,presort=False) 
       clf.fit(X_train,Y_train)

       """
           test the accruancy of our model
       """
       print("\n the accruacy of the algorithme is : \n")
       accruancy=clf.score(X_test,Y_test)
       print(accruancy)

       """
          an example of test,  
       """
       tweet=input("\n donner un tweet")
       l=[tweet]    # we consider each tweet as a unique string, than we obtain the vector
       test=(vect.transform(l))
       pred=clf.predict(test.toarray())
       if pred==0:
              print("\n non terroriste")
       else:
              print("\n  terroriste")


















