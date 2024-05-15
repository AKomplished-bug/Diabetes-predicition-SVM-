import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.ensemble import RandomForestClassifier





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

    if st.checkbox("Countplot of outcome"):
        sns.countplot(x='Outcome', data=df)
        st.pyplot()

    if st.checkbox("feature importance"):
        clf = RandomForestClassifier()
        clf.fit(X.copy(), y.copy())  
        feature_importances = clf.feature_importances_
        plt.figure(figsize=(10, 6))
        plt.barh(X.columns, feature_importances)
        plt.xlabel('Feature Importance')
        plt.ylabel('Feature')
        plt.title('Feature Importance Plot')
        st.pyplot()
 
    if st.checkbox("risk factor analysis"):
      mean_values = df.groupby('Outcome').mean().reset_index()
      features = df.columns.drop(['Outcome'])

      for feature in features:
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.barplot(data=mean_values, x='Outcome', y=feature, palette='pastel', ax=ax)
        ax.set_title(f'Mean {feature} by Outcome')
        ax.set_xlabel('Outcome')
        ax.set_ylabel(f'Mean {feature}')
        st.pyplot(fig)

