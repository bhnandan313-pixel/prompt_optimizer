import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

from question_engine import get_questions_for_prompt
from prompt_builder import build_prompt
from gemini_client import enhance_prompt

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Basic routing
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    """
    Analyzes the initial prompt and returns tailored diagnostic questions.
    Expects JSON body: { "prompt": "...", "category": "..." }
    """
    try:
        data = request.get_json() or {}
        prompt = data.get("prompt", "").strip()
        category = data.get("category", "auto")
        
        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400
            
        result = get_questions_for_prompt(prompt, category)
        return jsonify(result)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/build', methods=['POST'])
def build():
    """
    Assembles prompt and optionally refines it with Gemini API.
    Expects JSON body: { "prompt": "...", "answers": {...}, "refine": bool, "api_key": "..." }
    """
    try:
        data = request.get_json() or {}
        prompt = data.get("prompt", "").strip()
        answers = data.get("answers", {})
        refine = data.get("refine", False)
        api_key = data.get("api_key", "").strip()
        
        if not prompt:
            return jsonify({"error": "Original prompt is required"}), 400
            
        # 1. Build structured prompt
        assembled_prompt = build_prompt(prompt, answers)
        
        # 2. Refine prompt if requested
        refined_prompt = None
        explanation = None
        gemini_error = None
        
        if refine:
            res_str = enhance_prompt(assembled_prompt)
            if res_str.startswith("[OFFLINE MODE]"):
                refined_prompt = res_str
                gemini_error = "Local Ollama service is offline. A fallback mock response was generated."
            else:
                refined_prompt = res_str
                explanation = "Optimized using local Ollama model (llama3)."
                
        return jsonify({
            "assembled_prompt": assembled_prompt,
            "refined_prompt": refined_prompt,
            "explanation": explanation,
            "gemini_error": gemini_error
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    # Enable debugging for easier local development
    app.run(host="127.0.0.1", port=port, debug=True)
