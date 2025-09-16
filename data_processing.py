import pandas as pd 
dataset= pd.read_csv("data.csv")
dataset.head(3)
en_data= dataset[["gender","married"]]
en_data
# pd.get_dummies()
