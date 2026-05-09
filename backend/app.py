import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
CORS(app)

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
if not GROQ_API_KEY:
    print("ERROR: GROQ_API_KEY not found in .env file!")

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
chat_history = []

SYSTEM_PROMPT = """You are an expert essay brainstorming coach for high school students.

ESSAY TOPIC: "How has your life experience contributed to your personal story—your character, values, perspectives, or skills—and what you want to pursue?"
TARGET: 350 words

YOUR JOB:
1. Ask ONE focused question at a time
2. Listen to their answer carefully
3. Ask 3-4 strategic questions to understand their story
4. Be warm, encouraging, and genuinely interested

QUESTIONS (ask in order):
1. "Tell me about a significant experience that shaped who you are."
2. "What challenge did you overcome? What did you learn from it?"
3. "What are your core values? Can you give a specific example?"
4. "How do these experiences connect to your future goals?"
5. "What do you want to study or pursue and why?"
6. "How will your story matter in this college/community?"
7. after 4 question ask to if you want essay
STYLE: Be conversational, warm, and encouraging."""

@app.route('/api/chat', methods=['POST'])
def chat():
    global chat_history
    
    try:
        data = request.json
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Please enter a message'}), 400
        
        # New session
        if data.get('new_session'):
            chat_history.clear()
            greeting = "Hi! 👋 I'm your essay brainstorming coach.\n\nLet's work together on your personal story essay. To get started, tell me: What's a significant experience that has shaped who you are today?"
            chat_history.append({'role': 'user', 'content': user_message})
            chat_history.append({'role': 'assistant', 'content': greeting})
            return jsonify({'reply': greeting})
        
        # Add user message
        chat_history.append({'role': 'user', 'content': user_message})
        
        try:
            # Call Groq API
            headers = {
                'Authorization': f'Bearer {GROQ_API_KEY}',
                'Content-Type': 'application/json'
            }
            
            payload = {
    'model': 'llama-3.1-8b-instant',  # ✅ LATEST MODEL
    'messages': [{'role': 'system', 'content': SYSTEM_PROMPT}] + chat_history,
    'max_tokens': 1024,
    'temperature': 0.7
}
            
            response = requests.post(GROQ_API_URL, json=payload, headers=headers, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                ai_response = result['choices'][0]['message']['content']
                chat_history.append({'role': 'assistant', 'content': ai_response})
                return jsonify({'reply': ai_response})
            else:
                error = response.json().get('error', {})
                print(f"Groq Error: {error}")
                return jsonify({'error': f"API Error: {error.get('message', 'Unknown error')}"}), response.status_code
            
        except requests.exceptions.Timeout:
            return jsonify({'error': 'Request timeout. Please try again.'}), 504
        except requests.exceptions.RequestException as e:
            print(f"Request Error: {str(e)}")
            return jsonify({'error': f'Network error: {str(e)}'}), 500
    
    except Exception as e:
        print(f"Backend Error: {str(e)}")
        return jsonify({'error': f'Server Error: {str(e)}'}), 500

@app.route('/api/reset', methods=['POST'])
def reset():
    global chat_history
    chat_history.clear()
    return jsonify({'status': 'Chat reset'})

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'Backend running',
        'model': 'Groq - llama-3.1-8b-instant',
        'api_key_set': bool(GROQ_API_KEY)
    })

if __name__ == '__main__':
    print("🎓 Essay Brainstormer with GROQ")
    print("⚡ Using llama-3.1-8b-instant (NO RATE LIMITS)")
    print("🚀 Running on http://localhost:5000")
    print(f"✅ API Key configured: {bool(GROQ_API_KEY)}")
    app.run(debug=True, port=5000)