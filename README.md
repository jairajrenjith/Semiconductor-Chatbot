# Semiconductor-Chatbot

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
- Hugging Face LLM (Qwen 2.5 1.5B / TinyLlama 1.1B)  
- BGE Embeddings  
- Qdrant Vector Database  
- Gradio UI  

---

## Models Used

Embedding Model:
- BAAI/bge-small-en-v1.5

Language Models:
- TinyLlama 1.1B (fast and lightweight)
- Qwen 2.5 1.5B (higher accuracy)

Both language models use the same vector database for retrieval.

---

## Project Structure
```
Semiconductor-Chatbot/
│
├──.gradio/                 # Gradio runtime data and user-flagged interactions
│   └──flagged/             # Stored flagged queries and responses from the UI
│
├──_pycache_/               # Python bytecode cache (auto-generated)
│
├── data/
│   ├── raw/                # Input PDF datasheets
│   └── processed/          # Extracted and processed text
│
├── vector_db/
│   └── qdrant/             # Persistent vector database
│
├── ingest.py               # PDF ingestion and text extraction
├── index.py                # Vector index creation
├── query_engine.py         # Query engine and model configuration
├── app.py                  # Gradio-based UI
├── requirements.txt        # Python Dependencies
└── README.md               # Project Documentation
```
---

## Installation and Setup

1. Clone the repository:

    ```bash
    git clone <repo-link>
    ```

2. Goto the directory:

    ```bash
    cd Semiconductor-Chatbot
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the environment:

      a. Windows:
   
```
venv\Scripts\activate
```

      b. Linux / macOS:
   
```
source venv/bin/activate
```

6. Install dependencies:

      ```bash
      pip install -r requirements.txt
      ```

---

## Adding Datasheets

1. Download official semiconductor datasheets in PDF format.
2. Place the PDFs inside the directory:
```bash
data/raw/
```
Only text-based (non-scanned) PDFs are supported.

---

## Running the System

Step 1: Ingest datasheets
```bash
python ingest.py
```
This extracts and preprocesses text from the datasheets.

Step 2: Build the vector index
```bash
python index.py
```
This generates embeddings and stores them in a persistent Qdrant vector database.

Step 3: Launch the chatbot interface
```bash
python app.py
```
Open a browser and navigate to:
```bash
http://127.0.0.1:7860
```
---

## Example Questions

- What is the supply voltage range of LM358?
- What is the operating temperature range of LM358?
- What is the input offset voltage of LM358?
- What is the maximum output current of LM358?

---

## Notes

- The vector database is persistent and does not need rebuilding unless new datasheets are added.
- Designed to run efficiently on CPU-based systems.
- Answers are grounded strictly in the provided datasheets.

---

## License

This project is intended for educational and research purposes only.


By Jairaj R and Madhav R Nair.
