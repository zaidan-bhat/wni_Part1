<h1>wni_Part1

<p>This is a linear regression model, I have performed min-max normalization on the input attributes(X_train and X_test). 
I extracted the columns from the dataframe because verify_prediction method was not accepting ndarrays an inputs. So I changed to the format used
in the sample code by initializing the y_pred array in the same manner and then populating it with the predicted values.
  <br>
  <br>
  
 
 <h3>To train the model and see results on test data do "$ python3 model.py" in terminal after navigating to the directory
  
  
 <h1> Update
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
  
