import pandas as pd
df = pd.read_csv("./drive/My Drive/urls - Sheet1.csv")
for i in range(df.shape[0]):
  start = df.iloc[i,1].find("/")
  end = df.iloc[i,1].rfind("<")
  print(start,end)
  df.iloc[i,1] =df.iloc[i,1][start+2:end]
df