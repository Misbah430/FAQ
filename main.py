#E:\Minicinda\conda\FAQ\FAQ
import streamlit as st
import json
from fuzzywuzzy import process
import datetime

def load_faq_data():
    with open("faq.json", "r") as file:
        return json.load(file)

faq_data = load_faq_data()
def get_answer(question):
    question = question.lower()
    questions = list(faq_data.keys())
    best_match, score = process.extractOne(question, questions)
    if score >= 70:
        return faq_data[best_match]
    return "❓ Sorry, I don't understand that question."

st.set_page_config(page_title="FAQ Chatbot", page_icon="💬")

st.title("💬 FAQ Chatbot")
st.write("Ask me anything about our services.")
if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You:")

if user_input:
    answer = get_answer(user_input)
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", answer))

for speaker, text in st.session_state.history:
    st.markdown(f"**{speaker}:** {text}")

if st.button("📥 Download Chat"):
    chat_log = "\n".join([f"{s}: {t}" for s, t in st.session_state.history])
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    st.download_button("Download Chat Log", chat_log, file_name=f"chat_{timestamp}.txt")

st.markdown("### 📬 Feedback")
feedback = st.text_input("Your feedback:")
if st.button("Submit Feedback"):
    with open("feedback.txt", "a") as f:
        f.write(feedback + "\n")
    st.success("Thank you for your feedback! 🎉")
