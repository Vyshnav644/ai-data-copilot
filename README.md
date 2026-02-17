# AI Business Analytics Assistant

An AI-powered analytics assistant that lets users explore business data using natural language.
# 🚀 AI Data Copilot — Conversational Analytics Assistant

An AI-powered analytics tool that allows users to explore datasets using natural language.

The system understands informal queries, detects user intent, performs analysis, and generates visualizations — all grounded in the uploaded dataset.

---
## 🌐 Live Demo

Try it here:
https://ai-data-copilot-ekzttqfh7wmrqe9xdbgqgf.streamlit.app

## 🧠 Pipeline Architecture

User Query (Natural Language)

Intent Detection

Rule-based routing

Lightweight LLM fallback

Entity Extraction

Year detection

Metric detection

Category detection

Query Planning Layer

Summary

Trend

Comparison

Forecast

Data Engine

Pandas processing

Optional SQL backend

Visualization Engine

Dynamic chart selection

User-selectable graph types

Insight Layer (Optional)

AI-generated explanation

Streamlit Interface

Interactive dashboard

Dataset upload support


The system processes natural language queries by first detecting intent and extracting relevant entities such as time periods or metrics. It then plans the analysis, executes data operations using Pandas or SQL, generates visualizations, and optionally provides AI-driven explanations — all delivered through an interactive dashboard.


---

## ⚙️ Key Features

- Conversational query interface
- Informal prompt understanding
- Year vs year comparison
- Trend analysis
- Dynamic chart generation
- Chart type selection
- Dataset uploader (works with any CSV / Excel)
- Fast response optimization
- Interactive dashboard
- Grounded responses using dataset only

---

## 🛠 Tech Stack

- Python
- Streamlit
- Pandas
- Plotly
- LangChain
- Ollama (local LLM)
- Regex-based entity detection

---

## 🧩 System Components

dashboard.py → User interface + orchestration  
sql_agent.py → Natural language to SQL execution  
router.py → Query routing logic  
forecasting.py → Predictive analysis  
memory.py → Conversation context  
dataset loader → Data ingestion  

---

## 📊 Example Queries

- Compare 2017 vs 2018 sales
- Show trend over time
- What insights can you give?
- Total revenue
- Plot performance
- Explain results

---

## 🎯 Project Goal

To demonstrate how LLMs can be integrated with data pipelines to build an intelligent analytics assistant capable of interpreting natural language and supporting decision-making.

---

## 🚀 Future Improvements

- Advanced anomaly detection
- RAG-based knowledge grounding
- Multi-agent planning
- Cloud deployment
- Real-time streaming data

---




