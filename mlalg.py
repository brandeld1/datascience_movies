import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import linear_model
#from sklearn.cross_validation import train_test_split


#df1 = pd.read_csv("combinedMRData.csv")
df1 = pd.read_csv("combinedMRData.csv")


df1.replace(to_replace='Action', value=1, inplace=True)
df1.replace(to_replace='Adventure', value=2, inplace=True)
df1.replace(to_replace='Animation', value=3, inplace=True)
df1.replace(to_replace='Children', value=4, inplace=True)
df1.replace(to_replace='Comedy', value=5, inplace=True)
df1.replace(to_replace='Crime', value=6, inplace=True)
df1.replace(to_replace='Documentary', value=7, inplace=True)
df1.replace(to_replace='Drama', value=8, inplace=True)
df1.replace(to_replace='Fantasy', value=9, inplace=True)
df1.replace(to_replace='Film-Noir', value=10, inplace=True)
df1.replace(to_replace='Horror', value=11, inplace=True)
df1.replace(to_replace='IMAX', value=12, inplace=True)
df1.replace(to_replace='Musical', value=13, inplace=True)
df1.replace(to_replace='Mystery', value=14, inplace=True)
df1.replace(to_replace='Romance', value=15, inplace=True)
df1.replace(to_replace='Sci-Fi', value=16, inplace=True)
df1.replace(to_replace='Thriller', value=17, inplace=True)
df1.replace(to_replace='War', value=18, inplace=True)
df1.replace(to_replace='Western', value=19, inplace=True)



label=[]
allFeatures =[]

current_year = 1900
max_count = 0
saved_sentiment = 0
saved_genre = 0
saved_rating = 0

for ind in df1.index:
        label.append([df1.iloc[ind,1]])
        allFeatures.append([df1.iloc[ind,0],df1.iloc[ind,2],round(df1.iloc[ind,3],1),round(df1.iloc[ind,4])])


print(label)
print(allFeatures)


# Import train_test_split function

# Split dataset into training set and test set


X_train, X_test, y_train, y_test = train_test_split(allFeatures, label, test_size=0.3,random_state=109) # 70% training and 30% test

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
print(knn.fit(X_train, y_train))
print(knn.score(X_test, y_test))
print(knn.predict([[1897,2.8,-1,2]]))