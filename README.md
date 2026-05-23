NLP Web Assistant

Project by Riya & Akansha

📖 Project Overview

This project is an interactive, web-based Natural Language Processing (NLP) Virtual Assistant. It is designed to understand natural language commands, filter out noise (stopwords), and execute specific intents. The assistant features a modern, mobile-friendly Graphical User Interface (GUI) and supports both text and voice inputs directly within the browser.

✨ Features

Speech-to-Text (STT): Uses the browser's native Web Speech API to capture voice commands via the microphone.

Text-to-Speech (TTS): Audibly reads out responses using the window.speechSynthesis API.

NLP Pipeline: Tokenizes user input and removes common English stopwords to identify the core intent of the command.

Knowledge Retrieval: Integrates with the Wikipedia REST API to fetch and summarize information dynamically.

Mathematical Evaluator: Safely calculates math equations and expressions provided by the user.

Time & Date Tracking: Provides real-time system clock and date information.

Responsive GUI: Built with Tailwind CSS, ensuring the chat interface looks great on both desktops and mobile devices.

🛠️ Technologies Used

Frontend: HTML5, JavaScript (ES6)

Styling: Tailwind CSS (via CDN)

APIs:

Wikipedia REST API (for knowledge retrieval)

Web Speech API (for STT and TTS capabilities)

🚀 How to Run the Project

Because this is a pure HTML/JavaScript application, it requires zero setup or server installations.

Download or clone this repository.

Ensure you have the index.html file on your device.

Simply double-click index.html to open it in any modern web browser (Google Chrome, Safari, Edge, or Firefox).

Note for Voice Features: To use the microphone button, ensure your browser has permission to access your microphone. (Voice recognition works best on Google Chrome).

💬 Command Examples

Try typing or saying these commands to interact with the assistant:

Intent

Example Commands

Greeting

"Hello", "Hi", "Hey assistant"

Time

"What time is it?", "Tell me the time"

Date

"What is today's date?", "Date today"

Calculate

"Calculate 5 * 20", "What is 100 / 4"

Wikipedia

"Wikipedia Python programming", "Tell me about Black Holes"

Entertainment

"Tell me a joke", "Funny"

🧠 How the NLP Logic Works

The project uses a lightweight JavaScript replica of a standard Python NLP pipeline:

Normalization: The user's input is converted to lowercase.

Tokenization: The string is split into an array of individual words using Regular Expressions (match(/\w+/g)).

Stopword Filtering: Filler words (e.g., "is", "the", "please", "tell") are removed using a predefined array, leaving only high-value keywords.

Intent Classification: The system scans the remaining keywords to trigger the appropriate response block (e.g., if the keyword "time" remains, it triggers the time function).
