
import streamlit as st
import pandas as pd
import datetime as dt
from data.data_utils import load_data, preprocess_input_data
from app.config import DATA_PATH, MODEL_PATH
from model.model_utils import make_prediction, load_model


def main():

    st.title('Test Title')

    #Selectable store and item numbers
    store_numbers = [26, 39, 36, 34, 28, 24, 30 ,32, 35, 51, 27]
    item_numbers = [257847, 839362, 215352, 315176, 364606]

    #create input sidebar
    st.sidebar.header('Select properties') #header
    selected_store = st.sidebar.selectbox('Store Number', store_numbers) #store selection
    selected_item = st.sidebar.selectbox('Item Number', item_numbers) #item selection

    #create date range to select from
    min_date = dt.date(2014,1,1)
    max_date = dt.date(2014,3,31)
    default_date = dt.date(2014,1,15)

    date = st.date_input("Forecast Date", value=default_date, min_value=min_date, max_value=max_date)

    #load the data
    dataset = load_data(DATA_PATH)

    #load the model
    model = load_model(MODEL_PATH)

    #display line chart
    selected_data = dataset[
                            (dataset['store_nbr'] == selected_store)
                        & (dataset['item_nbr'] == selected_item)
                        & (dataset['date'] < date)
        ]

    st.line_chart(selected_data['unit_sales'])

    #create button for users to get forecast
    if st.button('Get forecast!'):
        #preprocess data
        input_data = preprocess_input_data(selected_store, selected_item, date, dataset)
        #predict data
        prediction = make_prediction(model, input_data)

        #print resulting prediction
        st.write(f"Predicted Sales for {date}: {prediction[0]}")


if __name__ == "__main__":
    main()