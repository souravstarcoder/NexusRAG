import streamlit as st
import html

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

from rag import search_knowledge_base
from config import GOOGLE_API_KEY, GEMINI_MODEL


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Knowledge Base AI",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* ---------- APP BACKGROUND ---------- */

    .stApp {
        background:
            radial-gradient(
                circle at top left,
                rgba(59,130,246,0.18),
                transparent 35%
            ),
            radial-gradient(
                circle at top right,
                rgba(139,92,246,0.15),
                transparent 35%
            ),
            linear-gradient(
                135deg,
                #020617,
                #0f172a,
                #111827
            );

        color: #f8fafc;
    }


    /* ---------- MAIN CONTAINER ---------- */

    .block-container {
        max-width: 850px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }


    /* ---------- HIDE STREAMLIT DEFAULT ---------- */

    #MainMenu {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }


    /* ---------- HERO ---------- */

    .hero-card {
        text-align: center;

        padding: 42px 30px;

        margin-bottom: 30px;

        border-radius: 26px;

        background:
            linear-gradient(
                135deg,
                rgba(15,23,42,0.96),
                rgba(30,58,138,0.90)
            );

        border: 1px solid rgba(148,163,184,0.20);

        box-shadow:
            0 20px 50px rgba(0,0,0,0.35);

        backdrop-filter: blur(12px);
    }


    .hero-icon {
        font-size: 52px;
        margin-bottom: 12px;
    }


    .hero-title {
        font-size: 40px;
        font-weight: 800;

        letter-spacing: -1px;

        color: #ffffff;

        margin-bottom: 10px;
    }


    .hero-subtitle {
        font-size: 16px;

        color: #cbd5e1;

        margin-bottom: 20px;
    }


    .status {
        display: inline-block;

        padding: 8px 16px;

        border-radius: 999px;

        background: rgba(34,197,94,0.12);

        border: 1px solid rgba(34,197,94,0.25);

        color: #86efac;

        font-size: 13px;

        font-weight: 600;
    }


    /* ---------- QUESTION ---------- */

    .question-label {
        font-size: 16px;

        font-weight: 700;

        color: #e2e8f0;

        margin-bottom: 8px;
    }


    /* ---------- TEXT INPUT ---------- */

    .stTextInput > div > div > input {

        background: rgba(15,23,42,0.85) !important;

        color: #ffffff !important;

        border: 1px solid #334155 !important;

        border-radius: 14px !important;

        padding: 14px !important;

        font-size: 16px !important;

        height: 52px;
    }


    .stTextInput > div > div > input:focus {

        border-color: #60a5fa !important;

        box-shadow:
            0 0 0 1px #60a5fa !important;
    }


    .stTextInput > div > div > input::placeholder {

        color: #94a3b8 !important;
    }


    /* ---------- ANSWER ---------- */

    .answer-card {

        margin-top: 25px;

        padding: 24px;

        border-radius: 18px;

        background:
            rgba(15,23,42,0.88);

        border:
            1px solid rgba(96,165,250,0.25);

        box-shadow:
            0 12px 35px rgba(0,0,0,0.30);
    }


    .answer-title {

        font-size: 20px;

        font-weight: 700;

        color: #93c5fd;

        margin-bottom: 12px;
    }


    .answer-text {

        color: #e2e8f0;

        font-size: 16px;

        line-height: 1.7;
    }


    /* ---------- SOURCES ---------- */

    .source-card {

        padding: 16px;

        margin-bottom: 12px;

        border-radius: 14px;

        background:
            rgba(2,6,23,0.75);

        border:
            1px solid #334155;

        color: #cbd5e1;

        line-height: 1.6;
    }


    /* ---------- FOOTER ---------- */

    .custom-footer {

        text-align: center;

        color: #64748b;

        font-size: 12px;

        margin-top: 45px;

        padding-top: 20px;

        border-top:
            1px solid rgba(148,163,184,0.12);
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# GEMINI
# =========================================================

llm = ChatGoogleGenerativeAI(
    model=GEMINI_MODEL,
    google_api_key=GOOGLE_API_KEY
)


# =========================================================
# HERO
# =========================================================

st.html(
    """
    <div class="hero-card">

        <div class="hero-icon">🤖</div>

        <div class="hero-title">
            Knowledge Base AI
        </div>

        <div class="hero-subtitle">
            Ask questions and get intelligent answers
            from your knowledge base.
        </div>

        <div class="status">
            ● AI Knowledge Assistant
        </div>

    </div>
    """
)


# =========================================================
# QUESTION
# =========================================================

st.markdown(
    '<div class="question-label">💬 Ask your question</div>',
    unsafe_allow_html=True
)


question = st.text_input(
    "Question",
    placeholder="e.g. What are the company's working hours?",
    label_visibility="collapsed"
)


# =========================================================
# RAG RESPONSE
# =========================================================

if question:

    with st.spinner("🔎 Searching knowledge base..."):

        documents = search_knowledge_base(question)

        if not documents:

            st.warning(
                "No relevant information found in the knowledge base."
            )

        else:

            context = "\n\n".join(
                document.page_content
                for document in documents
            )


            prompt = ChatPromptTemplate.from_template(
                """
You are a helpful knowledge-base assistant.

Answer the user's question using ONLY the information
provided in the context.

If the answer is not present in the context, say:

"I don't have that information in my knowledge base."

Context:
{context}

Question:
{question}

Answer:
"""
            )


            chain = prompt | llm


            response = chain.invoke(
                {
                    "context": context,
                    "question": question
                }
            )


            # Safely display AI response
            answer_text = html.escape(
                str(response.content)
            )


            # =================================================
            # ANSWER CARD
            # =================================================

            st.html(
                f"""
                <div class="answer-card">

                    <div class="answer-title">
                        ✨ Answer
                    </div>

                    <div class="answer-text">
                        {answer_text}
                    </div>

                </div>
                """
            )


            # =================================================
            # SOURCES
            # =================================================

            with st.expander("📚 View retrieved knowledge"):

                for i, document in enumerate(
                    documents,
                    1
                ):

                    source_text = html.escape(
                        document.page_content
                    )


                    st.html(
                        f"""
                        <div class="source-card">

                            <b>Source {i}</b>

                            <br><br>

                            {source_text}

                        </div>
                        """
                    )


# =========================================================
# FOOTER
# =========================================================

st.html(
    """
    <div class="custom-footer">

        Built with LangChain • ChromaDB •
        Hugging Face Embeddings • Gemini

    </div>
    """
)
