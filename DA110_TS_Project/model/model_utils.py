
import pickle
from app.config import GOOGLE_DRIVE_LINKS_MODEL
from data.data_utils import download_files


def load_model(path):

    file_path = f'{path}trained_model.pkl'

    download_files(file_path, GOOGLE_DRIVE_LINKS_MODEL['xgboost_model'])

    #open model with pickle
    with open(file_path, 'rb') as f:
        xgboost_model = pickle.load(f)

    return xgboost_model


def make_prediction(model, input_data):

    #drop date column since its not needed
    input_data = input_data.drop('date', axis=1)

    #drop unit_sales
    input_data = input_data.drop('unit_sales', axis=1)

    #make prediction with preprocessed data set
    prediction = model.predict(input_data)

    return prediction