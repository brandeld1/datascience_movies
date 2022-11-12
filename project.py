import pandas as pd

""""
import nltk
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
 
 #creating a year column
wholeNumbers=['0','1','2','3','4','5','6','7','8','9']
number=""
df1.insert(2,'year',0,True)
for ind in df1.index:
    if(ind!=0 and number!=''):
            number[slice(len(number)-4, len(number))]
            df1.iloc[ind-1,2]=float(number)
            number=""
    for character in df1.iloc[ind,1]:
        if character in wholeNumbers:
            number+=character


#for creating Sentiment scores
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

#for creating Sentiment scores
sentimentSum=0
for ind in df1.index:
        if(ind!=0):
            df1.iloc[ind-1,6]=sentimentSum
        sentimentSum=0
        for word in df1.iloc[ind,5]:
            sentimentSum+=round(sia.polarity_scores(str(word))['compound'],1)


#separate genres
dummies=df1['genres'].str.get_dummies()
tidy_movie_ratings=(pd.concat([df1, dummies], axis=1)
                    .drop(["movieId", "tag", "genres"], axis=1)
                )
#remove year from movie title
import re
start = "("
end = ")"
tidy_movie_ratings['title'] = tidy_movie_ratings['title'].str.replace(fr'(?s){re.escape(start)}.*?{re.escape(end)}', '', regex=True)
#tidy_movie_ratings.reset_index(inplace=True)

#finding most popular genre
genre_rank = (tidy_movie_ratings.iloc[:, 5:] # get the genre columns only
              .sum() # sum them up
              .sort_values(ascending=False) # sort descending
              .head(1)
              .index.values # get the genre names
              )

column_to_move = tidy_movie_ratings.pop("year")

#find most popular movie within a year
x=int(input("Enter a year within 1995 and 2018: "))

tidy_movie_ratings.insert(4, "year", column_to_move)

genre_groups = (tidy_movie_ratings.iloc[:, 4:]
                .groupby("year")
                .sum()
               ).loc[x, genre_rank]


#test
print(genre_groups)
#df1.to_csv('cleanedMovieData.csv', index=False)
#print(df1.head())
#print(df1.info())



