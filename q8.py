import pandas as pd
df = pd.read_csv("./urls.csv")
df_final = df;
for i in range(df_final.shape[0]):
  start = df_final.iloc[i,1].find("/")
  end = df_final.iloc[i,1].rfind("<")
  df.iloc[i,1] =df.iloc[i,1][start+2:end]
df_final