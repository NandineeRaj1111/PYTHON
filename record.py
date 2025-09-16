import pandas as pd 
data ={
    "name":["Harshit","Ayushman","Satyam"],
    "stat":["f","bff","of"],
    "imp":[8,9,7]
}
df=pd.DataFrame(data)
print(df)
print()
df["rate"]=[6,8,6.5]
print(df)