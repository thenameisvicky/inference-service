from fastapi import FastAPI
from pydantic import BaseModel
from llama_cpp import Llama

app = FastAPI(title="GGUF CPU Inference Service")

MODEL_PATH = "/home/thenameisvicky/Documents/quant_neural_models/mistral_7B_Q4.gguf"

print("Loading GGUF model...")
llm = Llama(model_path=MODEL_PATH)

class Prompt(BaseModel):
    prompt: str

@app.post("/infer")
def infer(data: Prompt):
    output = llm(data.prompt, max_tokens=50, temperature=0.7, stop=['\n'])
    return {"response" : output['choices']}