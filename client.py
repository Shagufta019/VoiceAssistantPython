from groq import Groq
import creds

# pip install Groq 

# This will store the conversation history globally in memory
chat_history = [
    {"role": "system", "content": "You are Jarvis, a virtual voice assistance like Alexa. Provide answers that are concise but informative, avoid one-word answers, but don't give long paragraphs. Keep responses concise but informative, not too short and not too long."}
]

def aiProcess(command):
    global chat_history
    
    client = Groq(api_key=f"{creds.groqapi}")
    
    # Add the user's new command to the history
    chat_history.append({"role": "user", "content": command})

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=chat_history
        )
        
        response = completion.choices[0].message.content
        
        # Save Jarvis's reply to the history so he remembers what he said
        chat_history.append({"role": "assistant", "content": response})
        
        # Keep the history reasonably short to avoid exceeding API token limits 
        # (keeps the system prompt at index 0, and the last 10 messages)
        if len(chat_history) > 11:
            chat_history = [chat_history[0]] + chat_history[-10:]
            
        return response
    except Exception as e:
        return f"Sorry, I ran into an error connecting to my brain. {str(e)}"
