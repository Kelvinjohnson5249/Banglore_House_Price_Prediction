import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/api"

st.title("Bangalore Home Price Prediction")
st.write("Enter the details of the property to estimate its price.")


def format_price_lakhs(value_lakhs):
    crore = value_lakhs / 100
    if value_lakhs >= 100:
        return f"₹ {crore:.2f} Crores"
    else:
        return f"₹ {value_lakhs:.2f} Lakhs"


#fetch locations from the API
@st.cache_data
def fetch_locations():
    response = requests.get(f"{API_URL}/locations")
    if response.status_code == 200:
        return response.json()['locations']
    return []

locations = fetch_locations()


#input fields
location = st.selectbox("Location", locations)
total_sqft = st.number_input("Total Square Feet", min_value=300, max_value=10000, value=1000)
bath = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2)
bhk = st.number_input("Number of BHK", min_value=1, max_value=10, value=2)

if st.button("Predict Price"):
    payload = {
        "total_sqft": total_sqft,
        "bath": bath,
        "bhk": bhk,
        "location": location
    }
    
    response = requests.post(f"{API_URL}/predict", json=payload)

    if response.status_code == 200:
        price = response.json()["estimated_price"]
        formatted = format_price_lakhs(price)
        st.success(f"🏷️ Estimated Price: **{formatted}**")
    else:
        st.error("Error fetching prediction. Check API backend.")