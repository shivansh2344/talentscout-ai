import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(page_title="TalentScout AI", page_icon="🤖")

# Title
st.title("🤖 TalentScout – AI Hiring Assistant")

# 🔒 GDPR Privacy Notice (Transparency + User Control)
st.caption(
    "🔒 **Privacy Notice:** This assistant collects limited personal information "
    "solely for initial hiring screening. No data is stored after the session ends. "
    "You may type **exit** at any time to stop and withdraw."
)

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# System prompt (Purpose Limitation explicitly stated)
SYSTEM_PROMPT = """
You are TalentScout, an AI hiring assistant for a recruitment agency.

Rules:
- Collect candidate information step by step.
- Ask only one question at a time.
- Be professional and friendly.
- After collecting tech stack, generate technical interview questions.
- If the user types exit, quit, or stop, end the conversation politely.
- Use candidate information strictly for initial hiring screening.
"""

# ----------------- Validation Helpers -----------------

def is_valid_email(email):
    return "@" in email and "." in email

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) >= 8

# ----------------- Session State Initialization -----------------

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

if "stage" not in st.session_state:
    st.session_state.stage = "name"

if "candidate" not in st.session_state:
    st.session_state.candidate = {}

# ----------------- Initial Greeting -----------------

if "greeted" not in st.session_state:
    greeting = "Hello! Let’s begin the screening. What is your full name?"
    st.session_state.messages.append(
        {"role": "assistant", "content": greeting}
    )
    st.session_state.greeted = True

# ----------------- Display Chat History -----------------

for msg in st.session_state.messages:
    if msg["role"] != "system":
        st.chat_message(msg["role"]).write(msg["content"])

# ----------------- Chat Input -----------------

user_input = st.chat_input("Type your response here...")

if user_input:

    # Empty input handling
    if user_input.strip() == "":
        st.session_state.messages.append(
            {"role": "assistant", "content": "Please enter a response so we can continue."}
        )
        st.rerun()

    # Exit handling (GDPR: Right to Withdraw + Storage Limitation)
    if user_input.lower() in ["exit", "quit", "stop"]:
        st.session_state.clear()
        st.chat_message("assistant").write(
            "Thank you for your time. Your information has not been stored. Goodbye!"
        )
        st.stop()

    # Store user input
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    stage = st.session_state.stage
    candidate = st.session_state.candidate

    # ----------------- Stage Logic -----------------

    if stage == "name":
        candidate["name"] = user_input
        bot_reply = "Thanks! What is your email address?"
        st.session_state.stage = "email"

    elif stage == "email":
        if not is_valid_email(user_input):
            bot_reply = "That doesn’t look like a valid email. Could you please re-enter your email address?"
        else:
            candidate["email"] = user_input
            bot_reply = "What is your phone number?"
            st.session_state.stage = "phone"

    elif stage == "phone":
        if not is_valid_phone(user_input):
            bot_reply = "Please enter a valid phone number (digits only)."
        else:
            candidate["phone"] = user_input
            bot_reply = "How many years of experience do you have?"
            st.session_state.stage = "experience"

    elif stage == "experience":
        candidate["experience"] = user_input
        bot_reply = "Which position(s) are you applying for?"
        st.session_state.stage = "position"

    elif stage == "position":
        candidate["position"] = user_input
        bot_reply = "Where are you currently located?"
        st.session_state.stage = "location"

    elif stage == "location":
        candidate["location"] = user_input
        bot_reply = "Please list your tech stack (languages, frameworks, tools)."
        st.session_state.stage = "tech_stack"

    elif stage == "tech_stack":
        candidate["tech_stack"] = user_input

        tech_prompt = f"""
        The candidate has the following tech stack:
        {user_input}

        Generate 3 to 5 technical interview questions for each technology.
        Difficulty should match {candidate.get('experience', 'their')} years of experience.
        Do not include answers.
        """

        st.session_state.messages.append(
            {"role": "system", "content": tech_prompt}
        )

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=st.session_state.messages,
            temperature=0.4
        )

        technical_questions = response.choices[0].message.content

        # -------- Confidence / Sentiment Estimation Prompt --------
        confidence_prompt = """
        You are an AI evaluator.

        Based ONLY on the candidate's interaction style and responses so far,
        estimate their interview confidence.

        Respond in EXACTLY this format (no extra text):

        Confidence Level: High / Moderate / Low
        Reason: One short sentence (max 15 words)

        Do NOT ask questions.
        Do NOT generate technical content.
        """



        st.session_state.messages.append(
            {"role": "system", "content": confidence_prompt}
        )

        confidence_response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=st.session_state.messages,
            temperature=0.3
        )

        # Clean formatting for confidence output
        confidence_result = confidence_response.choices[0].message.content
        confidence_result = confidence_result.strip()

        # Combine output
        bot_reply = (
        "### 📌 Technical Interview Questions\n\n"
        "_These questions are for recruiter evaluation. "
        "You are not required to answer them at this stage._\n\n"
        f"{technical_questions}\n\n"
        "### 📊 Confidence Assessment\n\n"
        f"{confidence_result}"
        )



        st.session_state.stage = "end"


    else:
        bot_reply = "Thank you for applying. Our team will reach out if there’s a match."
        st.session_state.stage = "end"

    # ----------------- Assistant Response -----------------

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )

    if st.session_state.stage == "end":
        st.session_state.messages.append(
            {"role": "assistant", "content": "This concludes the initial screening. Have a great day!"}
        )

    st.rerun()
