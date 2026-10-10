"""测试各模型是否支持 thinking disabled。"""
import asyncio

import anthropic

import config


async def test_model(client, model):
    try:
        resp = await client.messages.create(
            model=model,
            max_tokens=64,
            thinking={"type": "disabled"},
            messages=[{"role": "user", "content": "hi"}],
        )
        return model, "支持 disabled", resp.stop_reason
    except anthropic.AnthropicError as e:
        return model, "不支持", str(e)[:120]


async def main():
    client = anthropic.AsyncAnthropic(
        base_url=config.ANTHROPIC_BASE_URL,
        auth_token=config.ANTHROPIC_API_KEY,
    )
    # 并发测试所有模型
    results = await asyncio.gather(*(test_model(client, m) for m in config.AVAILABLE_MODELS))
    print(f"{'模型':<28} {'结论':<12} 说明")
    print("-" * 90)
    for model, verdict, detail in results:
        print(f"{model:<28} {verdict:<12} {detail}")


if __name__ == "__main__":
    asyncio.run(main())
