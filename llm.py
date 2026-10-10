import logging

import anthropic

import config

logger = logging.getLogger(__name__)

# 复用全局客户端(避免每次请求都新建连接)
_client: anthropic.AsyncAnthropic | None = None


def get_client() -> anthropic.AsyncAnthropic:
    global _client
    if _client is None:
        _client = anthropic.AsyncAnthropic(
            base_url=config.ANTHROPIC_BASE_URL,
            auth_token=config.ANTHROPIC_API_KEY,
        )
    return _client


async def chat(prompt: str, model: str = "", system: str = "") -> str:
    """调用 Anthropic 兼容接口,返回模型的文本回答。

    参考 knowledge-base-service 中 _free_chat 的调用方式。
    """
    client = get_client()
    model_name = model or config.DEFAULT_MODEL

    logger.info(f"[llm] model={model_name} prompt_len={len(prompt)}")
    response = await client.messages.create(
        model=model_name,
        max_tokens=config.MAX_TOKENS,
        system=system or None,
        messages=[{"role": "user", "content": prompt}],
    )

    answer = ""
    for block in response.content:
        if hasattr(block, "text"):
            answer += block.text
    logger.info(f"[llm] done, answer_len={len(answer)}")
    return answer.strip()
