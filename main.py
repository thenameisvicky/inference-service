from fastapi import FastAPI
from pydantic import BaseModel
from llama_cpp import Llama
from os import getenv

app = FastAPI(title="GGUF CPU Inference Service")

MODEL_PATH = getenv("MODEL_PATH")

print(f"Loading GGUF model from {MODEL_PATH}...")
llm = Llama(model_path=MODEL_PATH)

class Prompt(BaseModel):
    prompt: str

@app.post("/api/v1/infer")
def infer(data: Prompt):
    output = llm(data.prompt, max_tokens=100, temperature=0.7)
    return {"response": output['choices'][0]['text']}
    