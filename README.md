# NexusRAG 🧠

### Retrieval-Augmented Generation Knowledge Base Chatbot

NexusRAG is a simple and practical **RAG-based AI knowledge assistant** that retrieves relevant information from a custom knowledge base and uses an **LLM** to generate accurate, context-aware responses.

Instead of relying only on the model's general knowledge, NexusRAG first performs **semantic search** over the provided documents and then uses the retrieved context to generate the final answer.

---

## 🚀 Features

- 📄 Supports custom text/PDF-based knowledge sources
- 🔎 Semantic similarity search using vector embeddings
- 🧠 Retrieval-Augmented Generation (RAG) pipeline
- 🤖 LLM-powered context-aware responses
- 🗄️ ChromaDB vector database
- 🔤 Hugging Face embedding models
- ✂️ Intelligent document chunking
- ⚙️ Configurable chunk size, overlap and retrieval count
- 🔐 Environment-variable based API configuration
- 💻 Simple and easy-to-demo architecture

---

## 🏗️ Architecture

```text
                Knowledge Base
               (PDF / Text Data)
                      │
                      ▼
              Document Loading
                      │
                      ▼
             Text Chunking
                      │
                      ▼
          Hugging Face Embeddings
                      │
                      ▼
                ChromaDB
             Vector Database
                      │
                      │
User Query ───────────┘
      │
      ▼
Query Embedding
      │
      ▼
Semantic Search
      │
      ▼
Top-K Relevant Context
      │
      ▼
       LLM
      │
      ▼
Context-Aware Answer
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core development |
| LangChain | RAG pipeline and document processing |
| Hugging Face | Text embeddings |
| BAAI/BGE-small-en-v1.5 | Embedding model |
| ChromaDB | Vector database |
| LLM | Response generation |
| Streamlit | User interface |
| Git & GitHub | Version control |

---

## 📂 Project Structure

```text
NexusRAG/
│
├── data/
│   └── company_knowledge.txt
│
├── app.py
├── config.py
├── ingest.py
├── rag.py
├── requirements.txt
├── .gitignore
└── README.md
```

### File Description

- `app.py` — Application/UI entry point
- `rag.py` — Retrieval and generation logic
- `ingest.py` — Knowledge-base ingestion and vector-store creation
- `config.py` — Project configuration
- `data/` — Custom knowledge-base documents
- `requirements.txt` — Python dependencies
- `.gitignore` — Prevents sensitive/unnecessary files from being committed

---

## ⚙️ How It Works

### 1. Document Ingestion

The knowledge-base documents are loaded and divided into smaller chunks for efficient retrieval.

### 2. Embedding Generation

Each document chunk is converted into a numerical vector using the Hugging Face embedding model:

```text
BAAI/bge-small-en-v1.5
```

### 3. Vector Storage

The generated embeddings are stored in **ChromaDB**, allowing efficient semantic similarity search.

### 4. Query Processing

When a user asks a question, the query is converted into an embedding and compared with the stored document vectors.

### 5. Context Retrieval

The most relevant document chunks are retrieved using semantic similarity.

### 6. Response Generation

The retrieved context is passed to the LLM along with the user's question to generate a context-aware response.

---

## 🔧 Configuration

The project uses configurable parameters such as:

```text
Embedding Model: BAAI/bge-small-en-v1.5
Chunk Size: 800
Chunk Overlap: 150
Top-K Retrieval: 4
Vector Database: ChromaDB
```

API credentials should be stored in an environment file and **must not be committed to GitHub**.

Example:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/souravstarcoder/NexusRAG.git
cd NexusRAG
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file and add your API key:

```env
GOOGLE_API_KEY=your_api_key_here
```

### 5. Build the Knowledge Base

Run the ingestion script:

```bash
python ingest.py
```

This processes the knowledge source and creates the vector store.

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💡 Example Use Case

NexusRAG can be adapted for:

- 📚 Company knowledge assistants
- 📄 Document Q&A systems
- 🎓 Study material assistants
- 🏢 Internal knowledge bases
- 📋 Policy/document search
- 🧑‍💻 Technical documentation assistants

---

## 🔮 Future Improvements

- Support for multiple PDF/document formats
- Conversational memory
- Source citation for retrieved documents
- Hybrid search
- Improved reranking
- Authentication and user management
- Cloud deployment
- Production-grade API using FastAPI/Spring Boot
- React-based frontend

---

## 👨‍💻 Author

**Sourav Mishra**

GitHub: https://github.com/souravstarcoder

---

## ⭐ If You Like This Project

If you find NexusRAG useful, consider giving the repository a ⭐ on GitHub.
