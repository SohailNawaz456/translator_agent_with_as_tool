# 🌍 AI Translation Router with Agents

This project is a simple and modular AI translation system built with a multi-agent architecture. It routes translation requests to the appropriate language agent based on user input.

## 🚀 Features

- 🌐 Translates English text into:
  - Italian 🇮🇹
  - French 🇫🇷
  - German 🇩🇪
- 🧠 Uses a routing agent to automatically choose the correct translator
- 🔧 Built with `agents`, `Runner`, and `RunConfig` for easy extension

---

## 📦 Project Structure

```bash
.
├── agents/
│   └── # contains Agent and Runner classes
├── connection.py   # sets up model config
├── translator.py   # main logic with routing and translation agents
├── .env            # stores API keys securely
└── README.md       # you're here!

🛠️ Setup Instructions
1. Clone the repository

git clone https://github.com/yourusername/ai-translation-router.git
cd ai-translation-router

2. Install dependencies
Make sure you are using Python 3.9 or higher.
pip install -r requirements.txt
3. Add your API key
Create a .env file:

GEMINI_API_KEY=your-api-key-here
🧩 Code Overview
🔁 translator.py
Defines 3 translator agents and a central routing agent:


from agents import Agent, Runner
from connection import config

# Define individual language agents
italian_agent = Agent(...)
french_agent = Agent(...)
german_agent = Agent(...)

# Define router agent that delegates translation
translation_router = Agent(
    name="Translation Router",
    instructions="Route the request to the correct language agent...",
    tools=[italian_agent, french_agent, german_agent]
)

# Run example
result = Runner.run_sync(
    translation_router,
    "Translate 'I love learning' into Italian",
    run_config=config
)
print(result.final_output)

🧪 Example Output

Input: Translate 'I love learning' into Italian
Output: Amo imparare
📌 Notes
You can also directly run italian_agent, french_agent, or german_agent if you don't want to use the router.

Built to be easily extended to other languages like Spanish, Urdu, Arabic, etc.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

👨‍💻 Author
Made with ❤️ by Your Sohail


---

Let me know if you want:
- A `requirements.txt` file
- A `.env.example` template
- GitHub tags like `#ai`, `#langchain`, etc.

I'll generate those too.
