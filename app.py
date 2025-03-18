import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/vehicles_us.csv")

st.title("Car Advertisement Data Dashboard")

st.header("Exploratory Data Analysis of Vehicle Prices and Mileage")

if st.checkbox("Show raw data"):
    st.write(df.head())

st.subheader("Car Price Distribution")
fig = px.histogram(df, x="price", nbins=30, color_discrete_sequence=["orange"], title="Distribution of Car Prices")
st.plotly_chart(fig)

st.subheader("Mileage vs Price")
fig = px.scatter(df, x="odometer", y="price", color_discrete_sequence=["green"], title="Mileage vs Price")
st.plotly_chart(fig)