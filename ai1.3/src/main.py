from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os

from models.request import AnalyzeRequest
from services.analyzer import run_analysis

load_dotenv()

app = FastAPI()

@app.post("/analyze")
async def analyze(data: AnalyzeRequest):
    try:
        gemini_key = os.getenv("GEMINI_API_KEY")
        openai_key = os.getenv("OPENAI_API_KEY")

        if not gemini_key or not openai_key:
            raise HTTPException(status_code=500, detail="API keys not set in .env")

        result = run_analysis(data.prompt, gemini_key, openai_key)
        return {"result": result}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
