# 🧠 Essay Brainstormer AI

<p align="center">

AI-powered voice + text essay brainstorming assistant for students.

</p>

---

## ✨ Features

- 🎤 Voice Input & Voice Output
- ⌨️ Text Input Support
- 🤖 AI-Powered Essay Coaching
- 💬 Conversation History
- ⚡ Ultra-fast Responses using Groq
- 📱 Responsive Modern UI
- 🧠 Guided College Essay Brainstorming
- 🔊 Speech-to-Text + Text-to-Speech

---

# 📸 Preview

<img width="100%" alt="preview" src="https://via.placeholder.com/1200x600.png?text=Essay+Brainstormer+Preview">
<img width="1907" height="887" alt="image" src="https://github.com/user-attachments/assets/c51b8d8e-a6f4-4ce0-ba65-66160267208c" />
<img width="1917" height="878" alt="image" src="https://github.com/user-attachments/assets/02f57715-24c5-490a-a936-cb3b4621e5a5" />

---

# ⚙️ Tech Stack

| Frontend | Backend | AI |
|---|---|---|
| React 18 | Flask | Groq API |
| Vite | Python 3.8+ | Llama 3.1 |
| CSS3 | Flask-CORS | Speech AI |
| Web Speech API | python-dotenv | Fast Inference |

---

# 🚀 AI Model

```txt
Provider : Groq
Model    : llama-3.1-8b-instant
Speed    : Ultra Fast
Cost     : Free Tier
```

---

# 📂 Project Structure

```bash
essay-brainstormer/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── .env
│   └── venv/
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
├── .gitignore
└── README.md
```

---

# 🔑 Prerequisites

Before starting, install:

- Python 3.8+
- Node.js 16+
- Groq API Key
- Chrome / Edge browser

---

# 🛠️ Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/essay-brainstormer.git

cd essay-brainstormer
```

---

## 2️⃣ Backend Setup

```bash
cd backend

python -m venv venv
```

### Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Configure Environment Variables

Create `.env`

```env
GROQ_API_KEY=your_api_key_here
```

Get API Key from:

👉 https://console.groq.com

---

## 4️⃣ Start Backend

```bash
python app.py
```

Backend runs on:

```txt
http://localhost:5000
```

---

## 5️⃣ Frontend Setup

Open NEW terminal:

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```txt
http://localhost:5173
```

---

# 🎤 How It Works

1. User speaks or types
2. Speech converts to text
3. Frontend sends request to Flask backend
4. Backend calls Groq API
5. AI generates brainstorming response
6. Response appears as text + voice

---

# 🧠 Example Questions

The AI guides students using prompts like:

- Tell me about a meaningful experience.
- What challenge changed you?
- What are your core values?
- What motivates your future goals?
- Why this college or field?

---

# 🔒 Security Notes

## Never upload:

- `.env`
- `venv/`
- `node_modules/`

---

## Add this to `.gitignore`

```gitignore
venv/
node_modules/
.env
```

---

# 📦 API Endpoint

## POST `/api/brainstorm`

### Request

```json
{
  "text": "I want help brainstorming my college essay"
}
```

### Response

```json
{
  "result": "Tell me about a challenge you overcame..."
}
```

---

# 🎨 Future Improvements

- ✅ ChatGPT-style UI
- ✅ Streaming responses
- ✅ Authentication
- ✅ Essay export to PDF
- ✅ Dark mode
- ✅ Multi-language support
- ✅ Real-time websocket communication

---

# 📚 Documentation

- Groq Docs  
  https://console.groq.com/docs

- React Docs  
  https://react.dev

- Flask Docs  
  https://flask.palletsprojects.com

---

# 👨‍💻 Author

Developed using:

- React
- Flask
- Groq LLM API
- Web Speech API

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository  
🍴 Fork the project  
🧠 Contribute improvements

---

# 📄 License

MIT License
