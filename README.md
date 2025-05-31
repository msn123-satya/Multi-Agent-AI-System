# 🧠 Multi-Agent AI System using FastAPI & Gemini API

A web-based AI system that simulates collaboration between multiple intelligent agents to generate, evaluate, and refine creative ideas based on user input.  
This project uses **FastAPI (Python backend)**, **HTML/CSS/JavaScript (frontend)**, and **Gemini API (Google Generative AI)**.  
Deployed Live on **Render** 🚀

🔗 **Live Demo**: [https://multi-agent-ai-system-vqcj.onrender.com](https://multi-agent-ai-system-vqcj.onrender.com)

---

## 📌 Features

- ✍️ **Thinker Agent**: Generates 2–3 creative ideas from your prompt.
- ✅ **Checker Agent**: Evaluates ideas and selects the most feasible one.
- 🎯 **Finisher Agent**: Refines the best idea into a user-friendly response.
- 🌐 Frontend built with HTML, CSS, JS and connected to FastAPI backend.
- ⚡ Fast, responsive UI with real-time result rendering using templates.
- 🔐 Uses Google Gemini API (via API key).

---

## 🛠️ Tech Stack

| Layer     | Technology              |
|-----------|--------------------------|
| Frontend  | HTML, CSS, JavaScript    |
| Backend   | Python, FastAPI          |
| AI Engine | Google Gemini (via `google.generativeai`) |
| Templates | Jinja2 (`form.html`)     |
| Deployment| Render                   |
| Secrets   | `.env` file with Gemini API Key |

---

## 🚀 How It Works

1. User inputs a query (e.g., "An app idea for college students").
2. The **Thinker Agent** creates a list of 2–3 innovative ideas.
3. The **Checker Agent** selects the most technically feasible idea.
4. The **Finisher Agent** polishes the selected idea and shows it in a readable format.

Each agent uses Gemini API (`gemini-2.0-flash`) and communicates internally in a pipeline-style architecture.

---

## 🧪 Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/multi-agent-ai-system.git
cd multi-agent-ai-system
