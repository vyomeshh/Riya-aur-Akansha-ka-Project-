Advanced NLP Web Assistant

Project by Riya & Akansha

📖 Project Overview

This project is an intelligent, web-based Natural Language Processing (NLP) Virtual Assistant. Moving beyond basic keyword matching, this advanced version acts as a "smart brain" by integrating directly with a Large Language Model (LLM). It can understand complex natural language, execute local system commands, and fetch real-time data directly from the live internet.

✨ Key Features

Live Internet Search: Powered by AI grounding, the assistant can browse the live web to answer questions about current events, weather, news, and facts.

Smart App Commands: Understands commands to control the interface itself (e.g., "Turn on dark mode", "Set a timer").

Speech-to-Text (STT): Uses the Web Speech API to capture voice commands via the microphone.

Text-to-Speech (TTS): Audibly reads out responses using the native browser speech synthesis.

Modern GUI: Built with Tailwind CSS, offering a responsive, mobile-friendly chat interface with typing animations and dynamic theme switching.

🧠 How It Works

The assistant uses a Dual-Layer Architecture:

Local Intent Parser (Doing Stuff): When you type a command, the app first checks if it's a local UI instruction (like changing to dark mode or opening YouTube). If matched, it executes the command instantly using JavaScript.

AI Cloud Engine (Answering Stuff): If it's a general question, the app securely sends your query to the Gemini AI API. The AI uses its Google Search tool to find the real-time answer, synthesizes a concise response, and sends it back to the chat interface.

🚀 How to Run the Project from Scratch

Because this project relies on a live AI brain, you need to provide it with a free API key before opening it.

Step 1: Get a Free API Key

Go to Google AI Studio.

Sign in with your Google account.

Click on "Get API key" in the left menu and create a new key.

Copy the generated key.

Step 2: Add the Key to Your Code

Open the index.html file in any text editor (like Notepad, VS Code, or GitHub Codespaces).

Scroll down to the JavaScript section (around line 110) and find this line:

const apiKey = ""; 


Paste your key inside the quotation marks:

const apiKey = "AIzaSyYourGeneratedKeyHere12345"; 


Save the file.

Step 3: Run the App

You do not need a server or Python installed. Simply double-click the index.html file to open it in your preferred web browser (Google Chrome is recommended for the best voice recognition support).

The interface will load immediately.

Important: To use the voice features, click the microphone icon and click "Allow" when your browser asks for microphone permissions.

💬 Example Commands to Try

To trigger Live Web Search:

"What is the weather in Delhi right now?"

"Who won the latest Cricket World Cup?"

"What are the top tech news headlines today?"

To trigger Local App Commands:

"Turn on dark mode"

"Switch to light theme"

"Set a timer for 5 seconds"

"Open YouTube"
