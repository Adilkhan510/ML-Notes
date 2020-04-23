import pandas as pd
#------New section 
# - Notes
# - Notes



#---Data analysis:
# - its good to perform preliminary data analysis.
# - to find the outlier values and figure out which features of the dataset
# - are most important.

#---pandas
# -utilities include parsing multiple file formats to converting entire data table into numpy matrix array


#------Series 

#1-D data 
#- for 1-D data in pandas we use pandas.Series objects
#- created through the pd.Series constructor
#- does not have any arguments.

arr = [1,2,4,5,6,7]

series = pd.Series(arr)

print(repr(series))
#- has a label that can be set
#- pd.Series(arr, )


# 2D data : 
#- main purpose of pandas is to deal with tabular data.
# - tabular data is data that comes from spreadsheets and tables.
# - use pd.DataFrame()

