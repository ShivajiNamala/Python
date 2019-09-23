import numpy as np
#+++++++++++++++++++++++++++++++++++++++++++++++++
#To replace items that satisfy a condition with another value in numpy array.
#1. Replace all odd numbers by -1.
#input
arr1 = np.array([0,1,2,3,4,5,6,7,8,9])
#logic
arr1[arr1 % 2 == 1] = -1
print("#1 output")
print(arr1)
#+++++++++++++++++++++++++++++++++++++++++++++++++
#To reshape an array.
#2. Convert 1D Array to 2D Array with 2 rows.
#input
arr2 = np.arange(10)
#logic
arr21 = arr2.reshape((2,-1))
print("#2 output")
print(arr21)
#+++++++++++++++++++++++++++++++++++++++++++++++++
#To generate custom sequences in numpy without hardcoding.
#3. Create the pattern.
#input
arr3 = np.array([1,2,3])
#logic
arr31 = np.append((np.repeat(arr3,3)),(np.tile(arr3,3)))
print("#3 output")
print(arr31)
#+++++++++++++++++++++++++++++++++++++++++++++++++
#To get the common items between two python numpy arrays.
#4. Get the common item between a & b.
#input
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
#logic
c = np.intersect1d(a,b)
print("#4 output")
print(c)
#+++++++++++++++++++++++++++++++++++++++++++++++++
#To get the positions where elements of two arrays match.
#5. Get matched items position.
#input
a1 = np.array([1,2,3,2,3,4,3,4,5,6])
b1 = np.array([7,2,10,2,7,4,9,4,9,8])
#logic
c1 = np.nonzero(np.in1d(a, b))[0]
print("#5 output")
print(c1)
#+++++++++++++++++++++++++++++++++++++++++++++++++
#To create a 2D array containing random floats between 5 and 10.
#6. Create 5X3 array with decimal numbers between 5 and 10.
#input - NA
#logic
arr6 = np.random.uniform(low=5.0, high=10.0, size=(5,3))
print("#6 output")
print(arr6)
#+++++++++++++++++++++++++++++++++++++++++++++++++
#To limit the number of items printed in output of numpy array to 6.
#7. Limit the number of items to print 6.
#input
arr7 = np.arange(15)
#logic
np.set_printoptions(threshold=5)
print("#7 output")
print(arr7)
#+++++++++++++++++++++++++++++++++++++++++++++++++
#To pretty print a numpy array by suppressing the scientific notation.
#8. Suppress and limit the precision to 6 elements.
#input
np.random.seed(100)
rand_arr = np.random.random([3,3])/1e3
#logic
np.set_printoptions(precision=6, suppress=True) 
print("#8 output")
print(rand_arr)
#+++++++++++++++++++++++++++++++++++++++++++++++++
#To swap two columns in a 2d numpy array.
#9. Swap column 1 and 2.
#input
arr9 = np.arange(9).reshape(3,3)
#logic
arr9[:,[0, 1]] = arr9[:,[1, 0]]
print("#9 output")
print(arr9)
#+++++++++++++++++++++++++++++++++++++++++++++++++
#To swap two rows in a 2D numpy array.
#10. Swap rows 1 and 2.
#input
arr10 = np.arange(9).reshape(3,3)
#logic
arr10[[0, 1],:] = arr10[[1, 0],:]
print("#10 output")
print(arr10)
#+++++++++++++++++++++++++++++++++++++++++++++++++
