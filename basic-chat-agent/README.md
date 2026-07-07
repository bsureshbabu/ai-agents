# ai-agents
# 🤖 Basic ChatGPT Clone v1.0

A simple ChatGPT-style AI chatbot built using **Python**, **Streamlit**, **LangChain**, and **Ollama**. This project runs completely on your local machine without requiring an OpenAI API key.

---

## 🚀 Features

- 💬 ChatGPT-like chat interface
- 🤖 Local AI models using Ollama
- 📝 Chat history during the current session
- ⚙️ Model selection from the sidebar
- 🌡️ Adjustable temperature setting
- 🗑️ Clear chat button
- 🎨 Clean and responsive Streamlit UI
- 💻 No HTML, CSS, or JavaScript required

---

## 🛠️ Technologies Used

- Python
- Streamlit
- LangChain
- Ollama

---

## 📂 Project Structure

```
chatgpt-clone/
│
├── app.py
├── config.py
├── utils.py
├── requirements.txt
└── assets/
```

---

## 📦 Installation

### 1. Clone the project

```bash
git clone https://github.com/your-username/chatgpt-clone.git

cd chatgpt-clone
```

### 2. Create a virtual environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

### 4. Install Ollama

Download and install Ollama from:

https://ollama.com/download

---

### 5. Download a local model

Example:

```bash
ollama pull qwen2.5:1.5b
```

You can also use:

```bash
ollama pull gemma3:4b
```

or

```bash
ollama pull llama3.2
```

---

## ▶️ Run the application

```bash
python -m streamlit run app.py
```

The application will open automatically in your browser.

Default URL:

```
http://localhost:8501
```

---

## 📸 Version 1 Features

- Chat with a local AI model
- View previous messages
- Select different Ollama models
- Adjust model temperature
- Clear conversation
- Simple and clean interface

---

## 📋 Supported Models

- qwen2.5:1.5b
- gemma3:4b
- llama3.2

---

## 📦 Requirements

```text
streamlit
langchain
langchain-ollama
```

Install them with:

```bash
python -m pip install -r requirements.txt
```

---

## 🎯 Version 1 Goal

Build a fully functional local AI chatbot that provides a ChatGPT-like experience using only Python and Ollama.

---

## 🚀 Upcoming Features (Version 2)

- Streaming responses
- Conversation memory
- Better markdown rendering
- Copy code button
- Response regeneration
- Improved chat experience

---

## 📄 License

This project is for learning and educational purposes.

---

## 👨‍💻 Author

**Suresh Babu**

Learning AI Engineering with Python, Streamlit, LangChain, and Ollama.