# Semiconductor-Datasheet-AI-Chatbot

An AI-powered chatbot that enables natural-language querying of semiconductor datasheets to retrieve accurate technical specifications and parameters.

---

## Problem Statement

Engineers and students often spend a significant amount of time manually searching through large semiconductor datasheets to find specific electrical, thermal, or functional parameters. This process is inefficient and error-prone.

---

## Solution Overview

The Semiconductor Datasheet AI Chatbot ingests official semiconductor datasheets, converts them into semantic embeddings, stores them in a vector database, and allows users to ask natural-language questions. The system retrieves relevant datasheet sections and generates accurate answers strictly grounded in the source documents.

---

## Tech Stack Used

- Python  
- Hugging Face LLM (Qwen 1.5B / TinyLlama 1.1B)  
- BGE Embeddings  
- Qdrant Vector Database  
- Gradio UI  

---

## Project Structure
```
Chip AI Chatbot/
│
├── data/
│   ├── raw/                Input PDF datasheets
│   └── processed/          Extracted and processed text
│
├── vector_db/
│   └── qdrant/             Persistent vector database
│
├── ingest.py               PDF ingestion and text extraction
├── index.py                Vector index creation
├── query_engine.py         Query engine and model configuration
├── app.py                  Gradio-based UI
├── requirements.txt
└── README.md
```
---

## Installation and Setup

Clone the repository:

git clone https://github.com/jairajrenjith/semiconductor-datasheet-ai-chatbot.git  

cd semiconductor-datasheet-ai-chatbot

Create a virtual environment:

python -m venv venv

Activate the environment:

Windows:  
venv\Scripts\activate

Linux / macOS:  
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

---

## Adding Datasheets

1. Download official semiconductor datasheets in PDF format.
2. Place the PDFs inside the directory:

data/raw/

Only text-based (non-scanned) PDFs are supported.

---

## Running the System

Step 1: Ingest datasheets

python ingest.py

This extracts and preprocesses text from the datasheets.

Step 2: Build the vector index

python index.py

This generates embeddings and stores them in a persistent Qdrant vector database.

Step 3: Launch the chatbot interface

python app.py

Open a browser and navigate to:

http://127.0.0.1:7860

---

## Example Questions

- What is the supply voltage range of LM358?
- What is the operating temperature range of LM358?
- What is the input offset voltage of LM358?
- What is the maximum output current of LM358?

---

## Models Used

Embedding Model:
- BAAI/bge-small-en-v1.5

Language Models:
- TinyLlama 1.1B (fast and lightweight)
- Qwen 2.5 1.5B (higher accuracy)

Both language models use the same vector database for retrieval.

---

## Notes

- The vector database is persistent and does not need rebuilding unless new datasheets are added.
- Designed to run efficiently on CPU-based systems.
- Answers are grounded strictly in the provided datasheets.

---

## License

This project is intended for educational and research purposes only.
