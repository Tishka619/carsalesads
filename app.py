import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/vehicles_us.csv")

df['model_year'] = df.groupby('model')['model_year'].transform(lambda x: x.fillna(x.median()))
df['cylinders'] = df.groupby('model')['cylinders'].transform(lambda x: x.fillna(x.median()))
df['odometer'] = df.groupby('model_year')['odometer'].transform(lambda x: x.fillna(x.median()))

def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

df = remove_outliers(df, 'model_year')
df = remove_outliers(df, 'price')

st.title("Car Advertisement Data Dashboard")

st.header("Exploratory Data Analysis of Vehicle Prices and Mileage")

if st.checkbox("Show raw data"):
    st.write(df.head())

st.subheader("Car Price Distribution")
fig = px.histogram(df, x="price", nbins=50, color_discrete_sequence=["orange"], title="Distribution of Car Prices")
st.plotly_chart(fig)

st.subheader("Mileage vs Price")
fig = px.scatter(df, x="odometer", y="price", color_discrete_sequence=["green"], title="Mileage vs Price"
                 opacity=0.5)
st.plotly_chart(fig)