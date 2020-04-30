import numpy as np
#----Data Modeling with sckit-learn
# - main job of a data scientist is to analyze data.
# - -create models for obtaining results from data.
# -# Things to do when creating models: 
# -# 1. figure out the optimal hyperparameters to use.
# -- hyperparameters are values that we set when creating a model. 

#-------------Linear Regression --------#
#- main objectives of machine learning is to find a equation or a curve that fits the data.
#- Finding optimal model is hard so instead we find a approximate distribution. 
#- A Linear model is a combination of the datasets features.
#- linear regression refers to using a linear model to represent a relationship between iv and dv
#- y= ax1 + bx2 + cx3 +d <---formula

#--------------Basic Linear Regression ( least squares regression)---

#- 
dp = np.array([[2100,  800],
                    [2500,  850],
                    [1800,  760],
                    [2000,  800],
                    [2300,  810]])
dpr = np.array([[10.99, 12.5 ,  9.99, 10.99, 11.99]])

from sklearn import linear_model

reg = linear_model.LinearRegression()
#Fit function...
#- takes in dataset of features(columns), idependent variables.
#- we have features(columns) and data points(labels). 

#- also takes in an array of labels(dependent variables)X for each data instance.
data_model = reg.fit(dp, dpr)

#fit function allows us
# --- Predict Function--
new_data=([2000,820],[2200,830])
prediction = reg.predict(new_data)

print(prediction)

#---Is there a need for regularization of linear regression?

#- Regularizatin allows us to block the noise that often accompanies the data.
#- sometimes there can be many attributes that can allow us to create a linear model.
#- use regulariation 