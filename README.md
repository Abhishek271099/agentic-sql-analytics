# Agentic SQL Analytics Service

An Agentic AI-powered backend service that answers natural language questions over structured sales data using Azure SQL and Azure OpenAI.

The system converts user queries into safe, validated SQL using an LLM-based SQL agent, retrieves relevant data from the database, and then generates a grounded, human-readable response based strictly on the retrieved data.

---

## 🚀 Key Features

- Natural Language → SQL query generation using an LLM
- Schema-aware SQL generation for higher accuracy
- SQL safety validation to prevent destructive queries
- Data-grounded response generation (no hallucinations)
- Modular agent-based architecture
- Built with FastAPI for scalability and clean APIs

---

## 🧠 Architecture Overview

1. **User Query**
   - User submits a natural language question

2. **SQL Agent**
   - LLM generates a SQL query using provided table schemas
   - Query is cleaned and validated (SELECT-only enforcement)

3. **SQL Execution**
   - Validated query is executed against Azure SQL
   - Results are returned as structured data

4. **Response Agent**
   - A second LLM interprets the SQL result
   - Generates a clear, human-readable response strictly based on the data

---

## 📂 Project Structure

```text
.
├── app.py
├── requirements.txt
├── .env
└── src
    ├── agent.py              # SQLAgent and ResponseAgent
    ├── agent_prompt.py       # Prompts for agents
    ├── llm_service.py        # Azure OpenAI client wrapper
    ├── sql_service.py        # Azure SQL access layer
    ├── validator.py          # SQL safety validation
    ├── schemas.py            # Table schemas used for SQL generation
    └── utils.py              # Helper utilities
