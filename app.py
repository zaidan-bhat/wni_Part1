import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('finalized_model.sav', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    features = [x for x in request.form.values()]
    a= np.zeros(3);
    a[0]= (int(features[1])/1000.0-20200900000)/(20201231000-20200900000)
    if features[0].lower()=="tokyo":
        a[1]=0.910
        a[2]=0.745
    elif features[0].lower()=="naha":
        a[1]=0.0485
        a[2]=0.0153
    elif features[0].lower()=="fukuoka": 
        a[1]=0.241
        a[2]=0.583
    elif features[0].lower()=="sendai": 
        a[1]=0.992
        a[2]=0.943
    elif features[0].lower()=="osaka": 
        a[1]=0.607
        a[2]=0.667
    elif features[0].lower()=="nigata": 
        a[1]=0.8578
        a[2]=0.914
            
        
    #final_features = [np.array(a)]
    prediction = model.predict(a.reshape(1,3))[0]


    #output = round(prediction[0], 2)
    output= prediction

    return render_template('index.html', prediction_text='Predicted rain(予想される雨は): {}'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    features = list(data.values())
    a= np.zeros(3);
    a[0]= (int(features[1])/1000.0-20200900000)/(20201231000-20200900000)
    if features[0].lower()=="tokyo":
        a[1]=0.910
        a[2]=0.745
    elif features[0].lower()=="naha":
        a[1]=0.0485
        a[2]=0.0153
    elif features[0].lower()=="fukuoka": 
        a[1]=0.241
        a[2]=0.583
    elif features[0].lower()=="sendai": 
        a[1]=0.992
        a[2]=0.943
    elif features[0].lower()=="osaka": 
        a[1]=0.607
        a[2]=0.667
    elif features[0].lower()=="nigata": 
        a[1]=0.8578
        a[2]=0.914
    prediction = model.predict(a.reshape(1,3))
    
    output = prediction[0]
    res= {"Place": features[0],"rainfall": output}
    return res

if __name__ == "__main__":
    app.run(debug=True)
