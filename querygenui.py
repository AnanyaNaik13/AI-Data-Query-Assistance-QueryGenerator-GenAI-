import streamlit as st
import pandas as pd
from QueryGenapp import get_answer


st.title("CSV / Excel Question Answering System")

file = st.file_uploader("Upload file", type=["csv", "xlsx", "xls"])
question = st.text_input("Question")

if st.button("Get answer"):
    if file is None or not question:
        st.warning("Please upload a file and type a question.")
    else:
        if file.name.endswith(".csv"):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)

        code, answer = get_answer(df, question)

        st.code(code, language="python")
        st.subheader("Answer")
        st.write(answer)