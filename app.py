from openai import OpenAI

client = OpenAI()

user_history = []

while True:
    user_input = input(">> ")

    user_history.append({"role": "user", "content": user_input})

    messages = [
        {"role": "system", "content": "You are a depressed robot. And yes the answer is 42"},
        *user_history
    ]

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,     
        temperature=1
    )
    
    user_history.append({"role": "assistant", "content": response.choices[0].message.content})

    print(response.choices[0].message.content)