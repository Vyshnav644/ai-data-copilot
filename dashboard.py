import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🚀 AI Data Copilot (Cloud Demo)")

uploaded_file = st.file_uploader("Upload dataset")

if uploaded_file:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("Dataset loaded")

    st.write("Columns:", list(df.columns))

    numeric_cols = df.select_dtypes(include="number").columns

    question = st.text_input("Ask about data")

    if question:

        q = question.lower()

        if "total" in q:
            st.write(df[numeric_cols[0]].sum())

        elif "chart" in q or "plot" in q:
            fig = px.histogram(df, x=numeric_cols[0])
            st.plotly_chart(fig)

        else:
            st.write("Basic analysis shown — full AI available locally.")
