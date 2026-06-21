 Week 1 Submission Report – CSOT26 GenAI Agentic

**Name:** Shubham
**Task:** Week 1 – Terminal-Based Chatbot with Memory

---

## Objective

The objective of Week 1 was to build a terminal-based chatbot using a Large Language Model (LLM) API. The chatbot needed to support multi-turn conversations, securely manage API keys, and maintain conversation history for contextual responses.

---

## What I Built

I implemented a terminal-based chatbot using the **OpenRouter API ** (free model) in Python. The chatbot allows users to have continuous conversations through the command line interface (CLI).

The chatbot supports:

* Multi-turn conversation memory
* Secure API key management using `.env`
* Command-line interaction
* Context-aware responses using chat history



## Additional Features Implemented

To improve the chatbot and satisfy the Week 1 requirements, I added the following features:

### ChatAgent Class

The chatbot logic is encapsulated inside a reusable `ChatAgent` class. The class manages conversation history, model configuration, and API communication.

### Model Selection Menu

Before starting the conversation, the user can choose between multiple OpenRouter models. This makes the chatbot more flexible and allows easy experimentation with different LLMs.

### Configurable Conversation Buffer

The chatbot supports a configurable `max_history_turns` parameter. This controls how many conversation turns are retained in memory.

### History Trimming

When the conversation exceeds the configured limit, older messages are automatically removed while preserving the system prompt. This prevents the conversation history from growing indefinitely.

### Standalone Build Scripts

Two additional scripts were created:

* `build1.py` – Performs a single-turn API call and prints the raw response object.
* `build2.py` – Demonstrates response parsing and prints both the generated text and the full response object.


---

## Technologies Used

* **Python** – Main programming language
* **OpenRouter API** – LLM used for chatbot responses
* **python-dotenv** – For securely loading API keys from environment variables
* **GitHub** – Version control and project hosting

---

## How I Decided to Implement the Task

I selected the **Free OpenRouter model** because it is easy to integrate with Python and provides fast response generation. It also offers a beginner-friendly setup for educational projects.

For implementation, I divided the task into smaller components:

1. **API Integration**
   First, I connected the chatbot to the OpenRouter API to generate responses.

2. **Secure API Key Handling**
   Instead of hardcoding API keys in the source code, I used a `.env` file and `python-dotenv`. This approach improves security and follows best development practices.

3. **Conversation Memory**
   To make the chatbot remember previous messages, I implemented conversation memory inside a reusable `ChatAgent` class. The class stores user and assistant messages, manages conversation history, and automatically trims older messages when the configured history limit is exceeded.

4. **Terminal Interface**
   Since Week 1 required a CLI chatbot, I used Python’s `input()` and `print()` functions for interaction.

---

## Key Decisions and Why They Were Made

### 1. Why OpenRouter API?

I chose OpenRouter because:

* It is easy to set up
* Fast response generation
* Beginner-friendly documentation
* Suitable for educational AI projects

### 2. Why Use `.env`?

I used a `.env` file to securely store API keys. This prevents accidental exposure of credentials when uploading code to GitHub.

### 3. Why Store Chat History?

The chatbot required memory. Without storing history, the model would treat every question independently. By maintaining conversation history inside the `ChatAgent` class, the chatbot can understand context, provide more natural responses, and preserve relevant information across multiple turns.

### 4. Why Command Line Interface?

The Week 1 task specifically required a terminal chatbot, so I implemented interaction directly through the command line.

---

## Challenges Faced

Some challenges during implementation included:

* Understanding OpenRouter API integration
* Managing multi-turn memory correctly
* Keeping API keys secure while making the repository public

These challenges were solved using OpenRouter documentation, environment variables, and chat history implementation.

---

## Learning Outcomes

* Designing reusable software using Python classes
* Managing conversation context with bounded memory
* Implementing configurable chatbot settings
* Structuring AI projects with multiple utility scripts


Through this task, I learned:

* How LLM APIs work
* How to send prompts and receive responses from AI models
* Secure API key management using `.env`
* Managing conversation history for contextual chatbots
* Using GitHub for project submission

---

## Conclusion

This project fulfills the Week 1 requirements by implementing a terminal-based chatbot with a reusable ChatAgent class, model selection, configurable conversation memory, secure API key management, standalone build scripts, and multi-turn interaction using the OpenRouter API.
