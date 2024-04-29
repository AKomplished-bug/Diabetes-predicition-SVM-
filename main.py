"""This is the main module to run the app"""

# Importing the necessary Python modules.
import streamlit as st

# Import necessary functions from web_functions
from web import load_data

# Configure the app
st.set_page_config(
    page_title = 'Diabetes Prediction',
    page_icon ='🥯',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

# Import pages
import home_page, home_data, predict, visualise, diabetes_info



# Dictionary for pages
Tabs = {
    "Home": home_page,
    "Data Info": home_data,
    "Prediction": predict,
    "Visualisation": visualise,
    "Prescription": diabetes_info
     
}

# Create a sidebar
# Add title to sidear
st.sidebar.title("Navigation")

# Create radio option to select the page
page = st.sidebar.radio("Pages", list(Tabs.keys()))

# Loading the dataset.
df, X, y = load_data()

# Call the app funciton of selected page to run
if page in ["Prediction", "Visualisation"]:
    Tabs[page].app(df, X, y)
elif (page == "Data Info"):
    Tabs[page].app(df)
else:
    Tabs[page].app()
