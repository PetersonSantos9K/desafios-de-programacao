import pandas as pd
import seaborn as sns

df = pd.read_csv("books.csv", sep=",", on_bad_lines="skip")
df.drop(df[df.ratings_count == 0].index, inplace=True)
df.drop_duplicates()

most_rated = df.sort_values('ratings_count', ascending=False)



print(
sns.barplot(x=most_rated.head(10).ratings_count, y=most_rated.head(10).title))
print(most_rated.head(10).average_rating.mean())


print(
df[df.average_rating>4.9].sort_values('ratings_count', ascending=False).head(10))