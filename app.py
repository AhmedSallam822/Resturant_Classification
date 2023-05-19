import joblib
import streamlit as st
import pandas as pd
import xgboost
import sklearn

def app():
    model = joblib.load('Final_Model.h5')
    st.set_page_config(page_title=" Resturant Classifier ")
    st.title(" Resturant Classifier on Zomato ")
    st.header(" Epsilon Training Project ")

    st.write("This project predicts Resturant rate based on some features")

    online_order = st.selectbox('Does Online', ['Yes', 'No'])
    book_table	 = st.selectbox('Select Type of body', ['Yes', 'No'])
    votes = st.number_input("Votes 0 - 16832", value=0)
    approx_cost_for_two_people = st.number_input("Cost For Two People 40 - 6000", value=0)
    listed_in_type = st.radio('Select Type of Service', ['Buffet','Cafes','Delivery','Desserts','Dine-out','Drinks & nightlife','Pubs and bars'])
    listed_in_city = st.radio("Select the Country Targeted", ['Banashankari','Bannerghatta Road','Basavanagudi','Bellandur','Brigade Road','Brookefield','BTM','Church Street','Electronic City','Frazer Town','HSR','Indiranagar','Jayanagar','JP Nagar', 'Kalyan Nagar', 'Kammanahalli','Koramangala 4th Block','Koramangala 5th Block','Koramangala 6th Block','Koramangala 7th Block','Lavelle Road','Malleshwaram','Marathahalli','MG Road','New BEL Road','Old Airport Road','Rajajinagar','Residency Road','Sarjapur Road','Whitefield'])
    
    
    
    predict = st.button("Predict")
    if predict:
        df = pd.DataFrame.from_dict(
            {
                'online_order':[0 if online_order == 'No' else 1],
                'book_table':[0 if book_table == 'No' else 1],
                'votes':[votes],
                'approx_cost_for_two_people':[approx_cost_for_two_people],
                'listed_in_type':[0 if listed_in_type == 'Buffet' else (1 if listed_in_type == 'Cafes' else  (2 if listed_in_type == 'Delivery' else  (3 if listed_in_type == 'Desserts' else  (4 if listed_in_type == 'Dine-out' else  (5 if listed_in_type == 'Drinks & nightlife' else  (6 if listed_in_type == 'Pubs and bars' else 7 ))))))],
                'listed_in_city':[0 if listed_in_city == 'Banashankari' else (1 if listed_in_city == 'Bannerghatta Road' else  (2 if listed_in_city == 'Basavanagudi' else  (3 if listed_in_city == 'Bellandur' else  (4 if listed_in_city == 'Brigade Road' else  (5 if listed_in_city == 'Brookefield' else  (6 if listed_in_city == 'BTM' else  (7 if listed_in_city == 'Church Street' else  (8 if listed_in_city == 'Electronic City' else (9 if listed_in_city == 'Frazer Town' else (10 if listed_in_city == 'HSR' else(11 if listed_in_city == 'Indiranagar' else(12 if listed_in_city == 'Jayanagar' else (13 if listed_in_city == 'JP Nagar' else  (14 if listed_in_city == 'Kalyan Nagar' else  (15 if listed_in_city == 'Kammanahalli' else  (16 if listed_in_city == 'Koramangala 4th Block' else  (17 if listed_in_city == 'Koramangala 5th Block' else  (18 if listed_in_city == 'Koramangala 6th Block' else (19 if listed_in_city == 'Koramangala 7th Block' else (20 if listed_in_city == 'Lavelle Road' else  (21 if listed_in_city == 'Malleshwaram' else  (22 if listed_in_city == 'Marathahalli' else  (23 if listed_in_city == 'MG Road' else  (24 if listed_in_city == 'New BEL Road' else  (25 if listed_in_city == 'Old Airport Road' else (26 if listed_in_city == 'Rajajinagar' else  (27 if listed_in_city == 'Residency Road' else  (28 if listed_in_city == 'Sarjapur Road' else 29   ))))))))))))))))))))))))))))],
               
            }
        )

        st.write("Input Data: ")
        st.dataframe(df)

        pred = model.predict(df)
        st.write(F"Prediction: {pred}")

app()
