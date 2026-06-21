import streamlit as st

st.set_page_config(page_title="Dr. Bella - Healthcare Assistant", page_icon="🩺", layout="centered")

st.title("🩺 Dr. Bella: Medical Guidance Portal")
st.markdown("---")

medical_knowledge_base = {
    "hello": "Hello! I am Dr. Bella. How can I assist you with your health concerns today?",
    "hi": "Hello! Please let me know what symptoms you are experiencing.",
    "hey": "Greetings. Tell me how you are feeling so I can guide you.",
    "fever": "Clinical Advice [Fever]: Stay hydrated, get plenty of rest, and monitor your temperature. If it exceeds 101°F, consider paracetamol.",
    "headache": "Clinical Advice [Headache]: Ensure you are hydrated and reduce screen time. If it's a tension headache, a dark quiet room helps.",
    "cough": "Clinical Advice [Cough]: Warm liquids like herbal tea with honey can soothe your throat. If it persists, consult a physician.",
    "flu": "Clinical Advice [Flu]: Influenza requires rest, steam inhalation, and vitamin C. Keep your distance from others.",
    "name": "Identification: I am Dr. Bella, a deterministic rule-based healthcare agent built using optimized Hashmap architectures."
}

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello, I am Dr. Bella. Please describe your symptoms (or type 'exit' / 'bye' to close)."}]

if "session_active" not in st.session_state:
    st.session_state.session_active = True

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if not st.session_state.session_active:
    st.error("This clinical session has been closed/ended by the user.")
    if st.button("Restart Chat Session"):
        st.session_state.messages = [{"role": "assistant", "content": "Hello, I am Dr. Bella. Please describe your symptoms."}]
        st.session_state.session_active = True
        st.rerun()

if st.session_state.session_active:
    if user_query := st.chat_input("Type your symptoms here..."):
        
        with st.chat_message("user"):
            st.markdown(user_query)
        st.session_state.messages.append({"role": "user", "content": user_query})
        
        clean_input = user_query.lower().strip()
        
        # Core Branching Control
        if clean_input in ["exit", "bye", "quit", "close"]:
            bot_response = "Thank you for consulting Dr. Bella. Stay safe, take care of your health, and goodbye! 👋"
            with st.chat_message("assistant"):
                st.markdown(bot_response)
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
            st.session_state.session_active = False 
            st.rerun()
        else:
            # Token Dynamic Matching Block
            response_found = False
            bot_response = ""
            
            for keyword in medical_knowledge_base:
                if keyword in clean_input:
                    bot_response = medical_knowledge_base[keyword]
                    response_found = True
                    break
        
            if not response_found:
                bot_response = "[Clinical Guardrail Triggered]: Symptoms/Keywords not registered in my database. To avoid medical hallucination, please consult a real practitioner."
                
            with st.chat_message("assistant"):
                st.markdown(bot_response)
            st.session_state.messages.append({"role": "assistant", "content": bot_response})