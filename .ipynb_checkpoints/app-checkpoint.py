from flask import Flask, render_template, request, redirect,url_for,jsonify
import pickle
import numpy as np
app = Flask(__name__)
with open('LinearRegression.pkl', 'rb') as f:
    LinearRegressionModel = pickle.load(f)

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = LinearRegressionModel.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='House price should be $ {}'.format(output))


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('page404.html'), 404


@app.route('/predict',methods=['GET'])
def pred():
    return redirect(url_for('Home'))

if __name__=="__main__":
    app.run(debug=True)

