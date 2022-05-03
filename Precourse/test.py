import numpy as np
import pandas as pd

np_arr = np.array([[1,2,3], [2,3,4], [4,5,6], [5,6,7]])
pd_arr = pd.DataFrame(np_arr)

print(pd_arr)
print()

pd_means = pd_arr.mean()
list_means = pd_means.values.tolist()

print(pd_means)
print(type(pd_means))
print()

print(list_means)