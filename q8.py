import pandas as pd
df = pd.read_csv("./urls.csv")
for i in range(df.shape[0]):
  start = df.iloc[i,1].find("/")
  end = df.iloc[i,1].rfind("<")
  df.iloc[i,1] =df.iloc[i,1][start+2:end]
df