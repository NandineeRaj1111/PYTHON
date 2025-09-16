import pandas as pd 
data = [10,20,30,40]
s= pd.Series(data)
print("series\n",s)
# data frame
data = {
    "name":["NR", "Raj","Amit"],
    "age":[ 19,22,23],
    "branch":["csaiml","it","ece"]
}
df = pd.DataFrame(data)
print("dataframe:\n", df)
print(df.head(2))
print(df["name"])
print(df[["name","branch"]])
print(df[df["age"]>20])
df["marks"]=[100,95,85]
print(df)