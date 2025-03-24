
import pandas as pd
import gdown
import os
from app.config import GOOGLE_DRIVE_LINKS


def download_files(file_path, url):

    # Check if the file already exists locally
    if not os.path.exists(file_path):
        # If it doesn't exist, download the file from Google Drive using gdown
        gdown.download(url, file_path, quiet=False)
    else:
        # If the file already exists, print a message
        print(f"{file_path} already exists.")


def load_data(path):

    # define file path
    file_path = f"{path}prepared.csv"

    #download dataset
    download_files(file_path, GOOGLE_DRIVE_LINKS['prepared'])

    #store csv in DataFrame
    dataset = pd.read_csv(file_path)

    return dataset


def preprocess_input_data(selected_store, selected_item, selected_date, dataset):

    #converting date column to datetime
    dataset['date'] = pd.to_datetime(dataset['date'])

    #drop unnecessary columns
    dataset2 = dataset.drop(['id', 'onpromotion'], axis=1, inplace=False)

    # creating features based on lags
    dataset2['lag_1'] = dataset2['unit_sales'].shift(1)
    dataset2['lag_7'] = dataset2['unit_sales'].shift(7)
    dataset2['lag_30'] = dataset2['unit_sales'].shift(30)

    # creating rolling and expanding mean windows
    dataset2['rolling_mean_7'] = dataset2['unit_sales'].rolling(window=7).mean()
    dataset2['expanding_mean'] = dataset2['unit_sales'].expanding().mean()

    dataset3 = dataset2.dropna() #dropping resulting nan

    #splitting according to the selected date, keeping everything on and after that date
    dataset_splitted = dataset3[dataset2['date'] >= selected_date]

    #filtering for the requested store and item
    dataset_filtered = dataset_splitted[(
            dataset_splitted['store_nbr'] == selected_store)
            & (dataset_splitted['item_nbr'] == selected_item)
        ]

    return dataset_filtered