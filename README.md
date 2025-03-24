# Retail Store Demand Forecast
Web-based application to predict unit sales amount for a retail store through machine learning forecasts.

# 🌐Project Overview
- Conducted EDA to gain rudimentary insights about the data
- Preprocessed the data to handle errors and create necessary features
- Trained a Machine Learning model (XGBoost) to forecast sold units for different products
- Created a web-based application with Streamlit to be used by store management for easy demand predictions

# 🗂️The Data
- Used a retail store dataset from kaggle named 'Corporación Favorita Grocery Sales Forecasting'
- Filtered the data to only include one of the many regions called 'Guayas'
- Only used datapoints before April-2014

# 🛠️Pre-Processing 
- Filtered the data according to the requirements
- Assured that the Time Series consisted of equal time steps
- Handled missing and corrupted values
- Created additional features such as 'Weekday', 'Year' and so on

📚All the necessary data is included in the repository and will otherwise be downloaded from Google Drive automatically📚

# 🔑Predicitons
- The XGBoost-Model was trained with data from before 2014 and can now be used to do forecasting for the required time frame
- The Model is included as a pickle file or will be downloaded from Google drive otherwise
- The user of the Streamlit app has to input a date, a store number (pre-selected) and an item number (pre-selected). All other features are created automatically

❗️The app runs locally only

Have fun 🤓
