import datetime
import random
import re
import requests
from bs4 import BeautifulSoup
import urllib.parse
import wikipedia

try:
    import speech_recognition as sr
    VOICE_ENABLED = True
except ImportError:
    VOICE_ENABLED = False

try:
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    SPEECH_OUTPUT_ENABLED = True
except Exception:
    SPEECH_OUTPUT_ENABLED = False

# ==========================================
# 1. Output (Console and optional TTS)
# ==========================================
def assistant_speak(message):
    """Prints the message to the console and reads it aloud if TTS is enabled."""
    print(f"\nAssistant: {message}")
    if SPEECH_OUTPUT_ENABLED:
        try:
            engine.say(message)
            engine.runAndWait()
        except Exception:
            pass

# ==========================================
# 2. Internet Helpers (Web search & URL fetch)
# ==========================================
def web_search(query, max_results=3):
    """Use DuckDuckGo Instant Answer API to get a short summary and related topics."""
    try:
        params = {'q': query, 'format': 'json', 'no_html': 1, 'skip_disambig': 1}
        resp = requests.get('https://api.duckduckgo.com/', params=params, timeout=8)
        data = resp.json()
        abstract = data.get('AbstractText', '').strip()
        if abstract:
            return abstract

        # Fallback to RelatedTopics
        related = data.get('RelatedTopics', [])
        snippets = []
        for item in related[:max_results]:
            if isinstance(item, dict):
                text = item.get('Text') or item.get('Result') or ''
                if text:
                    snippets.append(text)
        if snippets:
            return '\n'.join(snippets[:max_results])
        return "No relevant results found from the search query."
    except Exception:
        return "Web search failed due to a network connection issue."


def fetch_url_content(url, max_chars=1000):
    """Fetch a URL and return a short plain-text summary (first paragraphs)."""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (assistant)'}
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')
        
        # Extract visible paragraph text from the HTML
        paragraphs = [p.get_text(separator=' ', strip=True) for p in soup.find_all('p')]
        text = '\n\n'.join([p for p in paragraphs if p])
        if not text:
            # Fallback: strip HTML tags manually
            text = re.sub(r'<[^>]+>', '', resp.text)
        return text[:max_chars] + ("..." if len(text) > max_chars else "")
    except Exception as exc:
        return f"Could not fetch content from URL: {exc}"

# ==========================================
# 3. Text Normalization
# ==========================================
def clean_text(text):
    """Tokenizes text and filters out common stop words."""
    words = re.findall(r"\w+", text.lower())
    stopwords = {
        'is', 'a', 'the', 'an', 'please', 'can', 'you', 'me', 'tell',
        'what', 'who', 'show', 'give', 'get', 'look', 'up', 'for', 'search',
        'do', 'does', 'did', 'find', 'about', 'on', 'in', 'of', 'and', 'to',
        'it', 'that', 'i', 'my', 'your', 'help', 'commands', 'today', 'now', 'tomorrow'
    }
    return [w for w in words if w not in stopwords]

# ==========================================
# 4. Safe Evaluation (Basic Calculator)
# ==========================================
def safe_eval(expr):
    """Safely evaluates basic mathematical expressions."""
    expr = expr.replace('x', '*').replace('X', '*')
    expr = re.sub(r'[^0-9\.\+\-\*\/\%\(\) ]', '', expr)
    return eval(expr, {'__builtins__': None}, {})

