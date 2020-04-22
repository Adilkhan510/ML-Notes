import numpy as np

#numpy arrays are just like python lists with added features
#use np.array(arr,dtype=np.float32)

list1 = [1,2,3,4,5,6]
arr= np.array([[2,3,4],[3,4,5]],dtype=np.float32)
print(repr(arr))

#dtype keyword argument takes in a numpy type and manually casts the array to the specified type.

#when the array has mixed types the type will be upcast to the highest level.

#Copying numpy Arrays 
#-Similar to python lists, making a refrence doesn't make a copy of the array.
#-use np.array().copy() function to get around this
#-Now we can manipulate the list without messing up the original arrray.

#Casting Numpy arrays:
#-use the astype() to change it
arr.astype(np.float32)
#-astype is a function.

#NaN
#--Useful when we want to hold a space in a array without giving it value.

arr3 = [1,23,4,5,5,5,np.nan,]

print(arr3)


# --------------NUMPY BASICS---------

#---Performing basic operations to create and modify numpy arrays.

#Ranged Data:
#-use np.arange(5) to create a numpy array with 5 elements

arr4 = np.arange(2.1,5.1,2)
print(arr4)

#-np.linspace

arr5 = np.linspace(1,99.5,num=50)
print(arr5)

#--------Reshaping Data-----

#-Use np.reshape 
#--takes in an array and a new shape as the required arguments.
#--Reshaped array must contain exactly the same amunt of elements.
arr = np.arange(8)

reshaped_arr = np.reshape(arr, (2, 4))
print(repr(reshaped_arr))
print('New shape: {}'.format(reshaped_arr.shape))

reshaped_arr = np.reshape(arr, (-1, 2, 2))
print(repr(reshaped_arr))
print('New shape: {}'.format(reshaped_arr.shape))