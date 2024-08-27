import streamlit as st
import os
from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

    model = Model(
        model_id=ModelTypes.LLAMA_3_70B_INSTRUCT,
        params={
            GenParams.MAX_NEW_TOKENS: 900,
            GenParams.RETURN_OPTIONS: {
                'input_text': True,
                'generated_tokens': True,
            },
        },
        credentials=Credentials(
            api_key=ibm_api_key,
            url="https://us-south.ml.cloud.ibm.com",
        ),
        project_id=ibm_project_id,
    )
        generated_response = model.generate(prompt=prompt)
# Function to call API
def call_api(prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=MODEL_NAME
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Define functions for each tool with few-shot examples
def personalized_learning_assistant(topic):
    prompt = f"""
    Provide a personalized learning plan for the topic: {topic}.
    Example 1: For 'Machine Learning': 'Create a plan with courses on supervised learning, unsupervised learning, and neural networks. Include practical exercises and projects.'
    Example 2: For 'Data Science': 'Suggest a plan with a focus on data analysis, visualization, and statistical modeling. Recommend tools like Python, R, and SQL.'
    Example 3: For 'Web Development': 'Outline a plan that covers front-end and back-end development, including HTML, CSS, JavaScript, and server-side technologies.'
    Example 4: For '{topic}':"""
    return call_groq_api(prompt)

def ai_coding_mentor(code_snippet):
    prompt = f"""
    Review this AI code snippet and provide suggestions or improvements:
    {code_snippet}
    Example 1: 'In the provided code, consider using a different activation function to improve performance.'
    Example 2: 'The code can be optimized by reducing redundant calculations and enhancing readability.'
    Example 3: 'Add comments to explain complex sections of the code for better understanding.'
    Example 4: 'For the provided snippet, suggest improvements or fixes:"""
    return call_groq_api(prompt)

def smart_document_summarizer(document_text):
    prompt = f"""
    Summarize the following document:
    {document_text}
    Example 1: 'The document discusses the impact of climate change on global agriculture, emphasizing the need for sustainable practices.'
    Example 2: 'It provides an overview of recent advancements in AI technology and its applications in various fields.'
    Example 3: 'The text outlines the historical development of renewable energy sources and their future potential.'
    Example 4: 'Summarize this document:"""
    return call_groq_api(prompt)

def interactive_study_planner(exam_schedule):
    prompt = f"""
    Create an interactive study plan based on this exam schedule:
    {exam_schedule}
    Example 1: 'For an exam schedule with subjects A, B, and C, create a plan that allocates study time for each subject and includes breaks.'
    Example 2: 'Plan should include daily study goals and revision sessions leading up to the exams.'
    Example 3: 'Suggest a study plan that balances subject preparation with relaxation to avoid burnout.'
    Example 4: 'Based on the provided schedule, create a study plan:"""
    return call_groq_api(prompt)

def real_time_qa_support(question):
    prompt = f"""
    Provide an answer to the following academic question:
    {question}
    Example 1: 'Question: What is the capital of France? Answer: Paris.'
    Example 2: 'Question: Explain the theory of relativity. Answer: The theory of relativity, developed by Albert Einstein, includes two theories: special relativity and general relativity, explaining the relationship between space, time, and gravity.'
    Example 3: 'Question: What is the process of photosynthesis? Answer: Photosynthesis is the process by which green plants use sunlight to synthesize foods with the help of chlorophyll, water, and carbon dioxide.'
    Example 4: 'Answer this question:"""
    return call_groq_api(prompt)

def mental_health_check_in(feelings):
    prompt = f"""
    Provide some advice based on these feelings:
    {feelings}
    Example 1: 'Feeling stressed? Try practicing mindfulness and deep breathing exercises to calm your mind.'
    Example 2: 'If you're feeling anxious, consider talking to a trusted friend or counselor for support.'
    Example 3: 'Feeling overwhelmed? Break your tasks into smaller steps and focus on completing them one at a time.'
    Example 4: 'Based on these feelings, provide advice:"""
    return call_groq_api(prompt)

# Initialize session state if not already set
if 'responses' not in st.session_state:
    st.session_state['responses'] = {
        "personalized_learning_assistant": "",
        "ai_coding_mentor": "",
        "smart_document_summarizer": "",
        "interactive_study_planner": "",
        "real_time_qa_support": "",
        "mental_health_check_in": ""
    }

# Function to clear session state values
def clear_session_state():
    for key in st.session_state.keys():
        if key.startswith('responses'):
            st.session_state[key] = ""
        if key in ['personalized_learning_assistant', 'ai_coding_mentor', 'smart_document_summarizer', 'interactive_study_planner', 'real_time_qa_support', 'mental_health_check_in']:
            st.session_state[key] = ""

# Inject CSS
st.markdown("""
    <style>
    /* Common Styles for Both Themes */
    body {
        font-family: 'Arial', sans-serif;
    }
    .stButton button {
        padding: 0.5rem 1rem;
        border-radius: 5px;
        border: 2px solid #1f316f;
    }
    .stTextInput, .stTextArea {
        padding: 0.5rem;
        border-radius: 5px;
        border: 2px solid #1f316f;
    }
    .footer {
        text-align: center;
        padding: 1rem;
        border-top: 2px solid #1f316f;
    }
    .footer a {
        margin: 0 1rem;
        text-decoration: none;
        font-weight: bold;
    }

    /* Light Theme */
    .light-theme {
        background-color: #ffffff; /* Light background */
        color: #000000; /* Black text */
    }
    .light-theme .stButton button {
        background-color: #e3c1e0 /* Navy blue button */
        color: #ffffff; /* White button text */
    }
    .light-theme .stButton button:hover {
        background-color: #0d1b3f; /* Darker navy blue on hover */
    }
    .light-theme .stTextInput, .light-theme .stTextArea {
        background-color: #ffffff; /* White input background */
        color: #e3c1e0; /* Black input text */
    }
    .light-theme .footer {
        background-color: #f6eacb; /* Cream footer background */
        color: #000000; /* Black footer text */
    }
    .light-theme .footer a {
        color: #1f316f; /* Navy blue footer links */
    }
    .light-theme .footer a:hover {
        color: #0d1b3f; /* Darker navy blue on hover */
    }

    /* Dark Theme */
    .dark-theme {
        background-color: #1e1e2f; /* Dark background */
        color: #ffffff; /* White text */
    }
    .dark-theme .stButton button {
        background-color: #eecad5; /* Light pink button */
        color: #000000; /* Black button text */
    }
    .dark-theme .stButton button:hover {
        background-color: #cba9b3; /* Darker pink on hover */
    }
    .dark-theme .stTextInput, .dark-theme .stTextArea {
        background-color: #2e2e3e; /* Dark input background */
        color: #ffffff; /* White input text */
    }
    .dark-theme .footer {
        background-color: #eecad5; /* Light pink footer background */
        color: #ffffff; /* Black footer text */
    }
    .dark-theme .footer a {
        color: #ffffff ; /* Black footer links */
    }
    .dark-theme .footer a:hover {
        color: #cba9b3; /* Darker pink on hover */
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar with navigation options
st.sidebar.title("Edu Nexus 📖")
selected_task = st.sidebar.radio("Select a Tool", [
    "🧑‍🎓 Personalized Learning Assistant",
    "🤖 AI Coding Mentor",
    "📄 Smart Document Summarizer",
    "🗓 Interactive Study Planner",
    "❓ Real-Time Q&A Support",
    "💬 Mental Health Check-In"
])

# Main content area
st.title(f"Welcome to Edu Nexus 📖 - {selected_task}")

# Display the selected task based on user selection
if selected_task == "🧑‍🎓 Personalized Learning Assistant":
    topic = st.text_input("Enter the topic of interest:")
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("Clear"):
            st.session_state['responses']["personalized_learning_assistant"] = ""
            st.rerun()
    with col2:
        if st.button("Generate Learning Plan"):
            if topic:
                st.session_state['responses']["personalized_learning_assistant"] = personalized_learning_assistant(topic)
            else:
                st.session_state['responses']["personalized_learning_assistant"] = "Please enter a topic."
    
    st.text_area("Response", value=st.session_state['responses']["personalized_learning_assistant"], height=200, key="personalized_learning_assistant")

elif selected_task == "🤖 AI Coding Mentor":
    code_snippet = st.text_area("Enter the AI code snippet for review:")
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("Clear"):
            st.session_state['responses']["ai_coding_mentor"] = ""
            st.rerun()
    with col2:
        if st.button("Get Code Review"):
            if code_snippet:
                st.session_state['responses']["ai_coding_mentor"] = ai_coding_mentor(code_snippet)
            else:
                st.session_state['responses']["ai_coding_mentor"] = "Please enter a code snippet."
    
    st.text_area("Response", value=st.session_state['responses']["ai_coding_mentor"], height=200, key="ai_coding_mentor")

elif selected_task == "📄 Smart Document Summarizer":
    document_text = st.text_area("Paste the document text here:")
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("Clear"):
            st.session_state['responses']["smart_document_summarizer"] = ""
            st.rerun()
    with col2:
        if st.button("Summarize Document"):
            if document_text:
                st.session_state['responses']["smart_document_summarizer"] = smart_document_summarizer(document_text)
            else:
                st.session_state['responses']["smart_document_summarizer"] = "Please paste the document text."
    
    st.text_area("Response", value=st.session_state['responses']["smart_document_summarizer"], height=200, key="smart_document_summarizer")

elif selected_task == "🗓 Interactive Study Planner":
    exam_schedule = st.text_area("Enter your exam schedule:")
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("Clear"):
            st.session_state['responses']["interactive_study_planner"] = ""
            st.rerun()
    with col2:
        if st.button("Generate Study Plan"):
            if exam_schedule:
                st.session_state['responses']["interactive_study_planner"] = interactive_study_planner(exam_schedule)
            else:
                st.session_state['responses']["interactive_study_planner"] = "Please enter your exam schedule."
    
    st.text_area("Response", value=st.session_state['responses']["interactive_study_planner"], height=200, key="interactive_study_planner")

elif selected_task == "❓ Real-Time Q&A Support":
    question = st.text_input("Enter your academic question:")
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("Clear"):
            st.session_state['responses']["real_time_qa_support"] = ""
            st.rerun()
    with col2:
        if st.button("Get Answer"):
            if question:
                st.session_state['responses']["real_time_qa_support"] = real_time_qa_support(question)
            else:
                st.session_state['responses']["real_time_qa_support"] = "Please enter a question."
    
    st.text_area("Response", value=st.session_state['responses']["real_time_qa_support"], height=200, key="real_time_qa_support")

elif selected_task == "💬 Mental Health Check-In":
    feelings = st.text_input("How are you feeling today?")
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("Clear"):
            st.session_state['responses']["mental_health_check_in"] = ""
            st.rerun()
    with col2:
        if st.button("Get Advice"):
            if feelings:
                st.session_state['responses']["mental_health_check_in"] = mental_health_check_in(feelings)
            else:
                st.session_state['responses']["mental_health_check_in"] = "Please enter your feelings."
    
    st.text_area("Response", value=st.session_state['responses']["mental_health_check_in"], height=200, key="mental_health_check_in")

# Footer with contact information
st.markdown("""
    <div class="footer">
        <a href="https://github.com/muhammadibrahim313" target="_blank"><i class="fab fa-github"></i> GitHub</a>
        <a href="https://www.linkedin.com/in/muhammad-ibrahim-qasmi-9876a1297/" target="_blank"><i class="fab fa-linkedin"></i> LinkedIn</a>
        <a href="https://github.com/Ahmad-Fakhar" target="_blank"><i class="fab fa-github"></i> Partner's GitHub</a>
        <a href="https://www.linkedin.com/in/ahmad-fakhar-357742258/" target="_blank"><i class="fab fa-linkedin"></i> Partner's LinkedIn</a>
    </div>
""", unsafe_allow_html=True)
