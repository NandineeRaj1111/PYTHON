import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# histogram for how data is spread
data=[2,4,6,6,8,8,9,10,10,11,11,11,12,13,14,15]
sns.histplot(data, bins=5, kde=True) 
# kde=true means smooth curve
plt.title("HISTOGRAM")
plt.show()

# box plot for extreme values easily visible
sns.boxplot(data=data)
plt.title("BOX PLOT")
plt.show()

# heatmap for relationship between columns and also strength
data=pd.DataFrame({
    "MATH": [99,89,84,78,65],
    "SCI":[99,98,95,92,90],
    "ENG": [98,90,70,65,60]

})
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("HEATMAP PLOT")
plt.show()

