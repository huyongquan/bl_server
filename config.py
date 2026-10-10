import os

# Anthropic 兼容网关(阿里云 MaaS),与 knowledge-base-service 保持一致
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "sk-sp-H.IMDY.ub05.MEYCIQCursP6FGTKbIKR3BIBAKnbVfuLW4TifWeiewRy8WoTtwIhAM5PR2L96WuA8ZHdQVB81jMdqQ4WLzpVV0GDz_536JpL")
ANTHROPIC_BASE_URL = os.environ.get("ANTHROPIC_BASE_URL", "https://token-plan.cn-beijing.maas.aliyuncs.com/apps/anthropic")

# 默认模型(入参未传 model 时使用)
DEFAULT_MODEL = "glm-5.3"

# 可选模型列表(用于 /models 接口)
AVAILABLE_MODELS = [
    "qwen3.8-max",
    "qwen3.8-flash",
    "qwen3.7-plus",
    "qwen3.7-max",
    "qwen3.6-plus",
    "qwen3.6-flash",
    "deepseek-v4.1-flash",
    "deepseek-v4-pro-0813",
    "deepseek-v4-pro",
    "deepseek-v4-flash-0731",
    "kimi-k2.5",
    "kimi-k2.6",
    "glm-5.3",
    "glm-5.2",
    "glm-5.1",
    "glm-5",
]

MAX_TOKENS = 4096
PORT = 8002
