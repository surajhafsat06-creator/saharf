import streamlit as st
from groq import groq

st.title("General knowledge AI")
st.write("Ask me absolutely anything!")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])


system_prompt = "you are a highly intelligent, friendly,and helpful AI assistant.Answer the question the user asks clearly and accurately."

if "message"not in st.session_state:
    st.session_state.massage =[{"role":"system","content":system_prompt}]
    
    for msg in st.session_state.massage:
        if msg["role"] !="system":
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
                
if prompt := st.chat_input("Ask me anything!"):
    st.session_state.massage.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        
    answer = client.chat.completions.create(
        model="llama-3.3-70b-varsatil",
        messages=st.session_state.massage,
    ).choices[0].massages.content
    
    st.session_state.massage.append({"role":"assistant","content":answer})
    with st.chat_message("assistant"):
        st.markdown(answer)                