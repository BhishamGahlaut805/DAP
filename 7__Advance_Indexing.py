#Advance indexing

import numpy as np

arr=np.array([98,23,21,29,87,67])
result=arr[[0,2,4]]
print(result)

arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
rows=[0,1,2]
cols=[2,1,0]
result1=arr1[rows,cols]
print(result1)

#Boolean Indexing
arr3=np.array([10,25,54,12,29])
result3=arr3[arr3>25]
print(result3)


result4=arr1[arr1%2==0]
print(result4)

'''
PS C:\Users\CC06\Desktop\world count> & C:/Users/CC06/AppData/Local/Programs/Python/Python312/python.exe "c:/Users/CC06/Desktop/world count/Dap02_04_26.py"
[98 21 87]
[3 5 7]
[54 29]
[2 4 6 8]
'''