# 📈 ForecastX – Store Sales Time Series Forecasting

ForecastX is a machine learning-based Flask web application that predicts store sales using historical data. It uses XGBoost and time-series feature engineering to provide custom and test set predictions.

---

## 🗂 Project Structure

ForecastX/
│
├── app.py # Flask application
├── Untitled.ipynb # Jupyter notebook for EDA & model training
├── model.pkl # Trained model
├── le_family.pkl # Label encoder for 'family'
├── le_store.pkl # Label encoder for 'store_nbr'
├── custom_predictions.csv # Output predictions from custom input
├── submission.csv # Output predictions from test set
├── templates/
│ └── index.html # HTML page for the Flask app
│
├── store-sales-time-series-forecasting/
│ ├── train.csv
│ ├── test.csv
│ ├── sample_submission.csv
│ ├── holidays_events.csv
│ ├── oil.csv
│ ├── stores.csv
│ └── transactions.csv
│
└── README.md # You're here!

---

## ⚙️ Features

- 🧠 ML Model: XGBoost Regressor
- 📊 Forecasts sales for future dates using:
  - Transactions
  - Holidays
  - Oil prices
  - Store types and locations
- 🌐 Simple and intuitive Flask web app
- 📤 Upload your own CSV for custom forecasts

---

## 🔧 Installation & Setup

### 1. Clone the Repo

```bash
git clone https://github.com/VIDHIGUPTA17/ForecastX.git
cd ForecastX
2. Install Dependencies
Make sure Python 3.10+ is installed.

```bash
Copy code
pip install -r requirements.txt
If requirements.txt is not available, install manually:

```bash
Copy code
pip install flask pandas numpy xgboost scikit-learn
3. Add train_X.pkl (Important)
Due to GitHub upload limits, train_X.pkl is not included.
You can:

Contact the developer (Vidhi Gupta) to obtain it

Or retrain the model using Untitled.ipynb

Place it in the root folder after obtaining:

Copy code
ForecastX/
├── train_X.pkl  ← Place it here
🚀 Run the Application
bash
Copy code
python app.py
Visit http://127.0.0.1:5000/ in your browser.

📸 Screenshots
Home Page

Add your screenshot here by uploading it to a screenshots/ folder and updating the link above.

🧠 Model Training Workflow
Load and preprocess data (Untitled.ipynb)

Feature engineering: holidays, oil prices, dates, etc.

Label encode categorical variables

Train XGBoost model

Save model & encoders using joblib

Use Flask to take input → process → predict → return result

📂 Dataset Info
All data files used are from the Store Sales - Time Series Forecasting Kaggle competition:

train.csv, test.csv: Sales data

transactions.csv: Daily transactions per store

holidays_events.csv: Holidays and events

oil.csv: Oil prices

stores.csv: Store metadata

🙋‍♀️ Author
Vidhi Gupta
GitHub: @VIDHIGUPTA17

💡 Future Improvements
Add data visualizations on the web app

Add retraining interface for updated data

Deploy on Heroku or Streamlit Cloud

yaml
Copy code

---

## ✅ What You Should Do Now

1. Place this README as `README.md` in the root of your GitHub repo.
2. Create a `screenshots/` folder and upload app screenshots if you want to show UI.
3. If `train_X.pkl` is sensitive or large, provide a **Google Drive link** or ask users to retrain.

Let me know if you want a deployment guide (e.g., Streamlit Cloud, Render, or Hugging
