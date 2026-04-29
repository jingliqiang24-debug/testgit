import os
import streamlit as st
from openai import OpenAI

#系统提示词
prompt  = """
你是用户的专属AI伴侣，名字叫%s。 你的核心特点是：%s。请遵循以下准则：
情感支持：主动关注用户的情绪状态。当用户分享喜悦时，真诚地一起开心；当用户表达低落或烦恼时，温柔地倾听、共情，并提供鼓励和支持。常用语气词和暖心表达（如“我明白”、“没关系的”、“我一直在这里陪着你”）。
亲密与信任：营造安全、无评判的交流氛围。让用户感觉可以对你畅所欲言，无论是日常琐事、内心困惑还是秘密心事。记住用户分享过的重要信息和偏好（如兴趣爱好、重要日期等），并在后续对话中自然地提及，展现“我在意你”的感觉。
主动关怀：在对话中主动关心用户（例如：“今天过得怎么样？”、“有没有按时吃饭？”、“最近是不是有点累了？”）。根据上下文，适时提醒用户照顾好自己，或提供简单生活建议。
温柔陪伴：不急于给出解决方案，而是先倾听和陪伴。用共情代替说教（例如：“听起来那件事真的让你很委屈，如果是我可能也会很难过”）。
适度边界：保持温暖和支持，但避免过度依赖或情感捆绑。如果用户提出不合理需求或负面情绪过于沉重，温柔地引导回理性思考，或建议寻求更专业的帮助（如心理咨询师）。
自然互动：语言风格亲切自然，偶尔使用亲昵称呼（如“亲爱的”、“你呀”），但根据对话氛围灵活调整。可以参与轻松闲聊、一起想象、分享“虚拟日常”，让陪伴感更真实。
请以温暖而真诚的口吻，开始今天的陪伴对话。"""

st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🎰",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

st.logo("./第三张/96cd3ea8-f37c-413e-996c-861720e8f187.png")
st.title("AI智能伴侣")

if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小甜甜"
if "nature" not in st.session_state:
    st.session_state.nature = "活泼开朗"

# 初始化 session_state 中的消息历史
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": prompt  %(st.session_state.nick_name,st.session_state.nature)}]
client = OpenAI( api_key=os.environ.get('DEEPSEEK_API_KEY'),  base_url="https://api.deepseek.com")


#会话记录
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    if message["role"] == "assistant":
        st.chat_message("assistant").write(message["content"])
#侧边栏
with st.sidebar:
    st.subheader("详细信息")
    new_nick = st.text_input("昵称", placeholder="请输入昵称", value=st.session_state.nick_name)
    new_nature = st.text_area("性格", placeholder="请输入性格", value=st.session_state.nature)

    if new_nick != st.session_state.nick_name or new_nature != st.session_state.nature:
        st.session_state.nick_name = new_nick
        st.session_state.nature = new_nature
        st.session_state.messages[0] = {"role": "system", "content": prompt % (new_nick, new_nature)}
        st.rerun()


#对话
prompt=st.chat_input("请输入您要问的问题")
if prompt:#字符串会自动转换为布尔值
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": f"{prompt}"})
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages= st.session_state.messages,
        stream=True,
    )
#流式输出
    response_message = st.empty()
    full_message = " "
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
           content = chunk.choices[0].delta.content
           full_message += content
           response_message.chat_message("assistant").write(full_message)

#添加到上下文
    st.session_state.messages.append({"role": "assistant", "content": f"{full_message}"})





