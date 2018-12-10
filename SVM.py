from sklearn import  cross_validation
import numpy as np
from sklearn import svm
import data

def action():
    """
    load the data from a file(data.data)
    """
    X,Y,vect=data.load()

    """
        split the data into a training set and test set
    """
    X_train,X_test,Y_train,Y_test=cross_validation.train_test_split(X,Y,test_size=0.2)

    """
        Build our classifier or our model 
    """
    clf=svm.SVC()
    clf.fit(X_train,Y_train)

    """
    test the accruancy of our model
    """
    print("The accruacy of the algorithme is : \n")
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
