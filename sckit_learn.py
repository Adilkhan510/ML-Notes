# -----------This section is all about Data Standardization---#
# -----Why standard data format?
# -----data can contain all sorts of different values. Converting data to the same format will make it easier to interpret that data.


# scikit-learn data preprocessing module.
# -- sklearn.preprocessing.
# -- scale module

from sklearn.preprocessing import scale, MinMaxScaler
# scale allows us to standardize our data to a given axis of a NumPy array.
arr = [[2100,   10,  800],
       [2500,   11,  850],
       [1800,   10,  760],
       [2000,   12,  800],
       [2300,   11,  810]]
data_standardized = scale(arr)
print(f"standardizes the data = {data_standardized}")

#function for standardizing data:
def standardize_data(data):
  scaled_data = scale(data);
  return scaled_data

#-------Data Range-----#
#- Another way to standardize data.
#- MinMaxScalar transformer performs range

data1 = [[500,0],[0,0],[500,1],[1,0],[1,2]]
default_scaler = MinMaxScaler()
scaled = default_scaler.fit_transform(data1)
print(f'scaled data: {scaled}')

scale_2 = default_scaler.fit(data1)
transformed_data = default_scaler.transform(data1)

print(f"new scaled data {transformed_data}",f"transformed data : {transformed_data}")