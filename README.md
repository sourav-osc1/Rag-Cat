# Cats Facts RAG (Retrieval Augmented Generation)

A local Retrieval Augmented Generation system that leverages open-source models to answer questions about cat facts using vector similarity and context-aware language generation.

## Project Overview

This project implements a RAG pipeline that:

- Loads a dataset of cat facts
- Generates embeddings for semantic understanding
- Retrieves relevant context based on user queries
- Generates contextual responses using a language model

## Project Architecture

```
┌─────────────────────┐
│   Dataset Loading   │
│ (cats-facts-rag.txt)│
└──────────┬──────────┘
           │
           ▼
┌─────────────────────────────────┐
│   Embedding Generation          │
│ (BGE-base-en-v1.5 Model)        │
└──────────┬──────────────────────┘
           │
           ▼
┌─────────────────────────────────┐
│   Vector Database Storage       │
│ (In-Memory: chunk + embedding)  │
└─────────────────────────────────┘
           ▲
           │
    ┌──────┴──────┐
    │             │
    │ User Query  │
    │             │
    └──────┬──────┘
           │
           ▼
┌─────────────────────────────────┐
│   Query Embedding + Similarity  │
│   (Cosine Similarity Search)    │
└──────────┬──────────────────────┘
           │
           ▼
┌─────────────────────────────────┐
│   Retrieved Context (Top-N)     │
└──────────┬──────────────────────┘
           │
           ▼
┌─────────────────────────────────┐
│   Language Model Generation     │
│ (Llama-3.2-1B-Instruct)         │
└──────────┬──────────────────────┘
           │
           ▼
┌─────────────────────────────────┐
│   Final Response Output         │
└─────────────────────────────────┘
```

## Component Description

### 1. **Data Layer**

- **File**: `cats-facts-rag.txt`
- Stores individual cat facts as text chunks
- Each line is treated as a separate document chunk for embedding

### 2. **Embedding Module**

- **Model**: BGE-base-en-v1.5
- **Source**: Hugging Face Community (CompendiumLabs)
- Converts text chunks into 768-dimensional embeddings
- Enables semantic similarity comparison

### 3. **Vector Database**

- In-memory storage implemented as Python list of tuples
- Format: `(chunk_text, embedding_vector)`
- Structure: `VECTOR_DB = [(chunk, embedding), ...]`

### 4. **Retrieval Engine**

- Implements **Cosine Similarity** for semantic search
- Retrieves top-3 most relevant chunks by default
- Compares query embedding with all stored embeddings

### 5. **Generation Module**

- **Model**: Llama-3.2-1B-Instruct
- **Source**: Hugging Face Community (bartowski GGUF)
- Uses retrieved context as system prompt
- Generates context-aware responses

## Models Used

### Embedding Model

- **Name**: BGE-base-en-v1.5
- **Provider**: CompendiumLabs (Hugging Face)
- **Model ID**: `hf.co/CompendiumLabs/bge-base-en-v1.5-gguf`
- **Purpose**: Generate semantic embeddings for text chunks
- **Embedding Dimension**: 768

### Language Model

- **Name**: Llama-3.2-1B-Instruct
- **Provider**: Meta (bartowski GGUF quantization)
- **Model ID**: `hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF`
- **Purpose**: Generate context-aware responses
- **Parameters**: 1 Billion
- **Type**: Instruction-tuned variant

## Technology Stack

- **Runtime**: Python 3.10+
- **Model Serving**: Ollama
- **Key Dependency**: ollama>=0.6.1
- **Search Algorithm**: Cosine Similarity

## Setup & Installation

### Prerequisites

- Python 3.10 or higher
- Ollama installed and running locally

### Installation Steps

1. **Clone/Navigate to project**

```bash
cd /path/to/project
```

2. **Create virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
# Or if using pyproject.toml
pip install .
```

4. **Start Ollama** (in another terminal)

```bash
ollama serve
```

5. **Run the application**

```bash
python main.py
```

## Usage

1. The application loads all cat facts from `cats-facts-rag.txt`
2. Generates embeddings for each fact
3. Prompts the user for a question
4. Retrieves the 3 most relevant facts
5. Uses the language model to generate a contextual response

Example:

```
Ask me a question: What do cats eat?
Retrieved knowledge:
 - [relevant facts]
Chatbot response:
[Generated answer based on retrieved facts]
```

## How RAG Works

1. **Retrieval**: Find relevant documents based on query similarity
2. **Augmentation**: Combine retrieved context with the query
3. **Generation**: Use language model to generate response using augmented context

This approach ensures responses are grounded in the provided dataset and reduces hallucination.

## Project Structure

```
.
├── README.md                 # This file
├── main.py                   # Main RAG application
├── pyproject.toml            # Project configuration
├── cats-facts-rag.txt        # Dataset of cat facts
└── .venv/                    # Virtual environment (optional)
```

## Performance Considerations

- **Vector Database**: In-memory list (suitable for small datasets)
- **Similarity Calculation**: Cosine similarity (O(n) retrieval complexity)
- **Model Size**: 1B parameter model optimized for efficiency
- **Streaming**: Responses streamed for better UX

## Future Enhancements

- Persistent vector database (e.g., Pinecone, Weaviate, FAISS)
- Batch processing for large datasets
- Fine-tuned embedding model
- Multi-document support
- Response caching
- Pagination for large retrieval sets

## License

This project is licensed under the **MIT License** - see the LICENSE file for details.

### Third-Party Model Licenses

This project uses open-source models. Please refer to the respective model licenses:

- **BGE-base-en-v1.5**: Apache 2.0
- **Llama-3.2**: Meta License

---

**Created**: 26th April 2026
