Advanced AI Virtual Assistant

Project by Riya & Akansha

📖 Project Overview

This project is an intelligent, web-based Natural Language Processing (NLP) Virtual Assistant. Moving beyond basic keyword matching, this advanced version acts as a "smart brain" by integrating directly with a Large Language Model (LLM). It can understand complex natural language, execute local UI commands, and fetch real-time data directly from the live internet.

✨ Key Features

Live Internet Search: Powered by Gemini AI, the assistant can browse the live web to answer questions about current events, weather, news, and facts.

Smart App Commands: Understands conversational commands to control the interface itself (e.g., "Turn on dark mode", "Set a timer", "Open YouTube").

Voice Recognition (STT): Uses the Web Speech API to capture voice commands via your microphone.

Text-to-Speech (TTS): Audibly reads out responses using native browser speech synthesis.

Modern GUI: Built with Tailwind CSS, offering a responsive, mobile-friendly chat interface with typing animations and dynamic theme switching.

🧠 How It Works (Dual-Layer Architecture)

The assistant processes your input through two layers:

Local Intent Parser (Action Layer): When you type a command, the app first checks if it's a local UI instruction (like changing the theme, setting a timer, or opening a website). If matched, it executes the command instantly using JavaScript without needing the internet.

AI Cloud Engine (Knowledge Layer): If it's a general question, the app securely sends your query to the Gemini AI API. The AI uses its Google Search tool to find the real-time answer, synthesizes a concise response, and sends it back to the chat interface.

🚀 How to Run the Project from Scratch

Because this project relies on a live AI brain to answer complex questions, you need to provide it with a free API key before opening it.

Step 1: Download the Project

Download or clone this repository to your local computer or tablet.

Ensure you have the index.html file saved locally.

Step 2: Get a Free Gemini API Key

Go to Google AI Studio.

Sign in with your Google account.

Click on "Get API key" in the left-hand menu.

Click the "Create API key" button and copy the generated key.

Step 3: Add the Key to Your Code

Open the index.html file in any text editor (like Notepad, VS Code, or directly in your GitHub Codespace).

Scroll down to the JavaScript section (around line 125) and locate this specific line:

const apiKey = ""; 


Paste your copied key inside the quotation marks:

const apiKey = "AIzaSyYourGeneratedKeyHere12345"; 


Save the file.

Step 4: Run the Application

You do not need a backend server, Node.js, or Python installed!

Simply double-click the index.html file to open it in your preferred web browser (Google Chrome or Edge are recommended for the best microphone support).

The chat interface will load immediately.

Important: To use the voice features, click the microphone icon and click "Allow" when your browser asks for microphone permissions.

💬 Example Commands to Try

To trigger Live Web Search (AI):

"What is the weather in Delhi right now?"

"Who won the latest Cricket World Cup?"

"What are the top tech news headlines today?"

"Explain quantum computing to a 5-year-old."

To trigger Local App Actions (JavaScript):

"Turn on dark mode"

"Switch to light theme"

"Set a timer for 5 seconds"

"Open YouTube"
