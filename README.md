<h1>WNI_Project(Rainfall Prediction)

<h4>This is a linear regression model, I have performed min-max normalization on the input attributes(X_train and X_test). 
I extracted the columns from the dataframe because verify_prediction method was not accepting ndarrays an inputs. So I changed to the format used
in the sample code by initializing the y_pred array in the same manner and then populating it with the predicted values.
  <br>
  <br>
  
 
 <h3>To train the model and see results on test data do "$ python3 model.py" in terminal after navigating to the directory
  
  
 <h1> Update 1
  <br>
  <br>
  <h4>Added simple webapp made with the flask framework 
  <br>
   <br> 
  Please note that this webapp is not yet error proof and only works for a specific input format. Support for other formats will be added soon.
  <br>
  To run the app change navigate to this directory and run "$ python3 app.py"
  <br>
  This will start the server and give you a local url, open the url in your web browser;
  <br>
  Enter name of city LOWERCASE ONLY.
  <br>
  Enter date_time in the format "YYYYMMDDHHMMSS"
  <br>
    <br>
  <h1> Update 2
  <br>
  <br>
  <h4>Added functionality for curl command 
  <br>
   <br> 
   Enter the curl command in the following format: " curl -X POST -H "Content-Type: application/json" -d '{"place":"tokyo", "datetime":20200918080000}' http://127.0.0.1:5000/results "
  <br>
    You should get a result in the following format: <br>
    {
    "Place": "tokyo", 
    "rainfall": 0.31246800953051446
    }
<br>
  Enter date_time in the format "YYYYMMDDHHMMSS"  
    <br>
    <br>
      <h1> Update 3
  <br>
  <br>
  <h4>Added Validation for date and City name
  <br>
   <br> 
   Now the app should output "Invalid date" if an invalid date is entered and "Invalid city" if name of a city not in the dataset is entered.
    Also now the inptut city name can be written in both lower and upper case. Valid dates range from 1st Sept 2020 to 24th Feb 2021. 
  
<br>
  Enter date_time in the format "YYYYMMDDHHMMSS"  
    
  
