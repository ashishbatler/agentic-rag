# Agentic RAG System

## Overview
An advanced Retrieval-Augmented Generation system using LangGraph, hybrid retrieval, and pgvector.

## Features
- Hybrid search (vector + BM25)
- HNSW indexing
- Query rewriting
- Agentic workflow
- FastAPI endpoint

## Tech Stack
- LangGraph
- PostgreSQL + pgvector
- Jina embeddings
- OpenAI
- FastAPI

## .env file under agentic-rag folder

DB_NAME=rag_db
DB_USER=postgres
DB_PASSWORD=
DB_HOST=localhost
OPENAI_API_KEY=yourKey

## Setup
```bash
pip install -r requirements.txt
