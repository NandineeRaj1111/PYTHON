import matplotlib.pyplot as plt

# simple line plot
x=[1,2,3,4,5,6]
y=[3,5,7,9,11,13]
plt.plot(x,y,marker='o',color='red',linestyle='--')
plt.title("LINE PLOT EXAMPLE")
plt.xlabel("X AXIS")
plt.ylabel("Y AXIS")
plt.show()

# bar chart
cat=["A","B","C","D"]
val=[4,7,1,8]
plt.bar(cat,val,color='blue')
plt.title("BAR CHART EXAMPLE")
plt.show()

# scatter plot
x=[5,7,8,7,6,9,6,5,7,8]
y=[99,87,100,67,78,87,94,103,68,88]
plt.scatter(x,y,color='orange')
plt.title("SCATTER PLOT EXAMPLE")
plt.show()
