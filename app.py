import streamlit as st
import google.generativeai as genai

# Konfigurasi API Key
genai.configure(api_key="AIzaSyBM3eshW0CW6lLDMvJtEdY4XGz08zyYpbY")

# Fungsi untuk mendapatkan respons dari Gemini
def get_gemini_response(prompt):
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt)
    return response.text

# Judul Aplikasi
st.title("My Chatbot")

# Inisialisasi session state untuk menyimpan percakapan
if "messages" not in st.session_state:
    st.session_state.messages = []

# Menampilkan percakapan sebelumnya
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input pengguna dengan tampilan chat
user_input = st.chat_input("Say something...")

if user_input:
    # Menampilkan input pengguna di chat
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Mendapatkan respons dari Gemini
    response = get_gemini_response(user_input)

    # Menampilkan respons chatbot di chat
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
