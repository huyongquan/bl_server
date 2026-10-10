import logging

import anthropic
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import config
import llm

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI(title="BL LLM Server", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    prompt: str
    model: str = ""
    system: str = ""
    thinking: bool = False


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/models")
async def models():
    return {"default": config.DEFAULT_MODEL, "models": config.AVAILABLE_MODELS}


@app.post("/chat")
async def chat(req: ChatRequest) -> str:
    """入参 prompt + model(可选),出参为模型的回答文本。"""
    if not req.prompt.strip():
        raise HTTPException(400, "prompt 不能为空")
    try:
        return await llm.chat(req.prompt, model=req.model, system=req.system, thinking=req.thinking)
    except anthropic.AnthropicError as e:
        logger.error(f"[chat] LLM 调用失败: {e}")
        raise HTTPException(502, f"LLM 调用失败: {e}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=config.PORT)
