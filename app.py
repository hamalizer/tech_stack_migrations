# imports
import pandas as pd
import streamlit as st
import plotly.express as px

# read dataframe
df = pd.read_csv('migrations.csv')

# webpage header
st.header('Tech Stack Migrations: All roads lead to Go.')

# changed-to stacks by-year
st.write(px.histogram(df, x='year', color='to'))

# a big ol set of scatterplots
st.write(px.scatter_matrix(df, color='year'))

st.write('It is not a functional application yet. Under construction.')


st.write('Source on Github:[link](https://github.com/hamalizer/tech_stack_migrations)')