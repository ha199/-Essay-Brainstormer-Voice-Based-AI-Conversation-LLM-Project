import React, { useState, useRef, useEffect } from 'react'
import './App.css'

export default function App() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const [isListening, setIsListening] = useState(false)
  const [loading, setLoading] = useState(false)
  const recognitionRef = useRef(null)
  const messagesEndRef = useRef(null)

  useEffect(() => {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition
    if (SpeechRecognition) {
      recognitionRef.current = new SpeechRecognition()
      recognitionRef.current.continuous = false
      recognitionRef.current.interimResults = true
      recognitionRef.current.lang = 'en-US'
      recognitionRef.current.onstart = () => setIsListening(true)
      recognitionRef.current.onend = () => setIsListening(false)
      recognitionRef.current.onresult = (event) => {
        for (let i = event.resultIndex; i < event.results.length; i++) {
          const transcript = event.results[i][0].transcript
          if (event.results[i].isFinal) {
            setInput(prev => prev + transcript)
          }
        }
      }
    }
  }, [])

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  const speak = (text) => {
    const utterance = new SpeechSynthesisUtterance(text)
    utterance.rate = 1.5
    window.speechSynthesis.cancel()
    window.speechSynthesis.speak(utterance)
  }

  const sendMessage = async () => {
    if (!input.trim()) return
    const userMsg = input
    setInput('')
    setMessages(prev => [...prev, { role: 'user', text: userMsg }])
    setLoading(true)

    try {
      const res = await fetch('http://localhost:5000/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userMsg, new_session: messages.length === 0 })
      })
      const data = await res.json()
      const reply = data.reply || 'Error'
      setMessages(prev => [...prev, { role: 'assistant', text: reply }])
      speak(reply)
    } catch (err) {
      setMessages(prev => [...prev, { role: 'assistant', text: 'Backend error' }])
    }
    setLoading(false)
  }

  return (
    <div className="app">
      <div className="header">
        <h1>🎤 Voice Chat with Brainstormer </h1>
        <p>Speak or type to chat</p>
      </div>
      <div className="messages">
        {messages.length === 0 && (
          <div className="empty">
            <div className="empty-icon">🎙️</div>
            <p>Start by clicking the mic or typing</p>
          </div>
        )}
        {messages.map((msg, i) => (
          <div key={i} className={`message ${msg.role}`}>
            <div className="message-content">{msg.text}</div>
          </div>
        ))}
        {loading && (
          <div className="message assistant">
            <div className="typing"><span></span><span></span><span></span></div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>
      <div className="input-area">
        <input type="text" value={input} onChange={(e) => setInput(e.target.value)} onKeyPress={(e) => e.key === 'Enter' && sendMessage()} placeholder="Type or speak..." disabled={loading} />
        <button onClick={() => { if (isListening) recognitionRef.current?.stop(); else recognitionRef.current?.start() }} className={isListening ? 'record-btn active' : 'record-btn'} disabled={loading}>{isListening ? '⏹️' : '🎤'}</button>
        <button onClick={sendMessage} disabled={loading || !input.trim()} className="send-btn">Send</button>
      </div>
    </div>
  )
}