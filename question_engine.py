import re

CATEGORIES = {
    "coding": ["code", "program", "function", "bug", "script", "algorithm", "error"],
    "web_development": ["website", "webpage", "html", "css", "navbar", "form", "landing page"],
    "study": ["explain", "what is", "difference between", "how does", "summarize", "notes"],
    "assignment": ["write", "essay", "report", "introduction", "conclusion", "paragraph"],
    "project": ["project idea", "suggest", "recommend", "plan", "build", "create"]
}

QUESTIONS = {
    "coding": [
        {"id": "language", "text": "Language?", "options": ["Python", "C", "Java", "JavaScript", "Other"]},
        {"id": "tone", "text": "Purpose?", "options": ["Write new code", "Fix a bug", "Explain code", "Optimize"]},
        {"id": "format", "text": "Output format?", "options": ["Just code", "Code + explanation", "Step-by-step"]},
        {"id": "audience", "text": "Level?", "options": ["Beginner", "Intermediate", "Advanced"]}
    ],
    "web_development": [
        {"id": "language", "text": "Stack?", "options": ["HTML/CSS only", "With JavaScript", "Bootstrap", "Other framework"]},
        {"id": "tone", "text": "What to build?", "options": ["Full page", "Single component", "Fix existing code"]},
        {"id": "error_handling", "text": "Style preference?", "options": ["Minimal", "Modern", "Dark theme", "Colorful"]},
        {"id": "length", "text": "Responsive needed?", "options": ["Yes", "No"]}
    ],
    "study": [
        {"id": "audience", "text": "Explain like I'm?", "options": ["A beginner", "A student", "Already familiar"]},
        {"id": "format", "text": "Format?", "options": ["Plain explanation", "With examples", "Bullet points", "Analogy-based"]},
        {"id": "length", "text": "Length?", "options": ["Short summary", "Detailed", "One-liner definition"]},
        {"id": "tone", "text": "Include?", "options": ["Diagram description", "Real-world use case", "Both", "Neither"]}
    ],
    "assignment": [
        {"id": "format", "text": "Type?", "options": ["Essay", "Report", "Introduction only", "Full assignment"]},
        {"id": "tone", "text": "Tone?", "options": ["Formal", "Semi-formal", "Simple English"]},
        {"id": "length", "text": "Word limit?", "options": ["Under 300", "300–600", "600+", "No limit"]},
        {"id": "error_handling", "text": "Include?", "options": ["Headings", "References placeholder", "Both", "Neither"]}
    ],
    "project": [
        {"id": "language", "text": "Domain?", "options": ["Web", "Python", "ML", "Android", "General CS"]},
        {"id": "tone", "text": "Purpose?", "options": ["College mini project", "Personal use", "Learning"]},
        {"id": "format", "text": "Output wanted?", "options": ["Just the idea", "Idea + structure", "Full roadmap"]},
        {"id": "length", "text": "Complexity?", "options": ["Simple (1–2 weeks)", "Medium", "Advanced"]}
    ],
    "fallback": [
        {"id": "format", "text": "Goal?", "options": ["Explain something", "Generate content", "Solve a problem", "Get ideas"]},
        {"id": "audience", "text": "Audience?", "options": ["Myself", "Teacher", "Evaluator", "General public"]},
        {"id": "tone", "text": "Tone?", "options": ["Formal", "Casual", "Technical"]},
        {"id": "length", "text": "Length?", "options": ["Short", "Medium", "Detailed"]}
    ]
}

def detect_category(prompt: str) -> str:
    """Detect category from prompt keywords."""
    p_lower = prompt.lower()
    for cat, keywords in CATEGORIES.items():
        for kw in keywords:
            if kw in p_lower:
                return cat
    return "fallback"

def get_questions_for_prompt(prompt: str, category: str = "auto") -> dict:
    """Analyze the prompt and category to return a tailored list of questions."""
    mapped_category = category
    if category == "auto" or not category:
        mapped_category = detect_category(prompt)
    elif category == "code" or category == "coding":
        mapped_category = "coding"
    elif category == "writing" or category == "assignment":
        mapped_category = "assignment"
    elif category == "analysis" or category == "study":
        mapped_category = "study"
    elif category == "general" or category == "fallback":
        mapped_category = "fallback"

    if mapped_category not in QUESTIONS:
        mapped_category = "fallback"

    return {
        "detected_category": mapped_category,
        "questions": QUESTIONS[mapped_category]
    }
