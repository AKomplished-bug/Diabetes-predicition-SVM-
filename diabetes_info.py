import streamlit as st
import pandas as pd

def app():
    st.title("Medicinal Prescriptions for Diabetes")

    # Define data
    data = {
        "Medication Class": ["Metformin", "Sulfonylureas", "Insulin", "GLP-1 agonists", 
                             "DPP-4 inhibitors", "SGLT2 inhibitors", "Meglitinides", 
                             "Alpha-glucosidase inhibitors"],
        "Medication Examples": ["Metformin", "Glipizide, Glyburide", "Rapid-acting, Long-acting",
                                "Liraglutide, Semaglutide", "Sitagliptin, Linagliptin",
                                "Empagliflozin, Dapagliflozin", "Repaglinide, Nateglinide",
                                "Acarbose, Miglitol"],
        "Medication Description": ["A first-line medication for type 2 diabetes, helps reduce glucose production in the liver and improves insulin sensitivity.",
                                   "Stimulate the pancreas to produce more insulin.",
                                   "Essential for type 1 diabetes and sometimes required for type 2 diabetes, helps regulate blood sugar levels.",
                                   "Help lower blood sugar levels by increasing insulin production and slowing digestion.",
                                   "Increase the levels of incretin hormones, which help control blood sugar levels.",
                                   "Help reduce blood sugar levels by increasing the excretion of glucose through the urine.",
                                   "Stimulate the pancreas to release insulin more quickly after meals.",
                                   "Slow down the digestion and absorption of carbohydrates, helping to control blood sugar levels."],
        "When to Take": ["Usually taken with meals", "Usually taken before meals", "Depends on type (rapid-acting before meals, long-acting once daily)", 
                         "Depends on type (some once daily, others once weekly)", "Usually taken once daily with or without food",
                         "Usually taken once daily in the morning with or without food", "Usually taken before meals", 
                         "Taken with the first bite of each main meal"]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Define CSS for styling the table
    table_styles = [
        dict(selector="th", props=[("font-size", "18px"), ("text-align", "center"), ("background-color", "#4CAF50"), ("color", "white"), ("border", "1px solid #ddd"), ("padding", "8px")]),
        dict(selector="td", props=[("font-size", "16px"), ("text-align", "left"), ("border", "1px solid #ddd"), ("padding", "8px")]),
        dict(selector=".row-hover:hover", props=[("background-color", "#f2f2f2")])
    ]

    # Set background color of the table
    st.markdown("<style>body {background-color: #4CAF50;}</style>", unsafe_allow_html=True)
    
    # Display styled table
    st.table(df.style.set_table_styles(table_styles))


