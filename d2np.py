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
arr11 = np.arange(8)

reshaped_arr = np.reshape(arr11, (2, 4))
print(repr(reshaped_arr))
print('New shape: {}'.format(reshaped_arr.shape))

reshaped_arr = np.reshape(arr11, (-1, 2, 2))
print(repr(reshaped_arr))
print('New shape: {}'.format(reshaped_arr.shape))

#----To flatten an array :
#- arr= np.array()
#- arr.flatten()

#--------Transposing Data : 
#-Use this to transpose the data into the proper format.

#-----Zeros and Ones 
#- np.zeros(4) <---- describes the shape of the array
#- np.zeros_like(arr) <--- creates an array with zeros like arr


#------------------Numpy MATH-------------#
#Goals for this section
# -- Learn how to perform math operations in numpy
# -- Write code using Numpy math functions

#Arithmetic:
arr111 = np.array([[1, 2], [3, 4]])
# Add 1 to element values
print(repr(arr + 1))
# Subtract element values by 1.2
print(repr(arr - 1.2))
# Double element values
print(repr(arr * 2))
# Halve element values
print(repr(arr / 2))
# Integer division (half)
print(repr(arr // 2))
# Square element values
print(repr(arr**2))
# Square root element values
print(repr(arr**0.5))


#Convert Farenheit to celsius : 
def f2c(temps):
    return (5/9)*(temps-32)
fahrenheits = np.array([32,-4,14,-40])
celsius = f2c(fahrenheits)
print(f"celcius {celsius}")

#--- Performing arithmetic doesn't change the original array it simply creates a new one.

#--- non-linear functions:
#-

#How to generate random numbers and arrays from different random distribution.

#A. Random Integers 
#- np.random.randint()
print(np.random.randint(5))

#------ Indexing : 
# - Accessing numpy arrays are very similar to python lists. 
#-- to access sub arrays = arr[index of sub array]

# ------Slicing in Numpy ------



#----Filtering Data in Numpy 

#To filter thru arrays we use the logical operators.
##-- can filter np.nan so use np.isnan to filter the location of the np.nan 


#-----FILTERING IN NUMPY -------#

# np.where  function : 
#- takes in a required first argument which is a boolean array.
#-- True represents the locations of hte elements we want to filter.
#-- returns a tuple of 1D arrays when only 1 argument is given.


#---------------------------Statistics in NUMPY--#
#- It is useful to analyze data for its trends. 
print(arr.min()) # 
#-alerts us to extreme outliers in the data.
#-axis=0 <--- for column axis=1 <---- for rows.

#Statistical metrics in Numpy
#--np.mean(data), np.var(data), np.median(data) to find variance in the data.
#- the np.mean take in a data which is a numpy array as arguments

#------------Aggregation in Numpy----#
# - To get the sum individual values in an array we use np.sum(arr)
# - To get the sum of each column use np.sum(arr,axis=0)
# - To get the sum of each row use np.sum(arr,axis=1)

# ---Cumalative Sums in Numpy --> np.cumsum
# - returns an array with cumaltive sums. 
# - if the axis is not specified then it will return a flattened arrray.
# - setting axis =0 operates on the columns 
# - setting axis = 1 operates on the rows.

#Concatenation 
# - np.concatenate([data1,data2], axis=1)
