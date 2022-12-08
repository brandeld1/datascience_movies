import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import linear_model
#from sklearn.cross_validation import train_test_split


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
"""
for ind in df1.index:
        label.append(df1.iloc[ind,1])
        allFeatures.append([df1.iloc[ind,0],df1.iloc[ind,2],round(df1.iloc[ind,3],1),round(df1.iloc[ind,4])])


print(label)
print(allFeatures)
"""
"""
for ind in df1.index:
    if(df1.iloc[ind,0]!=current_year):
        allFeatures.append([current_year,saved_rating,saved_sentiment,round(max_count)])
        label.append([saved_genre])
        max_count=0
        current_year = df1.iloc[ind,0]
    else:
        if(df1.iloc[ind,4]>max_count):
            max_count = df1.iloc[ind,4]
            saved_genre = df1.iloc[ind,1]
            saved_rating = round(float(df1.iloc[ind,2]),1)
            #saved_sentiment = round(float(df1.iloc[ind,3]),1)
            if(df1.iloc[ind,3]>0):
                saved_sentiment = 1
            elif(df1.iloc[ind,3]<0):
                saved_sentiment = -1
            elif(df1.iloc[ind,3]==0):
                saved_sentiment = 0

print(label)
print(allFeatures)
"""

"""

for ind in df1.index:
    if(df1.iloc[ind,0]!=current_year):
        allFeatures.append([saved_genre,saved_rating,saved_sentiment,round(max_count)])
        label.append([current_year])
        max_count=0
        current_year = df1.iloc[ind,0]
    else:
        if(df1.iloc[ind,4]>max_count):
            max_count = df1.iloc[ind,4]
            saved_genre = df1.iloc[ind,1]
            saved_rating = round(float(df1.iloc[ind,2]),1)
            #saved_sentiment = round(float(df1.iloc[ind,3]),1)
            if(df1.iloc[ind,3]>0):
                saved_sentiment = 1
            elif(df1.iloc[ind,3]<0):
                saved_sentiment = -1
            elif(df1.iloc[ind,3]==0):
                saved_sentiment = 0

print(label)
print(allFeatures)
"""


# Import train_test_split function

# Split dataset into training set and test set


X_train, X_test, y_train, y_test = train_test_split(allFeatures, label, test_size=0.3,random_state=109) # 70% training and 30% test

"""
regr = linear_model.LinearRegression()
regr.fit(X_train, y_train)
print(regr.score(X_test, y_test))
print(regr.predict([[3,0.7666666666666669,24.0]]))

"""
#Import Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB

#Create a Gaussian Classifier
gnb = GaussianNB()

#Train the model using the training sets
gnb.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = gnb.predict(X_test)

#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

print(gnb.predict([[2005,2.546610169491525,-2.102542372881356,118.0]]))
"""
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
print(knn.fit(X_train, y_train))
print(knn.score(X_test, y_test))
print(knn.predict([[1897,2.8,-1,2]]))

"""
