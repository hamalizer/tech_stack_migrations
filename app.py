# imports
import pandas as pd
import streamlit as st
import plotly.express as px

# read dataframe
df = pd.read_csv('migrations.csv')

# First, add a count column with a val of 1 to assist counting the total num of migrations
df['count'] = 1


# webpage header
st.header('Tech Stack Migrations: All roads lead to Go.')


# changed-to stacks by-year
# the goofiest histogram i admit
st.write('Changed-to stacks by-year')
st.write(px.histogram(df, x='year', color='to'))

# I have yet to find a quick and dirty way of dropping the outliers(or stacking them) so this is easier to read without modifying the data itself
st.write('An illustration of stack-to-stack changes, colored by-year.')
st.write(px.scatter(df, x='to', y='from', color='year'))

# a long string
longstring = 'We can see Golang is a very popular choice for tech companies who have decided to migrate their stack to a new language.<br>By-totals, the total number of migrations to golang is near double when accounting for the fact that TiDB is written in GO'
#conclusion statement
st.write(longstring)





st.write('Source on Github:[link](https://github.com/hamalizer/tech_stack_migrations)')