import pandas as pd

df = pd.read_csv('ESG_sustainability_scores.csv')

name_df = df["Company Name"]
score = df["Overall ESG SCORE"]

print(name_df)
print(score)

input = 'mixi, Inc'

idx = df[name_df == input].index.tolist()
date = df.get_value(idx[0], "Overall ESG SCORE")

print(date)