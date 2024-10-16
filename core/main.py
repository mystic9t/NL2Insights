"""run project as a FastAPI endpoint"""
# Planned structure
## API calls to receive conversation history
## History Engine to summarize previous conversations and extract information relevant to keep the conversation going
## Research Engine to analyze the request, search through connected corpus, and put together a report
## Execution Engine to use the report to construct a prompt and generate required output, validate generation and summarize the output to be ready for display
## Evaluation Engine to trace over all calls, maintain intermediate outputs and count tokens going in and out
## Pre-Processor to convert and store user documents into a Vector DB
## Generation Engine to make LLM and Embeddings calls
## Self-play to show agent-like behavior.  

from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

@app.get("/process")
async def process_query(query:str):
    try:
        return "Success"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5102)