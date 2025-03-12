import streamlit as st
import pandas as pd
from classify import classify
import os


st.title("🔍 Log Classification Tool")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        if "source" not in df.columns or "log_message" not in df.columns:
            st.error("CSV must contain 'source' and 'log_message' columns.")
        else:

            df["target_label"] = classify(list(zip(df["source"], df["log_message"])))

            st.write("### Classified Logs", df)

            output_file = "resources/output.csv"
            df.to_csv(output_file, index=False)

            with open(output_file, "rb") as file:
                st.download_button(
                    label=" Download Classified CSV",
                    data=file,
                    file_name="classified_logs.csv",
                    mime="text/csv"
                )

    except Exception as e:
        st.error(f"Error: {e}")
