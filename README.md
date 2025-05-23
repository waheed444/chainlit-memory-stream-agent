# Chainlit Memory Stream Agent: Your Gemini-Powered AI Chatbot 🤖💬

<p align="center">
  <a href="https://github.com/waheed444/chainlit-memory-stream-agent">
    <img src="https://img.shields.io/github/stars/waheed444/chainlit-memory-stream-agent?style=social" alt="GitHub stars">
  </a>
  <a href="https://github.com/waheed444/chainlit-memory-stream-agent">
    <img src="https://img.shields.io/github/forks/waheed444/chainlit-memory-stream-agent?style=social" alt="GitHub forks">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/python-3.9%2B-blue.svg" alt="Python Version">
  </a>
  <a href="https://docs.chainlit.io">
    <img src="https://img.shields.io/badge/Built%20with-Chainlit-764abc.svg" alt="Chainlit">
  </a>
  <a href="https://github.com/openai/openai-agents">
    <img src="https://img.shields.io/badge/OpenAI-Agent%20SDK-brightgreen.svg" alt="OpenAI Agent SDK">
  </a>
  <a href="https://git-scm.com/">
    <img src="https://img.shields.io/badge/version-control-Git-orange.svg" alt="Git">
  </a>
  <a href="https://makersuite.google.com/app/apikey">
    <img src="https://img.shields.io/badge/API-Gemini%20Key-yellow.svg" alt="Gemini API Key">
  </a>
  <a href="https://github.com/waheed444/chainlit-memory-stream-agent/fork">
    <img src="https://img.shields.io/badge/Contribute-Fork%20repo-blue.svg" alt="Fork">
  </a>
  <a href="https://github.com/waheed444/chainlit-memory-stream-agent/stargazers">
    <img src="https://img.shields.io/badge/Support-Give%20a%20Star-yellow.svg" alt="Star">
  </a>
</p>



A powerful AI assistant built with **Chainlit** and the **OpenAI Agent SDK**, leveraging the capabilities of **Google Gemini models**. This project boasts **real-time streaming responses** and maintains **persistent chat history**, providing a seamless ChatGPT-like experience within your own custom AI application.




##  Prerequisites ✅

Before running this project, ensure you have the following tools, libraries, and API keys properly configured:

| Tool / Library        | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| 🐍 Python 3.9+         | Required for running the application and libraries                         |
| 🧬 Chainlit            | Framework for building conversational UIs with LLMs                         |
| 🧠 OpenAI Agent SDK    | Enables agent orchestration and streaming capabilities                     |
| 🌐 Git                 | Version control for cloning and managing the project repository            |
| 🔑 Google Gemini API   | [Get API Key](https://makersuite.google.com/app/apikey) for Gemini models  |
| 🔑 OpenAI API Key      | [Get API Key](https://platform.openai.com/account/api-keys) for streaming  |
| 📦 dotenv              | For managing environment variables securely                                |
| 🧪  VS Code   | Recommended code editor for development                                    |

---


## Features ✨

* 🔄 **Real-time Token Streaming:** Experience the fluidity of ChatGPT-like responses.
* 🧠 **Persistent Memory:**  Maintain context across your conversations, ensuring your AI assistant remembers previous interactions.
* 🔗 **Chainlit Integration:**  Leverage Chainlit's ease of use for rapid UI development and deployment.
* 🤖 **Gemini Power:**  Utilize the cutting-edge capabilities of the `gemini-2.0-flash` model.
* 🧰 **OpenAI Agent SDK Integration:**  Benefit from the robust features and flexibility of the OpenAI Agent SDK.
* 🔐 **Secure API Key Management:**  Safely manage your API keys using a `.env` file.
* 🚀 **Developer-Friendly Codebase:**  A modular and well-structured Python codebase, making it easy to extend and customize.


## ⚙️ Installation Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/waheed444/chainlit-memory-stream-agent.git
   cd chainlit-memory-stream-agent
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

```bash
pip install openai-agents chainlit
       # for UV User's
uv add openai-agents chainlit
```

4. **Configure API keys:** Create a `.env` file in the root directory and add your API keys:

 - > 📌 Make sure to store your API keys securely in a `.env` file in the root directory:


```bash
GEMINI_API_KEY = paste_your_gemini_api_key_here
               # OR
OPENAI_API_KEY = paste_your_openai_api_key_here
```

5. **Run the App:**

   ```bash
   chainlit run agent.py
   ```

   **(Note: You need to have `chainlit` installed.  Install it via `pip install chainlit` if not already present.)**


## Usage Instructions 🗣️

### Usage Examples

Start the Chat UI: Once Chainlit is running, open the local URL provided in your terminal and start chatting with your AI assistant.


Ask questions like:

```kotlin
Who was the founder of Pakistan?
Summarize the history of Python in 3 lines.
What’s the latest in AI this year?
```

Enjoy token-by-token responses with context-aware answers based on your previous messages.


💡 You can customize the agent's behavior, memory strategy, or switch between Gemini and OpenAI models by modifying the `app.py` and `stream.py` files.

## Contributing


We welcome contributions to improve this project! Please follow these steps:

1. **Fork** the repository.
2. **Create a new branch:** `git checkout -b feature-name`
3. **Make your changes** and ensure they adhere to the project's coding style and best practices.
4. **Commit your changes:** `git commit -m "Add feature"`
5. **Push to the branch:** `git push origin feature-name`
6. **Submit a pull request** with a clear description of your changes and their benefits.
If you find any issues or want to improve this project, feel free to open a [GitHub issue]([![License](https://img.shields.io/badge/License-MIT-blue.svg)https://github.com/waheed444/Chainlit-AiAgent/issues) or submit a pull request.

This repo is only for learning and exploring new things, feel free to fork it, explore, or give suggestions!

**Star ⭐ the repo if it helps you!**

---


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙌 Let's Connect

<p align="left">
  <a href="https://www.linkedin.com/in/waheed444/?originalSubdomain=pk)" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-blue?style=flat-square&logo=linkedin" alt="LinkedIn">
  </a>
  <a href="https://github.com/waheed444" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub">
  </a>
  <a href="waheedahmad5519@gmail.com" target="_blank">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Gmail">
  </a>
</p>

---
