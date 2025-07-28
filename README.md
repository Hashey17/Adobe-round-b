Smart PDF Intelligence – Persona-Based Section Retrieval (Adobe Hackathon Round 1B)

Overview
This project was developed as part of Adobe India Hackathon 2025 – Round 1B under the theme "Connecting the Dots". The goal of this round was to retrieve the most relevant sections from a set of PDF documents based on a given user persona and task. The extracted information had to be ranked and presented in structured JSON format.
All processing was required to be completed offline within 60 seconds using only CPU resources.

Problem Statement
Given:
Multiple PDF documents
A user persona (e.g., marketing analyst, legal intern, student)
A specific task (e.g., identify key marketing insights, extract company risk disclosures)

Build a system that:
Understands the semantic meaning of the persona-task query
Searches through the PDF content efficiently
Returns the most relevant sections as a ranked list
Runs offline inside a Docker container under 60 seconds

Solution Overview
We designed a semantic search system powered by sentence embeddings. Here's how it works:
Load and chunk the content from all PDFs using PyMuPDF.
Convert each chunk and the user’s task into embeddings using Sentence Transformers (MiniLM model).
Compute cosine similarity scores between the persona-task query and each chunk.
Rank the chunks by similarity score and format the top results into a clean JSON structure.
Package everything inside a Docker container for reproducibility and offline execution.
