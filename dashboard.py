import streamlit as st
import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

st.set_page_config(page_title="Project", layout="wide")

st.title("Crypto Dashboard")
st.subheader("Crypto Market Data")
st.divider()

connection = psycopg2.connect(DATABASE_URL)

query = "SELECT * FROM crypto_prices"
df_question = pd.read_sql_query(query, connection)

connection.close()

coin_choice = st.selectbox("Choose a coin", df_question["coin_name"].unique())
filtered_data = df_question[df_question["coin_name"] == coin_choice]

st.line_chart(filtered_data.set_index("timestamp")["price"])