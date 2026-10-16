import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

st.title("Sales Data Analysis Dashboard")

file_path = Path(__file__).parent / "sales_data.csv"

if file_path.exists():
    df = pd.read_csv(file_path)

    st.subheader("Sales Data")
    st.dataframe(df)

    st.subheader("Total Records")
    st.write(len(df))

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    if numeric_columns:
        column = st.selectbox(
            "Select column for graph",
            numeric_columns
        )

        fig, ax = plt.subplots()
        df[column].plot(kind="bar", ax=ax)
        st.pyplot(fig)
        plt.close(fig)

else:
    st.error("sales_data.csv file not found!")