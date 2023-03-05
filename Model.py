import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

movie_ids_titles= pd.read_csv("movies.csv")

movie_ids_ratings=pd.read_csv("ratings.csv")

movie_ids_titles.drop(["genres"],inplace=True,axis=1)

movie_ids_ratings.drop(["timestamp"],inplace=True, axis=1)

merged_movie_df= pd.merge(movie_ids_ratings, movie_ids_titles, on='movieId')

print(merged_movie_df.groupby('title').describe())

print(merged_movie_df.groupby('title')['rating'].mean().head())

merged_movie_df.groupby('title')['rating'].mean().sort_values(ascending=False).head()

merged_movie_df.groupby('title')['rating'].count().sort_values(ascending=False).head()

movie_rating_mean_count=pd.DataFrame(columns=['rating_mean','rating_count'])

movie_rating_mean_count["rating_mean"]=merged_movie_df.groupby('title')['rating'].mean()

movie_rating_mean_count["rating_count"]=merged_movie_df.groupby('title')['rating'].count()

plt.figure(figsize=(10,8))
sns.set_style("darkgrid")

movie_rating_mean_count['rating_mean'].hist(bins=30,color='purple')

plt.figure(figsize=(10,8))
sns.set_style("darkgrid")

movie_rating_mean_count["rating_count"].hist(bins=33,color="blue")

print(plt.figure(figsize=(10,8)))

sns.set_style("darkgrid")

sns.regplot(x="rating_mean",y="rating_count", data= movie_rating_mean_count, color="brown")

movie_rating_mean_count.sort_values("rating_count",ascending=False).head()

user_movie_rating_matrix= merged_movie_df.pivot_table(index="userId",columns="title",values="rating")

import warnings
warnings.filterwarnings("ignore")

pulp_fiction_ratings= user_movie_rating_matrix["Pulp Fiction (1994)"]

pulp_fiction_correlations= pd.DataFrame(user_movie_rating_matrix.corrwith(pulp_fiction_ratings),columns=["pf_corr"])

print(pulp_fiction_correlations.sort_values("pf_corr",ascending=False).head(5))

pulp_fiction_correlations= pulp_fiction_correlations.join(movie_rating_mean_count["rating_count"])

pulp_fiction_correlations.dropna(inplace=False)

print(pulp_fiction_correlations.sort_values("pf_corr",ascending=False).head(5))