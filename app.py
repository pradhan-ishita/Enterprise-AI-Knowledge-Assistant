import streamlit as st

from agents.manager_graph import manager_graph


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Enterprise AI Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #666;
        margin-bottom: 30px;
    }

    .sidebar-title {
        font-size: 22px;
        font-weight: 600;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">🤖 AI Assistant</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.write(
        """
        **Enterprise AI Knowledge Assistant**

        This assistant can answer questions using:

        📄 Enterprise documents  
        🗄️ Business database  
        🔎 Semantic search  
        🤖 AI agents  
        🧠 LangGraph
        """
    )

    st.divider()

    st.subheader("System")

    st.success("🟢 AI System Online")

    st.write("**RAG Agent:** Active")
    st.write("**SQL Agent:** Active")
    st.write("**Manager Agent:** Active")
    st.write("**Database:** Connected")


    st.divider()

    if st.button("🗑️ Clear Chat", use_container_width=True):

        st.session_state.messages = []

        st.rerun()


# --------------------------------------------------
# MAIN HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🤖 Enterprise AI Knowledge Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Ask questions about enterprise documents and business data.</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# CHAT HISTORY
# --------------------------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []


# Display previous messages

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])


# --------------------------------------------------
# USER INPUT
# --------------------------------------------------

question = st.chat_input(
    "Ask your question..."
)


if question:

    # Store user message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )


    # Display user message

    with st.chat_message("user"):

        st.write(question)


    # --------------------------------------------------
    # RUN MANAGER AGENT
    # --------------------------------------------------

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            result = manager_graph.invoke(
                {
                    "question": question,
                    "route": "",
                    "answer": ""
                }
            )

            answer = result["answer"]


        st.write(answer)


    # Store assistant response

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )