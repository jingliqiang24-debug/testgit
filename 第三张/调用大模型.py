# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI
import streamlit

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")
messages =[{"role": "system", "content": "You are a helpful assistant"},]
while True:
    question = input("请输入你的问题")
    messages.append({"role": "user", "content": f"{question}"})
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages = messages,
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )
    assistant_message = response.choices[0].message.content
    messages.append({"role": "assistant", "content": f"{assistant_message}"})

    print(response.choices[0].message.content)
