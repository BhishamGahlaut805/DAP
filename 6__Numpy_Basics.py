#1.Basic of Numpy
#2.Copy in Numpy
#3.View in Numpy
#4.Dtype in Numpy
#5.Stacking in Numpy

#1.Basics of numpy
import numpy as np

arr1=np.array([10,20,30,40,50,60])
print("Numpy array : ",arr1)

arr2=np.array([[1,2],[3,4]])
print("2D array : ",arr2)

print("Shape of Array 1: ",arr1.shape)
print("Shape of Array 2: ",arr2.shape)

#Array dimensions
print("Dimensions array1 : ",arr1.ndim)
print("dimensions array2 : ",arr2.ndim)

#Data Type
print("DataType Array1 : ",arr1.dtype)
print("DataType Array2 : ",arr2.dtype)

#Array Size
print("Size of Array 1 : ",arr1.size)
print("Size of Arr2 : ",arr2.size)

#Numpy array of all Zeros
arr18=np.zeros((3,3),dtype=np.int32)
print("Array of 3*3 all Zeros using Numpy : ", arr18)

#Reshape arrays
arr19=arr1.reshape(2,3)
print("Array 1 reshaped into 2*3 : ",arr19)

#Flatten array2
arr20=arr2.flatten()
print("Flattened array 2 : ",arr20)

#Indexing
arr22=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Array1[2] : ",arr1[2])
print("Array2[1][2] : ",arr22[1][2])

#Slicing
print("Array 1 from 1 to 3 : ",arr1[1:5])

#min,max,sum,average
arr24=np.array([34,67,43,89,21,56,32,78,13,78,32])
print("minimum : ",arr24.min())
print("maximum : ",arr24.max())
print("Sum of elements : ",arr24.sum())
print("Mean of elements : ",arr24.mean())


#2.Copy array in Numpy
arr3=np.array([3,9,1,5,7,8])
arr4=arr3.copy()

print("Copy of array : ",arr4)
print("Original array : ",arr3)
arr3[0]=20
print("Copied array4-> Completely independent from parent from where it is copied : ",arr4)

#3.View in Numpy
arr5=np.array([92,21,24,50,12])
arr6_View= arr5.view()

print("Original array : ",arr5)
print("Viewed array : ",arr6_View)

arr5[2]=100
print("Array viewed -> changed -> Because of shared memory : ",arr6_View)

#4.Data Type in Numpy

arr7=np.array([9,8,7,6,5,4],dtype=np.int64)
print("Integer array : ",arr7)
print("Data Type : ",arr7.dtype)

#uint array
arr8=np.array([5,4,6,3,7,2],dtype=np.uint16)
print("Unsigned Integer array : ",arr8)
print("Data Type : ",arr8.dtype)

#float array
arr9=np.array([5,4.8,6.4,3.9,7.6,2.7],dtype=np.float32)
print("Float array : ",arr9)
print("Data Type : ",arr9.dtype)

#Complex array
arr10=np.array([1+3j,4+8j,3+3j,8+4J],dtype=np.complex64)
print("Complex array : ",arr10)
print("Data Type : ",arr10.dtype)

#Boolean array
#uint array
arr11=np.array([True,False,True,False],dtype=np.bool)
print("Unsigned Integer array : ",arr11)
print("Data Type : ",arr11.dtype)


#5.Stacking in Numpy
arr12=np.array([[1,2,3,4,5,6,7,8,9],[10,20,30,40,50,60,70,80,90]])
arr13=np.array([[9,8,7,6,5,4,3,2,1],[90,80,70,60,50,40,30,20,10]])

#stack() -> adds new axis
arr14=np.stack((arr12,arr13))
print("Stacked array -> stack() ",arr14)
print("Shape of array stacked : ",arr14.shape)

#Vstack->vertical stack(row-wise)
arr15=np.vstack((arr12,arr13))
print("Stacked array -> Vertical stack() ",arr15)
print("Shape of array vstacked : ",arr15.shape)

#Hstack -> horizontal stack(Column-wise)
arr16=np.hstack((arr12,arr13))
print("Stacked array -> Horizontal stack() ",arr16)
print("Shape of array hstacked : ",arr16.shape)

#Dstack-> depth stacking
arr17=np.dstack((arr12,arr13))
print("Stacked array -> depth stack() ",arr17)
print("Shape of array vstacked : ",arr17.shape)

'''
Outputs:
Numpy array :  [10 20 30 40 50 60]
2D array :  [[1 2]
 [3 4]]
Shape of Array 1:  (6,)
Shape of Array 2:  (2, 2)
Dimensions array1 :  1
dimensions array2 :  2
DataType Array1 :  int64
DataType Array2 :  int64
Size of Array 1 :  6
Size of Arr2 :  4
Array of 3*3 all Zeros using Numpy :  [[0 0 0]
 [0 0 0]
 [0 0 0]]
Array 1 reshaped into 2*3 :  [[10 20 30]
 [40 50 60]]
Flattened array 2 :  [1 2 3 4]
Array1[2] :  30
Array2[1][2] :  6
Array 1 from 1 to 3 :  [20 30 40 50]
minimum :  13
maximum :  89
Sum of elements :  543
Mean of elements :  49.36363636363637
Copy of array :  [3 9 1 5 7 8]
Original array :  [3 9 1 5 7 8]
Copied array4-> Completely independent from parent from where it is copied :  [3 9 1 5 7 8]
Original array :  [92 21 24 50 12]
Viewed array :  [92 21 24 50 12]
Array viewed -> changed -> Because of shared memory :  [ 92  21 100  50  12]
Integer array :  [9 8 7 6 5 4]
Data Type :  int64
Unsigned Integer array :  [5 4 6 3 7 2]
Data Type :  uint16
Float array :  [5.  4.8 6.4 3.9 7.6 2.7]
Data Type :  float32
Complex array :  [1.+3.j 4.+8.j 3.+3.j 8.+4.j]
Data Type :  complex64
Unsigned Integer array :  [ True False  True False]
Data Type :  bool
Stacked array -> stack()  [[[ 1  2  3  4  5  6  7  8  9]
  [10 20 30 40 50 60 70 80 90]]

 [[ 9  8  7  6  5  4  3  2  1]
  [90 80 70 60 50 40 30 20 10]]]
Shape of array stacked :  (2, 2, 9)
Stacked array -> Vertical stack()  [[ 1  2  3  4  5  6  7  8  9]
 [10 20 30 40 50 60 70 80 90]
 [ 9  8  7  6  5  4  3  2  1]
 [90 80 70 60 50 40 30 20 10]]
Shape of array vstacked :  (4, 9)
Stacked array -> Horizontal stack()  [[ 1  2  3  4  5  6  7  8  9  9  8  7  6  5  4  3  2  1]
 [10 20 30 40 50 60 70 80 90 90 80 70 60 50 40 30 20 10]]
Shape of array hstacked :  (2, 18)
Stacked array -> depth stack()  [[[ 1  9]
  [ 2  8]
  [ 3  7]
  [ 4  6]
  [ 5  5]
  [ 6  4]
  [ 7  3]
  [ 8  2]
  [ 9  1]]

 [[10 90]
  [20 80]
  [30 70]
  [40 60]
  [50 50]
  [60 40]
  [70 30]
  [80 20]
  [90 10]]]
Shape of array vstacked :  (2, 9, 2)
'''