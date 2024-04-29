import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def plot_sugar_progression(sugar_levels, month_names):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(month_names, sugar_levels, marker='o', linestyle='-')
    ax.set_title("Sugar Level Progression")
    ax.set_xlabel("Month")
    ax.set_ylabel("Sugar Level")
    ax.grid(True)
    return fig

def app():
    st.title("Sugar Level Progression")

    # Define list of all 12 months
    all_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Ask user for number of months of sugar level data
    num_months = st.number_input("Enter the number of months:", min_value=1, step=1)

    # Initialize lists to store sugar levels and month names
    sugar_levels = []
    month_names = []

    for i in range(num_months):
        # Ask user to select a month
        selected_month = st.selectbox(f"Select month {i + 1}:", all_months)

        # Remove the selected month from the list of available months
        available_months = [month for month in all_months if month != selected_month]

        # Update the list of available months
        all_months = available_months

        # Ask user for sugar level for the selected month
        sugar_level = st.number_input(f"Enter sugar level for {selected_month}:", min_value=0.0, key=f"sugar_level_{selected_month}_{i}")
        month_names.append(selected_month[:3])  # Use first three letters of month name for better display
        sugar_levels.append(sugar_level)

    # Display plot of sugar level progression
    fig = plot_sugar_progression( sugar_levels, month_names)
    st.pyplot(fig)

    # Calculate and display the average sugar level
    average_sugar_level = np.mean(sugar_levels)
    st.write(f"The average sugar level for the selected months is: {average_sugar_level:.2f}")

