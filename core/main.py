# Planned structure
## API calls to receive conversation history
## History Engine to summarize previous conversations and extract information relevant to keep the conversation going
## Research Engine to analyze the request, search through connected corpus, and put together a report
## Execution Engine to use the report to construct a prompt and generate required output, validate generation and summarize the output to be ready for display
## Evaluation Engine to trace over all calls, maintain intermediate outputs and count tokens going in and out
## Pre-Processor to convert and store user documents into a Vector DB
## Generation Engine to make LLM and Embeddings calls
## Self-play to show agent-like behavior.  