from flask import Flask, request, render_template
import numpy as np
import pickle
import math

app = Flask(__name__)



# Filename='uber_rides.sav'
Filename='model.pkl'


try:

    model=pickle.load(open(Filename,'rb'))
    print("model loaded")
except:
    print("error has occured")




@app.route('/')

def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    int_features  = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0],2)
    return render_template('index.html',prediction_text="Number of Weekly Rides Should be {}".format(math.floor(output)))


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)