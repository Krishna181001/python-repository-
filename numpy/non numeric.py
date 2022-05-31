import numpy as np
  

n_arr = np.array([[10.5, 22.5, 3.8],
                  [41, np.nan, np.nan]])
  
print("Given array:")
print(n_arr)
  
print("\nRemove all rows containing non-numeric elements")
print(n_arr[~np.isnan(n_arr).any(axis=1)])
