# filtering means selecting elements from array that matches the condition
import numpy as np
ages= np.array([[21,16,17,19,20,18,76],[39,22,15,14,18,19,34]])
teens=ages[ages<18]
seniors=ages[ages>60]
print(f"teens ages are : {teens}")
print(f"senior citizen ages are : {seniors}")
adults=np.where(ages>=18,ages,0) #prints 0 for age <18
print(adults)
# it can be done otherwise as : (here using boolean indexing)
ages[ages<18]=0
print(ages)