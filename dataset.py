import seaborn as sb 
import pandas as pd
# titanic dataset load
df=sb.load_dataset("titanic")
print(df.head())
# missing values check
print(df.isnull().sum)