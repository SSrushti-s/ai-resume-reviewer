# AI Resume Reviewer 📄
```
An interactive, AI-powered web application built with Streamlit, LangChain, and Groq Cloud. This tool extracts content from a user's PDF resume, analyzes it against a target job description, and provides a structured JSON evaluation including a match percentage score, identified skill gaps, and critical recommendations.

Live Demo: https://ai-resume-reviewer-7mdbo4mgsvcg6mqklvgpph.streamlit.app/

```
---

## 🚀 Features

- **PDF Text Extraction:** Seamlessly parses text data from uploaded resumes using a robust PDF byte reader.
- **Fast AI Inference:** Leverages Groq Cloud's ultra-fast LLM speeds via `ChatGroq`.
- **Streamlit Web UI:** Intuitive dashboard layout featuring large visual metrics and structured result components.
- **Zero-Latency Evaluation:** Gives candidate-facing score analysis in seconds.

---

## 🛠️ Tech Stack

- **Frontend/UI:** [Streamlit](https://streamlit.io)
- **AI Orchestration:** [LangChain](https://langchain.com) & `langchain-groq`
- **Inference Provider:** [Groq Cloud LLM](https://groq.com)
- **PDF Processing:** `pypdf`

---

## 📁 Repository Structure

```text
├── app/
│   ├── __init__.py
│   ├── agent.py          # AI logic and LangChain prompt orchestration
|   ├── prompts.py
│   └── pdf_loader.py     # Extracting plain text from PDF stream data
├── main.py                # Main Streamlit web application interface
├── requirements.txt      # Production package dependencies
└── README.md             # Project documentation
```

---

## 💻 Local Setup Instructions

Follow these steps to run the application on your local machine:

### 1. Clone the Repository
```bash
git clone [<your-repository-url>](https://github.com/SSrushti-s/ai-resume-reviewer)
cd ai-resume-reviewer
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Your API Key
Create a `.env` file in the root folder (or set it in your system environment):
```env
GROQ_API_KEY=gsk_your_actual_private_api_key_here
```

### 5. Start the App
```bash
streamlit run app.py
```
Your local browser tab will automatically open at `http://localhost:8501`.

---

## ☁️ Cloud Deployment (Streamlit Community Cloud)

This app is optimized for seamless deployment to **Streamlit Community Cloud**:

1. Push your latest code changes to your public **GitHub repository**.
2. Visit [share.streamlit.io](https://streamlit.io) and log in using your GitHub account.
3. Click **Create App**, then select your repository, branch, and specify `app.py` as the main file path.
4. **Important (API Configuration):** Before clicking deploy, click **Advanced Settings** -> **Secrets** and paste your API key in the following TOML format:
   ```toml
   GROQ_API_KEY = "gsk_your_actual_private_api_key_here"
   ```
5. Click **Deploy** and your live URL will be ready within minutes!
