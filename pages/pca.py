import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

def visualize_pca_tsne(df):
    # Standardize the data
    standardized_data = (df - df.mean()) / df.std()

    # Apply PCA
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(standardized_data)

    # Visualize PCA results
    st.subheader('PCA Visualization')
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(pca_result[:, 0], pca_result[:, 1], c=df['Outcome'], cmap='viridis')
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    st.pyplot(fig)

    # Apply t-SNE
    tsne = TSNE(n_components=2, random_state=42)
    tsne_result = tsne.fit_transform(standardized_data)

    # Visualize t-SNE results
    st.subheader('t-SNE Visualization')
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(tsne_result[:, 0], tsne_result[:, 1], c=df['Outcome'], cmap='viridis')
    ax.set_xlabel('t-SNE Dimension 1')
    ax.set_ylabel('t-SNE Dimension 2')
    st.pyplot(fig)

def app(df):
    st.title("PCA and t-SNE Visualization")
    if st.checkbox("Visualize PCA and t-SNE"):
        visualize_pca_tsne(df)

# Example usage
# Load your dataset here
# Assuming df is your DataFrame containing the dataset
# app(df)
