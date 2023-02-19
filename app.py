# imports
import pandas as pd
import streamlit as st
import plotly.express as px

# read dataframe
df = pd.read_csv('migrations.csv')

st.header('Tech Stack Migrations: All roads lead to Go.')

st.write(px.histogram(df, x='year', color='to'))

st.write(px.scatter_matrix(df, color='year'))

st.write('It is not a functional application yet. Under construction.') https://github.com/hamalizer/tech_stach_migrations