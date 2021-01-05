# Please do not modify
import requests
import json

def verify_predictions(y_pred):
    
    url = "https://q7wmplg8u6.execute-api.ap-northeast-1.amazonaws.com/dev"
    
    payload = {
        "submission": y_pred
    }
    response = requests.request("POST", url,data=json.dumps(payload),headers = {'content-type': 'application/json'})
    
    return response.text

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# loading the datasets
df = pd.read_csv('Japan_cities_rainfall.csv')
df_to_predict = pd.read_csv('rainfall_to_predict.csv')
y_train=list(df["rainfall"])
#y_train=[int(i) for i in y_train]
longitude= list(df["longitude"])
latitude= list(df["latitude"])
date_time= list(df["date_time"])
x_train= np.empty([19976, 3])
for i in range(len(date_time)):
    temp = date_time[i].split('_')
    temp1 = temp[0]+temp[1];
    date_time[i]= int(temp1)/1000;
    x_train[i][0]= (date_time[i]-20200900000)/(20201231000-20200900000)
    x_train[i][1]= (longitude[i]-127.0)/(141.0-127.0)
    x_train[i][2]= (latitude[i]-26.0)/(39.0-26.0)

linRegr = LinearRegression()

linRegr.fit(x_train, y_train)

y_pred=[]
longitude_test= list(df_to_predict["longitude"])
latitude_test= list(df_to_predict["latitude"])
date_time_test= list(df_to_predict["date_time"])
x_test= np.empty([len(longitude_test), 3])
for i in range(len(date_time_test)):
    temp = date_time_test[i].split('_')
    temp1 = temp[0]+temp[1];
    date_time_test[i]= int(temp1)/1000;
    x_test[i][0]= (date_time_test[i]-20200900000)/(20201231000-20200900000)
    x_test[i][1]= (longitude_test[i]-127.0)/(141.0-127.0)
    x_test[i][2]= (latitude_test[i]-26.0)/(39.0-26.0)
    y_pred.append(linRegr.predict(x_test[i].reshape(1,3))[0])
#import pandas as pd
#y_pred= pd.Series(y_pred).to_json(orient='values') 
filename = 'finalized_model.sav'
pickle.dump(linRegr, open(filename, 'wb'))

y_predi = [0]*len(date_time_test)
for i in range(len(y_predi)):
    y_predi[i]=y_pred[i]

result_rmse= verify_predictions(y_predi)
print(result_rmse)
