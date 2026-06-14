# Prompt Optimizer
### Python Mini Project | Flask + Ollama (LLaMA 3)

A web-based AI prompt engineering tool that takes a rough user prompt, asks targeted clarifying questions based on the task category, and generates a structured, high-quality prompt ready to use in any AI model.

---

## Objective

Most users write vague or incomplete prompts when interacting with AI tools. This project solves that problem by guiding users through a 3-step wizard that collects task-specific details and assembles a well-structured prompt automatically — with optional AI enhancement using a local LLM.

---

## Features

- 3-step wizard interface (Input → Refine → Result)
- Automatic category detection from prompt keywords
- 6 task categories with targeted questions and clickable options:
  - Auto-Detect
  - Coding
  - Web Development
  - Study / Explanation
  - Assignment / Writing
  - Project / Idea
- Local AI refinement using Ollama (LLaMA 3) — no internet or API key required
- Offline fallback mode if Ollama is unavailable
- Side-by-side display of Structured Prompt vs AI Refined Prompt
- One-click copy to clipboard
- Minimal dark UI

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| AI / LLM | Ollama (LLaMA 3 — runs locally) |
| Frontend | HTML, CSS, JavaScript (Vanilla) |
| Fonts | Inter, JetBrains Mono (Google Fonts) |
| Environment | python-dotenv |

---

## Project Structure

```
prompt_optimizer/
├── app.py              ← Flask routes, core logic
├── question_engine.py  ← Your "model" — rule-based question selector
├── prompt_builder.py   ← Assembles final prompt from answers
├── gemini_client.py    ← API call, isolated
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── requirements.txt
```

---

## How It Works

1. **User enters a rough prompt** and selects a task category (or lets the system auto-detect it)
2. **`question_engine.py`** detects the category using keyword matching and returns 4 targeted questions with clickable options
3. **User selects answers** — no typing required
4. **`prompt_builder.py`** assembles the answers into a structured prompt format
5. **`gemini_client.py`** sends the structured prompt to a locally running LLaMA 3 model via Ollama for AI refinement
6. **Results are displayed** side-by-side — structured version and AI-refined version — both copyable

---

## Setup Instructions

### Prerequisites

- Python 3.8 or above
- Ollama installed → [https://ollama.com](https://ollama.com)
- LLaMA 3 model pulled

### Step 1 — Clone the repository

```bash
git clone https://github.com/your-username/prompt-optimizer.git
cd prompt-optimizer
```

### Step 2 — Install Python dependencies

```bash
pip install -r requirements.txt
```

### Step 3 — Pull the LLaMA 3 model

```bash
ollama pull llama3
```

This downloads approximately 4.7 GB. Only required once.

### Step 4 — Start Ollama

```bash
ollama serve
```

Keep this terminal open. Ollama runs on `http://127.0.0.1:11434`.

### Step 5 — Run the Flask app

Open a new terminal:

```bash
python app.py
```

### Step 6 — Open in browser

```
http://127.0.0.1:5000
```

---

## Requirements

```
flask
requests
python-dotenv
```

Install with:
```bash
pip install -r requirements.txt
```

---

## Category System

The `question_engine.py` detects the task category from keywords in the user's prompt and loads the appropriate question set.

| Category | Trigger Keywords |
|---|---|
| Coding | code, program, function, bug, script, algorithm, error |
| Web Development | website, webpage, html, css, navbar, form, landing page |
| Study / Explanation | explain, what is, difference between, how does, summarize, notes |
| Assignment / Writing | write, essay, report, introduction, conclusion, paragraph |
| Project / Idea | project idea, suggest, recommend, plan, build, create |

If no keyword matches, a general fallback question set is used.

---

## Offline Fallback

If Ollama is not running or the model fails to respond, the system automatically returns a mock-enhanced prompt using a pre-defined template. The UI displays a warning and still shows the structured prompt — the application does not crash.

---

## Limitations

- Requires Ollama installed locally for AI refinement
- LLaMA 3 model requires approximately 4.7 GB disk space and 8 GB RAM for smooth performance
- Category detection is keyword-based, not ML-based — complex or mixed prompts may fall to the general fallback

---

## Future Scope

- Add more categories (Data Analysis, Image Generation, Email Writing)
- Upgrade to ML-based category classification
- Export optimized prompt as a text or PDF file
- Add prompt history and saved sessions
- Deploy to cloud with Groq API as an alternative backend

This project is developed for academic purposes as a Python mini project submission.
