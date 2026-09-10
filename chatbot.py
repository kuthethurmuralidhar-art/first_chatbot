import streamlit as st

# Customise your information here
NAME = "Dell"  # Put your name here
EMAIL = "your.email@example.com"
LINKEDIN = "https://linkedin.com"

st.set_page_config(page_title=f"{NAME}'s Resume Bot", page_icon="💼")
st.title(f"💼 {NAME}'s Career Assistant")
st.write(f"Welcome! Ask me anything about {NAME}'s professional skills, projects, or background.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": f"Hi there! I am {NAME}'s virtual assistant. Try asking me 'What are your skills?' or 'How can I contact you?'"}
    ]

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if user_input := st.chat_input("Ask about my career..."):
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    query = user_input.lower()
    
    # Matching rules for responses
    if "skill" in query or "language" in query or "technology" in query:
      response = (
            f"**{NAME}'s core skills include:**\n\n"
            "- 🗄️ **Database Administration:** Oracle DBA\n"
            "- ☁️ **Cloud Computing:** Oracle Cloud Infrastructure (OCI)\n"
            "- 🛠️ **Systems & Design:** Oracle Designer\n"
            "- 🐍 **Programming:** Python Basics & Streamlit development"
        )
    elif "project" in query or "built" in query or "portfolio" in query:
        response = f"**Key Projects:**\n1. **Interactive Resume Bot:** Built using Python and Streamlit, hosted live on the web.\n2. *Add your other projects here!*"
    
    elif "contact" in query or "email" in query or "linkedin" in query or "resume" in query:
        response = f"You can connect with {NAME} via:\n- 📧 **Email:** {EMAIL}\n- 🔗 **LinkedIn:** [{NAME}'s Profile]({LINKEDIN})"
        
    elif "experience" in query or "background" in query or "work" in query:
        response = f"{NAME} is an experienced database professional specialising in **Oracle DBA**, **OCI**, and **Oracle Designer**, with expanding capabilities in **Python automation** and application design."
    elif "hello" in query or "hi" in query:
        response = f"Hello! Feel free to ask about {NAME}'s skills, projects, or contact information."
        
    else:
        response = "I'm not quite sure about that one. Try asking about my 'skills', 'projects', 'work experience', or 'contact details'!"

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
