import os
import openai

openai.api_key = "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"



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
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
        ai_response = completion.choices[0].message.content.strip()
        print(f"Daniel's AI: {ai_response}")


