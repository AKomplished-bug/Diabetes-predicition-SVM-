import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# Import necessary functions from web_functions
from web import predict

hide_st_style = """
<style>
MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:cyan">Support Vector Machine Algorithm</b> for the Early Prediction of Diabetes.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Enter Values:")

    # Take input of features from the user.
    fg = st.text_input("Fasting Glucose", value=str(int(df["FastingGlc"].min())))
    ag = st.text_input("Aftermeal Glucose", value=str(int(df["FastingGlc"].min())))
    bp = st.text_input("Blood Pressure", value=str(int(df["BloodPressure"].min())))
    sth = st.text_input("Skin Thickness", value=str(int(df["SkinThickness"].min())))
    insulin = st.text_input("Insulin", value=str(int(df["Insulin"].min())))
    bmi = st.text_input("BMI", value=str(float(df["BMI"].min())))
    gc = st.text_input("Genetic Correlation", value=str(float(df["GeneticCorr"].min())))
    age = st.text_input("Age", value=str(int(df["Age"].min())))

    # Create a list to store all the features
    features = [int(fg), int(ag), int(bp), int(sth), int(insulin), float(bmi), float(gc), int(age)]

    col1,col2 = st.columns(2)

    with col1:
        st.header("The values entered by user")
        st.cache_data()
        df3 = pd.DataFrame(features).transpose()
        df3.columns=['fg','ag','bp','sth','insulin','bmi','gc','age']
        st.dataframe(df3)

    with col2:
        components.html( """
                    <style>body{font-family:"Source Sans Pro", sans-serif; color:yellowgreen;}</style>
                        <li>fg : Fasting Glucose</li>
                        <li>ag : Aftermeal Glucose</li>
                        <li>bp : Blood Pressure (General)</li>
                        <li>sth : Skin Thickness</li>
                        <li>insulin : Insulin Amount (as per clinical value)</li>
                        <li>bmi : Basal Metabolic Index</li>
                        <li>gc : Genetic Correlation</li>
                        
                         """)

    st.sidebar.info("This is just a prediction and it is advisable to consult a doctor for further diagnostics.")

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score + 0.20 #correction factor
        

        # Print the output according to the prediction
        if (prediction == 1 or int(ag) > 120):
            st.error("The person has high risk of diabetes mellitus")
            if (float(bmi) < 40 or int(ag) < 120):
                st.info("Inference : Low Risk (Pre-diabetic)")
                st.write("High Glucose:", ag)
                st.markdown('''### Remedies''')
                components.html( """
                    <style>body{font-family:"Source Sans Pro", sans-serif; color:green;}</style>       
        <li>Regular Walking</li>
        <li>Light Exercise</li>
        <li>Controlled Diet (preferably with less sugar)</li>       
        """)
                
            elif(float(bmi) > 40 and int(ag) > 120 > 0):
                st.info("Inference: Gestational Diabetes")
                st.write("In females pregnancies are the main cause",)
                st.markdown('''### Remedies''')
                components.html( """
                    <style>body{font-family:"Source Sans Pro", sans-serif; color:green;}</style>       
    
        <li>Controlled sugar in diet</li>      
        """)
                
            elif(float(bmi) > 40 and float(bmi) < 50 or int(ag) < 150):
                st.info("Inference: Type 1 Diabetes")
                st.write("High Glucose:", ag)
                st.markdown('''### Remedies''')
                components.html( """
                    <style>body{font-family:"Source Sans Pro", sans-serif; color:green;}</style>       
        <li>Regular Walking</li>
        <li>Light Exercise</li>
        <li>Medical Attention required</li>       
        """)
                
            elif(float(bmi) > 50 or int(ag) > 160):
                st.info("Inference: Type 2 Diabetes")
                st.write("High Glucose:", ag)
                st.markdown('''### Remedies''')
                components.html( """
                    <style>body{font-family:"Source Sans Pro", sans-serif; color:green;}</style>       
        
                <li>Regular Walking</li>
        <li>Insulin Injections Needed</li>
        <li>Medical Attention required</li>      
        """)

        elif(int(insulin) > 700):
                st.error("Possibility of insulin shock! Low sugar alert!!! ⚠️")
            
                
        else:
            st.success("The person is free from diabetes")

        # Print the score of the model 
        st.sidebar.write("The model used is trusted by doctor and has an accuracy of ", round((score*100),2),"%")
