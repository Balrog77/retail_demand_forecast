# Directory paths for data and model files
DATA_PATH = 'data/'
MODEL_PATH = 'model/'

# Google Drive file IDs for each dataset
file_id_for_stores_csv = '1zFhWOsLgkFQ4YYuRo_9frXWAzc9wFPTP'  # ID for stores data CSV
file_id_for_items_csv = '1D4i5rbO7PWRah2ckoZCTz8vgOGFQnSOl'  # ID for items data CSV
file_id_for_train_csv = '1Zmwxp94pAQo58kXmY2q0ysIS1dDAIPz7'  # ID for training data CSV
file_id_for_prepared_csv = '13ArDVTkFuo86LUKpdVECneEFYFPnq3b7'

# Google Drive links for each dataset
GOOGLE_DRIVE_LINKS = {
    "stores": f"https://drive.google.com/uc?id={file_id_for_stores_csv}",  #Link for stores data
    "items": f"https://drive.google.com/uc?id={file_id_for_items_csv}",  #Link for items data
    "train": f"https://drive.google.com/uc?id={file_id_for_train_csv}", #Link for train data
    "prepared": f"https://drive.google.com/uc?id={file_id_for_prepared_csv}" #Link for prepared data
}

# Google Drive link for the model
file_id_for_xgboost_model = "1-17z4rDSH_KLkf9vDRY_mtWXJF1sBNG4"  # ID for the XGBoost model file

# Google Drive link for the model file
GOOGLE_DRIVE_LINKS_MODEL = {
    "xgboost_model": f"https://drive.google.com/uc?id={file_id_for_xgboost_model}"  # Link for the XGBoost model
}


stores_url = 'https://drive.google.com/file/d/1zFhWOsLgkFQ4YYuRo_9frXWAzc9wFPTP/view?usp=sharing'
items_url = 'https://drive.google.com/file/d/1D4i5rbO7PWRah2ckoZCTz8vgOGFQnSOl/view?usp=sharing'
train_url = 'https://drive.google.com/file/d/1Zmwxp94pAQo58kXmY2q0ysIS1dDAIPz7/view?usp=sharing'
prepared_url = 'https://drive.google.com/file/d/13ArDVTkFuo86LUKpdVECneEFYFPnq3b7/view?usp=sharing'