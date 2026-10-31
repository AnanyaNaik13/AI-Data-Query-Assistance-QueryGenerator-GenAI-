import io
import os
import pandas as pd
from contextlib import redirect_stdout
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-120b", api_key=os.getenv('GROQ_API_KEY'), temperature=0)


def get_answer(df, question):
    column_names = list(df.columns)
    prompt = """Role:Act as a data analyst Task:Write code in python to get answer of the given question.Question:{} column names:{} dataframe variable name:df constraints:give only executable code output:plain text format without markdown""".format(
        question, column_names
    )

    code = llm.invoke(prompt).content

    buffer = io.StringIO()
    with redirect_stdout(buffer):
        exec(code, {"df": df, "pd": pd})

    return code, buffer.getvalue()