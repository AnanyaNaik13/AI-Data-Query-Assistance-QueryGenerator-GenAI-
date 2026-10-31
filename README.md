# Query Generator App

A simple Streamlit app where you upload a CSV or Excel file, ask a question in plain English, and get the answer. An LLM (Groq) writes the pandas code for your question, and the app runs it on your data and shows the result.

**Live demo:** https://querygeneratorapp.streamlit.app/

## How it works

1. Upload a CSV or Excel file.
2. Type a question, for example: *What is the average salary of employees?*
3. Click **Get answer**.
4. The app sends your question and the column names to the Groq model (`openai/gpt-oss-120b`).
5. The model returns Python (pandas) code, which the app shows and runs on your data.
6. The output is displayed as the answer.

## Project structure

```
.
├── querygenui.py       # Streamlit page (upload, question, get answer button)
├── QueryGenapp.py      # Logic: Groq model, prompt, runs generated code
├── requirements.txt    # Python libraries
├── .env                # API key (not uploaded to GitHub)
└── README.md
```

## Tech stack

- Python
- Streamlit
- Pandas
- LangChain Groq (`langchain-groq`)
- python-dotenv

## Run locally

1. Clone the repository:
   ```
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. Install the libraries:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project folder and add your Groq API key:
   ```
   GROQ_API_KEY=your_key_here
   ```
   You can get a key from the [Groq Console](https://console.groq.com/).

4. Start the app:
   ```
   streamlit run querygenui.py
   ```

5. Open `http://localhost:8501` in your browser.

## Deploy on Streamlit Community Cloud

1. Push this project to GitHub (do not upload the `.env` file).
2. Create a new app on [Streamlit Community Cloud](https://streamlit.io/cloud) and select your repository and `querygenui.py`.
3. In the app's **Settings → Secrets**, add:
   ```
   GROQ_API_KEY = "your_key_here"
   ```

## Notes

- The model only receives the column names, not your actual data. The generated code runs on your data locally in the app.
- The app uses `exec` to run the model's code, so it is meant for learning and demos, not for untrusted users in production.

## Example

| Question | Generated code | Answer |
|---|---|---|
| What is the average salary of employees? | `print(df['employee_salary'].mean())` | `44800.0` |
