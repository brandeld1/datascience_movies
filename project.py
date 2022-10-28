import pandas as pd
import nltk

""""
nltk.download()
nltk.download([
     "names",
     "stopwords",
     "state_union",
     "twitter_samples",
     "movie_reviews",
     "averaged_perceptron_tagger",
     "vader_lexicon",
     "punkt",
])
"""

#get the datasets
df1 = pd.read_csv("../MovieData/movies.csv")
df2 = pd.read_csv("../MovieData/ratings.csv")
df3 = pd.read_csv("../MovieData/tags.csv")

#remove useless data
df2.drop(['timestamp','userId'], inplace=True, axis=1)
df3.drop(['userId','timestamp'], inplace=True, axis=1)

#combine datasets and remove repitive rows, combine ratings based on mean
df1 = df1.merge(df2, on='movieId')
df1 = df1.groupby(['movieId','title','genres'],as_index=False,sort=False)['rating'].mean().round(1)

#combine datasets and combine rows with tags as an array 
df3 = df3.groupby('movieId')['tag'].apply(list).reset_index()
df1 = df1.merge(df3, on='movieId')
df1.insert(5,'sentiment',0,True)

#for testing to make the dataset smaller, delete later
df1 = df1.iloc[40000:,]
 
 #creating a year column
number=""
df1.insert(2,'year',0,True)
for ind in df1.index:
    if(ind-40000!=0 and number!=''):
                number[slice(len(number)-4, len(number))]
                df1.iloc[ind-40000-1,2]=float(number)
                number=""
    for character in df1.iloc[ind-40000,1]:
        if character.isnumeric():
            number+=character


#for creating Sentiment scores
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

#for creating Sentiment scores
sentimentSum=0
for ind in df1.index:
        if(ind-40000!=0):
            df1.iloc[ind-40000-1,6]=sentimentSum
        sentimentSum=0
        for word in df1.iloc[ind-40000,5]:
            sentimentSum+=round(sia.polarity_scores(word)['compound'],1)

print(df1.head())






