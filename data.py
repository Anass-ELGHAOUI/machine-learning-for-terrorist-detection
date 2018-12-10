# the return is X and Y 
from nltk.stem import PorterStemmer
from nltk.tokenize import  word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer #on peux utliser countVectorizer()
from nltk.corpus import stopwords

def load():
    print("------------------------------------------data loaded successefilly---------------- ")
    print("---------------------------------------------------------------")
    file=open('file.txt','r')
    lignes=file.readlines()
    
    #steaming
    
    lignes_steaming=[]
    for sentence in lignes:
        sentence_steam=steamer(sentence)
        lignes_steaming.append(sentence_steam)
    vect = TfidfVectorizer(stop_words=stopwords.words("english"),lowercase=True) #min_df=2,
    X = vect.fit_transform(lignes_steaming)
    file.close()
    #the labels: we have 140 tweets not terroriste then :

    Y=[]
    for i in range(140):
        Y.append(0)
    for i in range(len(lignes)-140):
        Y.append(1)
    return X,Y,vect     # we return the vect in order to do tests 

def steamer(s):
    sentence_return=""
    sentence_steam=s.lower()
    sentence_steam=sentence_steam[:len(sentence_steam)-1]
    ps = PorterStemmer()
    words = word_tokenize(sentence_steam)
    for word in words:
        sentence_return=sentence_return + ps.stem(word)+" "
    return sentence_return

#load()
 
    









