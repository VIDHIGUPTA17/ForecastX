from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

# Load model and encoders
model = pickle.load(open("model.pkl", "rb"))
le_store = pickle.load(open("le_store.pkl", "rb"))
le_family = pickle.load(open("le_family.pkl", "rb"))
train_X = pickle.load(open("train_X.pkl", "rb"))

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def predict():
    prediction = None
    if request.method == 'POST':
        store_nbr = int(request.form['store_nbr'])
        family = request.form['family']
        onpromotion = int(request.form['onpromotion'])
        oil = float(request.form['dcoilwtico'])
        transactions = int(request.form['transactions'])
        weekday = int(request.form['weekday'])
        lag_1 = float(request.form['lag_1'])
        rolling_mean_7 = float(request.form['rolling_mean_7'])

        row = pd.DataFrame(np.zeros((1, train_X.shape[1])), columns=train_X.columns)
        row['store_nbr'] = le_store.transform([store_nbr])[0]
        row['family'] = le_family.transform([family])[0]
        row['onpromotion'] = onpromotion
        row['dcoilwtico'] = oil
        row['transactions'] = transactions
        row['weekday'] = weekday
        row['is_weekend'] = int(weekday in [5, 6])
        row['lag_1'] = lag_1
        row['rolling_mean_7'] = rolling_mean_7

        prediction = model.predict(row)[0]
    
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
