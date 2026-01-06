# TalentScout – AI Hiring Assistant 🤖

## AI/ML Intern Assignment

*An intelligent, context-aware hiring assistant chatbot built using Python, Streamlit, and Large Language Models (LLMs) to automate the initial screening of candidates for technical roles.*

## Features
- Professional conversational AI hiring assistant
- Step-by-step candidate information collection
- Dynamic technical question generation based on declared tech stack
- Context-aware, stage-based conversation handling
- Graceful exit and user-controlled termination
- Input validation and fallback handling
- Secure API key management using environment variables
- GDPR-aligned data handling (session-only, no persistence)

## Tech Stack
- **Programming Language:** Python
- **Frontend/UI:** Streamlit
- **Large Language Model:** LLaMA 3.1 (via Groq API)
- **Environment Management:** python-dotenv

## Project Structure
```
talentscout/
│
├── app.py              # Streamlit application (main entry point)
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
└── .env                # Environment variables (not uploaded)
```

## Installation & Setup

**1. Clone the Repository**
```
git clone <your-repo-link>
cd talentscout
```

**2. Install Dependencies**
```
pip install -r requirements.txt
```

**3. Configure Environment Variables**

Create a `.env` file in the project root and add:
```
GROQ_API_KEY=your_api_key_here
```

*Note: The .env file is intentionally excluded from version control for security reasons.*

**4. Run the Application**
```
streamlit run app.py
```

## Prompt Design Strategy
- A System Prompt defines the role, tone, and constraints of the hiring assistant.
- Stage-based logic ensures that only one question is asked at a time.
- A dynamic prompt is generated after the candidate declares their tech stack to produce relevant technical interview questions.
- Question difficulty is adapted based on the candidate's years of experience.
- The model is instructed not to include answers, ensuring realistic interview-style questioning.

## Conversation Flow
1. Greeting and purpose explanation
2. Full Name
3. Email Address (validated)
4. Phone Number (validated)
5. Years of Experience
6. Desired Position(s)
7. Current Location
8. Tech Stack Declaration
9. AI-generated Technical Questions
10. Graceful conversation termination

## Data Privacy & GDPR Compliance
This project follows key principles of the EU General Data Protection Regulation (GDPR):

- **Data Minimization:** Only essential information required for initial screening is collected.
- **Purpose Limitation:** All data is used strictly for hiring-related screening.
- **Storage Limitation:** Candidate data is stored only in-memory during the active session and is never persisted.
- **Security:** No personal data is logged, stored in databases, or shared with third parties.
- **Transparency:** Users are informed about data usage at the start of the interaction.
- **User Control:** Candidates may exit the conversation at any time, immediately ending data processing.

No personal data is retained after the session ends.

## Evaluation Criteria Mapping

### Technical Proficiency
- Context-aware hiring assistant implemented using an LLM (LLaMA 3.1).
- Dynamic generation of technical interview questions.
- Clean, readable, and modular Python code.

### Problem-Solving & Critical Thinking
- Stage-based conversation control to maintain coherence.
- Prompt engineering to guide LLM behavior.
- Fallback mechanisms for invalid or unexpected inputs.

### User Interface & Experience
- Streamlit-based chat interface.
- Simple, intuitive, and professional UI tailored for hiring use cases.

### Documentation & Presentation
- Comprehensive documentation covering setup, usage, architecture, and design decisions.
- Explicit explanation of prompt strategy and data privacy practices.

## Example Tech Stack Input
```
Python, Django, SQL
```

## Future Enhancements
- Sentiment analysis to assess candidate confidence
- Multilingual support
- Persistent encrypted storage (optional)
- Enhanced UI styling and analytics dashboard

## Author
**Shivansh Garg**  
AI/ML Intern Assignment

*Final Note for Evaluators:*  
This project emphasizes responsible AI usage, prompt engineering, and context-aware interaction design, demonstrating practical application of Large Language Models in real-world hiring scenarios.
