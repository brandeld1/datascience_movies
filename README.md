# Popularity and Ratings of Movie Genres

## CLEANING

### project.py contains the data cleaning code, the input file used was too large to be uploaded to the github. The output file generated is cleanedMovieData.csv, which contains all the tags. cleanedMovieData2.csv contains the implemented sentiment calculator which replaces the tags with just a number representing if the tags were generally positive or negative.

#

## MAP REDUCE

### MR1, MR2, and MR3 contain the mapreduce code which was ran in hadoop. MR1, MR2, and MR3 output files with the key being year,genre. MR1 outputs a file with the value being the count, MR2 outputs a file with the value being the average sentiment, and MR3 outpust a file with the value being the average rating.

#

## MACHINE LEARNING ALGORITHM

### mlalg.py contains the code for the machine learning algorithm that was used on our cleaned data. The input file used is the combinedMRData.csv which contains the outputs from MR1, MR2, and MR3 combined based on year.

#

## DATA VISUALIZATIONS

### yeargenre_rating.xlsx contains the data visuals with further cleaned data from the mapreduce. The files are highest_count_genre_per_year.csv, highest_rated_genre_per_year.csv, and highest_sentiment_genre_per_year.csv.
