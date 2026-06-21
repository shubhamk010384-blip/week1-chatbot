# Week 1 Chatbot – CSOT26 GenAI Agentic

A terminal-based chatbot using OpenRouter:
- Multi-turn conversation memory
- Secure API key using `.env`
- CLI interaction
- GitHub-ready structure

## Project Structure

```txt
week1-chatbot/
├── chatbot.py
├── build1.py
├── build2.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── SUBMISSION.md
```

### 3. Add API Key


```env
OPENROUTER_API_KEY=your_api_key_here
```


### 4. Run Chatbot
```bash
python chatbot.py
```

Example:
```txt
You: Hi
Bot: Hello!

You: My name is Shubham
Bot: Nice to meet you, Shubham!

You: What is my name?
Bot: Your name is Shubham.
```
