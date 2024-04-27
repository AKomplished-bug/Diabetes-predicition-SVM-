import streamlit as st
import pandas as pd


def app(df):

    # Add title to the page
    st.title("Data Info page")

    # Add subheader for the section
    st.subheader("View Data")

    # Create an expansion option to check the data
    with st.expander("View data"):
        st.dataframe(df)

    # Create a section to columns values
    # Give subheader
    st.subheader("Columns Description:")

    # Create a checkbox to get the summary.
    if st.checkbox("View Summary"):
        summary = df.describe()
        st.dataframe(summary)

        # Additional information: mean, median, and standard deviation
        st.subheader("Additional Information:")
        with st.expander("View additional information"):
            additional_info = pd.DataFrame({
                "Mean": df.mean(),
                "Median": df.median(),
                "Standard Deviation": df.std()
            })
            st.dataframe(additional_info)

    # Create multiple check box in row
    col_name, col_dtype, col_data = st.columns(3)

    # Show name of all dataframe
    with col_name:
        if st.checkbox("Column Names"):
            st.dataframe(df.columns)

    # Show datatype of all columns 
    with col_dtype:
        if st.checkbox("Columns data types"):
            dtypes = df.dtypes.apply(lambda x: x.name)
            st.dataframe(dtypes)
    
    # Show data for each columns
    with col_data: 
        if st.checkbox("Columns Data"):
            col = st.selectbox("Column Name", list(df.columns))
            st.dataframe(df[col])
