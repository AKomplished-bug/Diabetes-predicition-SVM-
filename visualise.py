import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st





def app(df, X, y):
    """This function create the visualisation page"""
    
    # Remove the warnings
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Set the page title
    st.title("Visualise the Diabetes Prediction Web app")

    # Create a checkbox to show correlation heatmap
    if st.checkbox("Show the correlation heatmap"):
        st.subheader("Correlation Heatmap")

        fig = plt.figure(figsize = (10, 6))
        ax = sns.heatmap(df.iloc[:, 1:].corr(), annot = True)   # Creating an object of seaborn axis and storing it in 'ax' variable
        bottom, top = ax.get_ylim()                             # Getting the top and bottom margin limits.
        ax.set_ylim(bottom + 0.5, top - 0.5)                    # Increasing the bottom and decreasing the top margins respectively.
        st.pyplot(fig)

    if st.checkbox("Fasting Glucose Level vs Blood Pressure Plot"):
        sns.color_palette("rocket", as_cmap=True)
        ax=sns.scatterplot(x="FastingGlc",y="BloodPressure",data=df)
        st.pyplot()

    if st.checkbox("Aftermeal Glucose Level vs Blood Pressure Plot"):
        sns.color_palette("rocket", as_cmap=True)
        ax=sns.scatterplot(x="AfterGlc",y="BloodPressure",data=df)
        st.pyplot()

    if st.checkbox("Blood Pressure Level vs Skin Thickness Plot"):
        sns.color_palette("rocket", as_cmap=True)
        ax=sns.scatterplot(x="BloodPressure",y="SkinThickness",data=df)
        st.pyplot()

    if st.checkbox("Show Histogram"):
        sns.color_palette("rocket", as_cmap=True)
        ax=sns.histplot(data=df,x="Age",y="BloodPressure")
        st.pyplot()

