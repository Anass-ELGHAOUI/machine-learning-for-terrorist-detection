import DecisionTree
import KnearestNeighbers
import SVM
import os
print("***********************PROJET FIN D'ANNEE**************************")
print("***********************PROJET FIN D'ANNEE**************************")
print("***********************PROJET FIN D'ANNEE**************************")
print("***********************PROJET FIN D'ANNEE**************************")
print("\n********************************load of the data***************** \n ")

continuer="o"
while(continuer=="o"):
    algo=input("______________________________choisir l'agorihme qui vous convient________________________\n knearestNeigbers : \t tapper k \n DecisionTree : \t tapper d \n SVM : \t\t tapper s\n")
    
    if(algo=='d'):
        DecisionTree.action()
    elif(algo=='s'):
        SVM.action()
    elif(algo=='k'):
        KnearestNeighbers.action()
    print("voulez-vous continuer , taper (O/N)")
    continuer=input()
print("-------------FIN----------")
os.system("pause")
