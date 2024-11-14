import React, { useState } from 'react';
import '../css/chatbot.css';


const Chatbot = () => {
    const [messages, setMessages] = useState([
        { text: "Hola! En que puedo ayudarte hoy", sender: "bot" },
    ]);

    const [input, setInput] = useState('');

    const handleCreateConsult = (prompt) => {
        fetch('http://localhost:3000/query', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 
                code: `${prompt}`, 
            }),
        })
            .then((response) => response.json())
            .then((data) => {
                setMessages([...messages, { text: data.message.content, sender: "bot" }]);
                setMessages((prev) => [...prev, { text: data.message.content, sender: "bot" }]);
            })
            .catch((error) => {
                console.log(prompt);
                console.error('Error:', error);
        })
    }

    const handleSendMessage = () => {
        if (input.trim()) {
            setMessages([...messages, { text: input, sender: "user" }]);
            handleCreateConsult(`${input}`);
            setInput('');
        }
    };

    const handleKeyDown = (e) => {
        if (e.key === 'Enter') {
            handleSendMessage();
        }
    };

    return (
            <div className="chat-container">
                <div className="chat-window col-12">
                    {messages.map((message, index) => (
                        <div key={index} className={`chat-message ${message.sender}`}>
                            {message.text}
                        </div>
                    ))}
                </div>
                <div className="chat-input-container">
                    <input
                        type="text"
                        value={input}
                        onChange={(e) => setInput(e.target.value)}
                        onKeyDown={handleKeyDown} 
                        placeholder="Escribe tu mensaje..."
                    />
                    <button onClick={handleSendMessage}>Enviar</button>
                </div>
            </div>
    );
};

export default Chatbot;
