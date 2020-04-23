# -----------This section is all about Data Standardization---#
# -----Why standard data format?
# -----data can contain all sorts of different values. Converting data to the same format will make it easier to interpret that data.


# scikit-learn data preprocessing module.
# -- sklearn.preprocessing.
# -- scale module

from sklearn.preprocessing import scale, MinMaxScaler, RobustScaler, Normalizer

from sklearn.decomposition import PCA
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

#Robust Scalar : allows us to scale data without being affected by the outliers in the data.
#robust scaling function
def robust_scaling(data):
    robust_scaler = RobustScaler()
    transformed = robust_scaler.fit_transform(data)

#---------normalizing data : 
#- 
def normalize_data(data):
    normalizer = Normalizer()
    transformed_1 = normalizer.fit_transform(data)
    return transformed_1
print(normalize_data(data1))

#--Data Imputation -##
#- we use data imputation to fill some values when the data is missing them.
#----np.nan..
#- SimpleImputer transformer
#--- has 4 methods ..use mean value, median value, most frequent value, constants 
# --- use the strategy="methodnamehere" to fill it 


#------------Principal component Analysis---#
#- useful when merging different similar features. ppg and total points. 
#- also called dimensionality reduction

pca_obj = PCA(n_components=2)
pc = pca_obj.fit_transform(data1).round(3)
print(pc)
