import numpy as np
import pandas as pd
df = pd.read_csv("./country_vaccination_stats.csv")
for i in range(df.shape[0]):
  if(np.isnan(df.iloc[i,2])):
    temp = df[df['country'] == df.iloc[i,0]]
    df.iloc[i,2] = temp['daily_vaccinations'].min()
df['daily_vaccinations'] = df['daily_vaccinations'].fillna(0)