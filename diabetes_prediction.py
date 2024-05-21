import streamlit as st
import numpy as np
import pandas as pd
# from sklearn.preprocessing import StandardScaler
# from sklearn.model_selection import train_test_split
# from sklearn import svm
# from sklearn.metrics import accuracy_score

# Load the diabetes dataset
diabetes_dataset = pd.read_csv('diabetes.csv')

# Display the dataset using Streamlit
st.title("Diabetes Prediction App")
st.subheader("Diabetes Dataset")
st.dataframe(diabetes_dataset)

# Summary statistics
st.subheader("Dataset Summary")
st.write(diabetes_dataset.describe())

# Class distribution
st.subheader("Class Distribution")
st.write(diabetes_dataset['Outcome'].value_counts())

# Mean values by Outcome
st.subheader("Mean Values by Outcome")
st.write(diabetes_dataset.groupby('Outcome').mean())