# ==========================================
# 5. Intent Classification
# ==========================================
def check_intent(keywords, raw_text):
    """Classifies the user intent based on keywords and raw text, then triggers actions."""
    text = raw_text.lower()

    # If the raw text is empty, prompt the user. Do not rely exclusively on keywords.
    if not raw_text or not raw_text.strip():
        assistant_speak("Please say or type something. If you need assistance, please type 'help'.")
        return True

    if any(word in text for word in ['help', 'commands', 'what can you do', 'options']):
        assistant_speak(
            "I can assist you with: hello, time, date, wikipedia <topic>, calculate <expression>, joke, help, and exit.\n"
            "You can also type 'voice' to initiate voice-activated input."
        )
        return True

    if any(word in text for word in ['hello', 'hi', 'hey', 'greetings', 'bot']):
        assistant_speak("Hello! I am your virtual assistant. How can I help you today?")
        return True

    if any(word in text for word in ['time', 'current time', 'what time']):
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        assistant_speak(f"The current time is {current_time}.")
        return True

    if any(word in text for word in ['date', 'today']) and ('date' in keywords or 'today' in keywords):
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        assistant_speak(f"Today's date is {current_date}.")
        return True

    if 'calculate' in text or 'what is' in text or "what's" in text or 'solve' in text or 'evaluate' in text or re.search(r'[0-9]+\s*[\+\-\*\/]', text):
        expression = text
        for prefix in ['calculate', 'what is', "what's", 'solve', 'evaluate']:
            expression = expression.replace(prefix, '')
        expression = expression.strip()
        if expression == '':
            assistant_speak('What would you like me to calculate?')
            return True
        try:
            result = safe_eval(expression)
            assistant_speak(f"{expression} = {result}")
        except Exception:
            assistant_speak("I am sorry, I could not process or understand that calculation.")
        return True

    if 'wikipedia' in text or 'who is' in text or 'what is' in text or 'about' in text:
        assistant_speak('Searching Wikipedia...')
        search_query = text
        for phrase in ['wikipedia', 'tell me about', 'who is', 'what is', 'about']:
            search_query = search_query.replace(phrase, '')
        search_query = search_query.strip()
        if not search_query:
            search_query = raw_text
        try:
            result = wikipedia.summary(search_query, sentences=2)
            assistant_speak(result)
        except wikipedia.exceptions.DisambiguationError:
            assistant_speak('This topic contains multiple definitions. Please be more specific.')
        except wikipedia.exceptions.PageError:
            assistant_speak('I am sorry, no matching page was found on Wikipedia.')
        except Exception:
            assistant_speak('There is an issue connecting to Wikipedia or the internet.')
        return True

    if any(word in text for word in ['search', 'web', 'look up']) or text.startswith('search for'):
        # Web search via DuckDuckGo Instant Answer API
        query = text
        for prefix in ['search for', 'search', 'find', 'look up', 'web']:
            query = query.replace(prefix, '')
        query = query.strip()
        if not query:
            assistant_speak('What would you like me to search for?')
            return True
        assistant_speak(f'Searching the web for: {query}')
        result = web_search(query)
        assistant_speak(result)
        return True

    if text.startswith('open ') or text.startswith('fetch ') or text.startswith('visit '):
        # Attempt to fetch a URL or treat it as a fallback search term
        target = text.split(' ', 1)[1].strip()
        # If it does not look like a URL, execute a web search fallback
        if not target.startswith('http'):
            assistant_speak(f"Treating '{target}' as a search query. Fetching web results...")
            search_result = web_search(target)
            assistant_speak(search_result)
            return True
        assistant_speak(f'Fetching content from: {target}')
        content = fetch_url_content(target, max_chars=1500)
        assistant_speak(content)
        return True

    if any(word in text for word in ['joke', 'funny', 'humor']):
        jokes = [
            'Why do programmers prefer dark mode? Because light attracts bugs!',
            'Your virtual assistant is ready and fully operational. Please let me know how I can help.',
            'There are 10 types of people in the world: those who understand binary, and those who don\'t.'
        ]
        assistant_speak(random.choice(jokes))
        return True

    if any(word in text for word in ['exit', 'quit', 'stop', 'bye', 'goodbye']):
        assistant_speak('Goodbye! Have a great day.')
        return False

    assistant_speak("I am sorry, I did not recognize that command. Please type 'help' to see available options.")
    return True

# ==========================================
# 6. Voice Input Helper (Microphone)
# ==========================================
def get_voice_command():
    """Captures speech from the microphone and converts it to string format via Google Speech Recognition."""
    if not VOICE_ENABLED:
        assistant_speak("Voice support is currently unavailable. Please install the 'SpeechRecognition' library.")
        return ''

    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            assistant_speak('Listening... Please speak now.')
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        voice_text = recognizer.recognize_google(audio, language='en-US')
        print(f"You (voice): {voice_text}")
        return voice_text
    except sr.WaitTimeoutError:
        assistant_speak('Listening timed out. Please try again.')
    except sr.UnknownValueError:
        assistant_speak('I am sorry, I could not understand or decode your audio.')
    except sr.RequestError:
        assistant_speak('The voice service is currently unavailable. Please verify your internet connection.')
    except Exception as exc:
        assistant_speak(f'Voice input error encountered: {exc}')
    return ''

# ==========================================
# 7. Main Loop
# ==========================================
if __name__ == '__main__':
    assistant_speak('The NLP Assistant is now initialized. You may enter text commands or use voice input.')
    assistant_speak("To close the assistant, type 'exit', 'stop', or 'bye'. Type 'help' to review configuration instructions.")

    is_running = True
    while is_running:
        user_input = input('\nYou (type text or "voice" for microphone input): ')
        if user_input.strip().lower() in ['voice', 'mic', 'listen', 'audio']:
            user_input = get_voice_command()
            if user_input.strip() == '':
                continue

        if user_input.strip() != '':
            extracted_keywords = clean_text(user_input)
            print(f"[NLP Debug] Extracted Keywords: {extracted_keywords}")
            is_running = check_intent(extracted_keywords, user_input)