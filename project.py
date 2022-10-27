import pandas as pd

#get the datasets
df1 = pd.read_csv("../MovieData/movies.csv")
df2 = pd.read_csv("../MovieData/ratings.csv")
df3 = pd.read_csv("../MovieData/tags.csv")

#remove useless data
df2.drop(['timestamp','userId'], inplace=True, axis=1)
df3.drop(['userId','timestamp'], inplace=True, axis=1)

#combine datasets and remove repitive rows, combine ratings based on mean
df1 = df1.merge(df2, on='movieId')
df1 = df1.groupby(['movieId','title','genres'],as_index=False,sort=False)['rating'].mean()

#combine datasets and combine rows with tags as an array
df3 = df3.groupby('movieId')['tag'].apply(list).reset_index()
df1 = df1.merge(df3, on='movieId')

print(df1.head())

