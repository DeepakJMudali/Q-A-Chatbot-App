# Enhanced Q&A ChatBot With OPENAI and LangChain

Small Streamlit app that provides a Q&A chatbot powered by OpenAI models and LangChain components.

**Features**
- Interactive Streamlit UI with sidebar controls for model, temperature, and tokens.
- Uses `langchain` + `langchain-openai` for LLM integration and prompt chaining.
- Optionally reads `.env` values via `python-dotenv` for LangChain tracing/config.

**Requirements**
- Python 3.8+
- See `requirements.txt` for exact packages used (examples below).

**Dependencies (from `requirements.txt`)**
- `langchain-openai`
- `langchain`
- `python-dotenv`
- `langchain_community`
- `langchain_core`
- `streamlit`

**Setup (Windows PowerShell)**
- Create and activate a virtual environment, then install deps:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
pip install -r requirements.txt
```

- If PowerShell blocks script execution when activating the virtualenv, run (as needed):

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Environment / API Keys**
- The app prompts for your OpenAI API key in the sidebar at runtime. Enter your `OPENAI` key there.
- Optionally create a `.env` file in the project root to set `LANGCHAIN_API_KEY` (the app loads `.env` at start):

```
LANGCHAIN_API_KEY=your_langchain_key_here
# (optional) other env vars
```

**Run (development)**
- Start the Streamlit app from PowerShell:

```powershell
streamlit run app.py
```

- Open the URL shown by Streamlit (usually `http://localhost:8501`).

**Usage**
- Enter your OpenAI API key in the sidebar `Enter your OpenAI API Key` field.
- Choose a model and adjust `temperature` / `max tokens` sliders.
- Type a question in the main input and press Enter.

**Notes & Troubleshooting**
- The app currently routes the OpenAI key from the sidebar into `openai` and the LangChain components. If you prefer to use an environment variable for the OpenAI key, you can modify `app.py` to read `OPENAI_API_KEY` from the environment and set it when launching Streamlit.
- If you see import errors, confirm the virtualenv is activated and packages from `requirements.txt` are installed.

**Contributing**
- Small changes, bug reports, and improvements are welcome. Open an issue or PR with a clear description and reproduction steps.

**License**
- No license specified. Add a `LICENSE` file if you want to open-source this project.
