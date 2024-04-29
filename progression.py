import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def plot_sugar_progression(months, sugar_levels):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(range(1, months + 1), sugar_levels, marker='o', linestyle='-')
    ax.set_title("Sugar Level Progression")
    ax.set_xlabel("Month")
    ax.set_ylabel("Sugar Level")
    ax.set_xticks(range(1, months + 1))
    ax.grid(True)
    return fig

def app():
    st.title("Sugar Level Progression")

    # Ask user for number of months of sugar level data
    num_months = st.number_input("Enter the number of months:", min_value=1, step=1)

    # Initialize list to store sugar levels
    sugar_levels = []

    # Ask user for sugar level for each month
    for i in range(1, num_months + 1):
        sugar_level = st.number_input(f"Enter sugar level for month {i}:", min_value=0.0)
        sugar_levels.append(sugar_level)

    # Check if sugar levels are provided for all months
    if len(sugar_levels) == num_months:
        # Display plot of sugar level progression
        fig = plot_sugar_progression(num_months, sugar_levels)
        st.pyplot(fig)

        # Calculate and display the average sugar level
        average_sugar_level = np.mean(sugar_levels)
        st.write(f"The average sugar level for the {num_months} months is: {average_sugar_level:.2f}")

