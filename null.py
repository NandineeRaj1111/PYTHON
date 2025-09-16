import pandas as pd
data={
    'Name':['NR','AJ','TF'],
    'age':[19,21,None],
    'salary':[300000,50000,None]
    # salary is in $
}
df=pd.DataFrame(data)
print(df)
print(df.isnull().sum())
drop=df.dropna()
print(drop)
df['age'].fillna(df['age'].mean(),inplace=True)
df['salary'].fillna(df['salary'].mean(), inplace=True)
print(df)
