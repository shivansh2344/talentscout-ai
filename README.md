# TalentScout – AI Hiring Assistant 🤖

## AI/ML Intern Assignment

*TalentScout is an intelligent, context-aware hiring assistant chatbot built using Python, Streamlit, and Large Language Models (LLMs) to automate the initial screening of candidates for technical roles. The assistant gathers essential candidate information and dynamically generates technical interview questions based on the candidate's declared tech stack.*

## Features
- Professional conversational AI hiring assistant
- Step-by-step candidate information collection
- Context-aware, stage-based conversation handling
- Dynamic technical interview question generation based on tech stack
- Input validation and fallback handling (email, phone, empty input)
- Graceful exit and user-controlled termination
- **Bonus Feature:** LLM-based confidence assessment of candidate interaction
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
git clone https://github.com/shivansh2344/talentscout-ai
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

*Note: The .env file is intentionally excluded from version control for security and privacy reasons.*

**4. Run the Application**
```
streamlit run app.py
```

## Prompt Design Strategy
- A System Prompt defines the assistant's role, tone, and constraints.
- Stage-based logic ensures only one question is asked at a time.
- A dynamic prompt generates technical interview questions after tech stack declaration.
- Question difficulty is adapted based on years of experience.
- A constrained evaluator prompt is used to generate a concise confidence assessment.
- The model is explicitly instructed not to generate answers to interview questions.

## Conversation Flow
1. Greeting and purpose explanation
2. Full Name
3. Email Address (validated)
4. Phone Number (validated)
5. Years of Experience
6. Desired Position(s)
7. Current Location
8. Tech Stack Declaration
9. AI-generated Technical Interview Questions
10. Confidence Assessment (Bonus Feature)
11. Graceful conversation termination

## Data Privacy & GDPR Compliance
This project is designed in alignment with key principles of the EU General Data Protection Regulation (GDPR):

- **Data Minimization:** Only essential information required for initial screening is collected.
- **Purpose Limitation:** Candidate data is used strictly for hiring-related screening.
- **Storage Limitation:** Data is stored only in-memory during the active session and is not persisted.
- **Security:** No personal data is logged, stored in databases, or shared with third parties.
- **Transparency:** Users are informed about data usage at the beginning of the interaction.
- **User Control:** Candidates can exit at any time, immediately stopping data processing.

No personal data is retained after the session ends.

## Evaluation Criteria Mapping

### Technical Proficiency
- Context-aware hiring assistant using an LLM (LLaMA 3.1).
- Dynamic technical question generation based on candidate tech stack.
- Clean, readable, and maintainable Python code.

### Problem-Solving & Critical Thinking
- Stage-based conversation flow to maintain coherence.
- Prompt engineering for controlled LLM behavior.
- Robust fallback handling for invalid or unexpected inputs.

### User Interface & Experience
- Streamlit-based chat interface.
- Professional, intuitive UI tailored for hiring scenarios.

### Documentation & Presentation
- Comprehensive documentation covering setup, usage, and design decisions.
- Clear explanation of prompt strategy, privacy, and ethical AI considerations.

## Example Tech Stack Input
```
Python, Django, SQL
```

## Future Enhancements
- Multilingual support
- Answer evaluation and scoring
- Persistent encrypted storage (optional)
- Advanced analytics and recruiter dashboard

## Author
**Shivansh Garg**  
AI/ML Intern Assignment

*Final Note for Evaluators:*  
This project emphasizes responsible AI usage, prompt engineering, and context-aware interaction design, demonstrating practical application of Large Language Models in real-world hiring workflows.
