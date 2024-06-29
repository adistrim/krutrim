from openai import OpenAI
  
openai = OpenAI(
    api_key="",
    base_url="https://cloud.olakrutrim.com/v1",
)

chat_completion = openai.chat.completions.create(
    model="Krutrim-spectre-v2",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello"}
    ]
)

print(chat_completion.choices[0].message.content)
