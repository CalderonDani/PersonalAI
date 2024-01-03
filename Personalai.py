import os

from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
import openai

openai.api_key = openai_api_key

while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        

        prompt = f"You: {user_input}\nAI:"

        completion = openai.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        #0-1, higher gives a more random output, lower is more deterministic
        #temperature = 0.5
        
        max_tokens = 150,
        messages=
        [
            {
                "role": "user", 
                "content": "My name is Daniel, please use it from here on."
            },
            {
                "role": "user",
                "content": prompt
            }
            
        ],
    )
        ai_response = completion.choices[0].message.content.strip()
        
        print(f"Daniel's AI: {ai_response}")



