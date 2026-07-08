# ✈️ Travel AI Agent (Local LLM)

A local AI-powered Travel Assistant built using **Python**, **Streamlit**, **LangChain**, and **Ollama**. The application runs completely on your machine using local Large Language Models (LLMs) without requiring OpenAI APIs.

---

## 🚀 Features

- 💬 ChatGPT-style interface
- 🤖 Local AI using Ollama
- ⚡ Streaming AI responses
- 📝 Chat history
- 🔒 100% Local (Privacy Friendly)
- 🧩 Modular Architecture
- 🛠️ Easy to Extend
- 🌐 No OpenAI API Key Required

---

## 🛠️ Tech Stack

| Technology | Description |
|------------|-------------|
| Python | Programming Language |
| Streamlit | Frontend UI |
| LangChain | LLM Framework |
| Ollama | Local LLM Runtime |
| Gemma 3 / Qwen2.5 | Local AI Models |

---

## 📁 Project Structure

```text
travel-ai-agent/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── llm/
│   ├── __init__.py
│   ├── ollama_client.py
│   └── prompts.py
│
├── utils/
│   └── __init__.py
│
└── test.py
```

---

## 📋 Prerequisites

- Python 3.10+
- Ollama installed
- Git (Optional)

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/travel-ai-agent.git

cd travel-ai-agent
```

Or create the project manually.

---

### 2. Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🦙 Install Ollama

Download

https://ollama.com/download

Verify installation

```bash
ollama --version
```

---

## 📥 Download AI Model

Recommended

```bash
ollama pull gemma3:4b
```

or

```bash
ollama pull qwen2.5:1.5b
```

Verify

```bash
ollama list
```

Example

```text
NAME            SIZE
gemma3:4b       3.3 GB
qwen2.5:1.5b    986 MB
```

---

## ⚙️ Configuration

Edit `config.py`

```python
MODEL_NAME = "gemma3:4b"
OLLAMA_URL = "http://localhost:11434"
```

---

## ▶️ Run Ollama

In a new terminal

```bash
ollama serve
```

If you receive

```text
address already in use
```

The server is already running.

---

## 🧪 Test the LLM

Run

```bash
python test.py
```

Expected output

```text
Hello!

How can I help you today?
```

---

## 🚀 Start the Application

```bash
python -m streamlit run app.py
```

Open

```
http://localhost:8501
```

---

## 💬 Example Prompt

```
Plan a 3-day trip to Goa with a budget of ₹20,000.
```

---

## 📦 Requirements

```text
streamlit
langchain
langchain-community
langchain-core
langchain-ollama
python-dotenv
```

---

## 📌 Current Features

- Local AI Chat
- Streaming Responses
- Chat History
- Streamlit UI
- LangChain Integration
- Ollama Integration

---

## 🚧 Upcoming Features

### Phase 2

- Travel Planning Form
- Memory
- ChromaDB
- RAG
- Prompt Templates

### Phase 3

- Flight Search
- Hotel Search
- Weather Integration
- Google Maps
- Places API

### Phase 4

- Multi-Agent System
- LangGraph
- Budget Optimizer
- Itinerary Generator
- PDF Export

### Phase 5

- Voice Input
- Speech Output
- User Authentication
- Database
- Deployment

---

## 🧠 Architecture

```text
                User
                  │
          Streamlit UI
                  │
            LangChain
                  │
             ChatOllama
                  │
        Gemma 3 / Qwen2.5
                  │
           AI Response
```

---

## 📸 Screenshots

Coming Soon

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Create a Pull Request.

---

## 📄 License

MIT License

---

## 👨‍💻 Author

**Suresh Babu**

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

Happy Coding! 🚀