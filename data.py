from sklearn.preprocessing import LabelEncoder
import pandas as pd
df=pd.read_csv("data.csv")
df_label= df.copy()
le= LabelEncoder()
df_label['Gender_Encoded']=le.fit_transform(df_label['Gender'])
df_label['passed_encoded']=le.fit_transform(df_label['passed'])
print('\n Label encoded data')
print(df_label[['Name','Gender','Gender_Encoded','passed','passed_encoded']])
df_encoded=pd.get_dummies(df_label, columns=['City'])
print('\n One-hot encoded data(City)')
print(df_encoded)