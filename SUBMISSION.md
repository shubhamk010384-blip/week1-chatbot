 Week 1 Submission Report – CSOT26 GenAI Agentic

**Name:** Shubham
**Task:** Week 1 – Terminal-Based Chatbot with Memory

---

## Objective

The objective of Week 1 was to build a terminal-based chatbot using a Large Language Model (LLM) API. The chatbot needed to support multi-turn conversations, securely manage API keys, and maintain conversation history for contextual responses.

---

## What I Built

I implemented a terminal-based chatbot using the **Google Gemini API** (`gemini-1.5-flash`) in Python. The chatbot allows users to have continuous conversations through the command line interface (CLI).

The chatbot supports:

* Multi-turn conversation memory
* Secure API key management using `.env`
* Command-line interaction
* Context-aware responses using chat history

---

## Technologies Used

* **Python** – Main programming language
* **Google Gemini API** – LLM used for chatbot responses
* **python-dotenv** – For securely loading API keys from environment variables
* **GitHub** – Version control and project hosting

---

## How I Decided to Implement the Task

I selected the **Gemini API** because it is easy to integrate with Python and provides fast response generation. It also offers a beginner-friendly setup for educational projects.

For implementation, I divided the task into smaller components:

1. **API Integration**
   First, I connected the chatbot to the Gemini API to generate responses.

2. **Secure API Key Handling**
   Instead of hardcoding API keys in the source code, I used a `.env` file and `python-dotenv`. This approach improves security and follows best development practices.

3. **Conversation Memory**
   To make the chatbot remember previous messages, I implemented a `chat_history` list. Each user message and model response is stored and passed again to the model, enabling contextual conversation.

4. **Terminal Interface**
   Since Week 1 required a CLI chatbot, I used Python’s `input()` and `print()` functions for interaction.

---

## Key Decisions and Why They Were Made

### 1. Why Gemini API?

I chose Gemini because:

* It is easy to set up
* Fast response generation
* Beginner-friendly documentation
* Suitable for educational AI projects

### 2. Why Use `.env`?

I used a `.env` file to securely store API keys. This prevents accidental exposure of credentials when uploading code to GitHub.

### 3. Why Store Chat History?

The chatbot required memory. Without storing history, the model would treat every question independently. By maintaining `chat_history`, the chatbot can understand context and respond more naturally.

### 4. Why Command Line Interface?

The Week 1 task specifically required a terminal chatbot, so I implemented interaction directly through the command line.

---

## Challenges Faced

Some challenges during implementation included:

* Understanding Gemini API integration
* Managing multi-turn memory correctly
* Keeping API keys secure while making the repository public

These challenges were solved using Gemini documentation, environment variables, and chat history implementation.

---

## Learning Outcomes

Through this task, I learned:

* How LLM APIs work
* How to send prompts and receive responses from AI models
* Secure API key management using `.env`
* Managing conversation history for contextual chatbots
* Using GitHub for project submission

---

## Conclusion

This project successfully fulfills the Week 1 requirements by implementing a secure, terminal-based chatbot with memory and multi-turn interaction using the Gemini API.
