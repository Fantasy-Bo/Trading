"""Shared model catalog for CLI selections and validation."""

from __future__ import annotations

from typing import Dict, List, Tuple

ModelOption = Tuple[str, str]
ProviderModeOptions = Dict[str, Dict[str, List[ModelOption]]]


MODEL_OPTIONS: ProviderModeOptions = {
    "openai": {
        "quick": [
            ("GPT-5.5 - Latest flagship, best tool-heavy workflows", "gpt-5.5"),
            ("GPT-5.4 Mini - Fast, strong coding and tool use", "gpt-5.4-mini"),
            ("GPT-5.4 Nano - Cheapest, high-volume tasks", "gpt-5.4-nano"),
            ("GPT-5.4 - Prior frontier, lower-cost fallback", "gpt-5.4"),
            ("GPT-4.1 - Smartest non-reasoning model", "gpt-4.1"),
            ("Custom model ID", "custom"),
        ],
        "deep": [
            ("GPT-5.5 - Latest flagship for complex reasoning and coding", "gpt-5.5"),
            ("GPT-5.4 - Prior frontier, lower-cost fallback", "gpt-5.4"),
            ("GPT-5.4 Mini - Fast, strong coding and tool use", "gpt-5.4-mini"),
            ("Custom model ID", "custom"),
        ],
    },
    "anthropic": {
        "quick": [
            ("Claude Fable 5 - Latest highest-capability model", "claude-fable-5"),
            ("Claude Sonnet 4.6 - Best speed and intelligence balance", "claude-sonnet-4-6"),
            ("Claude Haiku 4.5 - Fast, near-instant responses", "claude-haiku-4-5"),
            ("Custom model ID", "custom"),
        ],
        "deep": [
            ("Claude Fable 5 - Latest highest-capability model", "claude-fable-5"),
            ("Claude Opus 4.8 - Latest Opus tier for complex workflows", "claude-opus-4-8"),
            ("Claude Sonnet 4.6 - Best speed and intelligence balance", "claude-sonnet-4-6"),
            ("Custom model ID", "custom"),
        ],
    },
    "google": {
        "quick": [
            ("Gemini 3.5 Flash - Latest stable fast model", "gemini-3.5-flash"),
            ("Gemini 3 Flash - Preview fast fallback", "gemini-3-flash-preview"),
            ("Gemini 2.5 Flash - Balanced, stable", "gemini-2.5-flash"),
            ("Gemini 3.1 Flash Lite - Most cost-efficient", "gemini-3.1-flash-lite-preview"),
            ("Custom model ID", "custom"),
        ],
        "deep": [
            ("Gemini 3.1 Pro - Latest pro preview for complex workflows", "gemini-3.1-pro-preview"),
            ("Gemini 3.5 Flash - Latest stable fast model", "gemini-3.5-flash"),
            ("Gemini 2.5 Pro - Stable pro model", "gemini-2.5-pro"),
            ("Custom model ID", "custom"),
        ],
    },
    "xai": {
        "quick": [
            ("Grok 4.3 - Latest recommended general model", "grok-4.3"),
            ("Grok 4.1 Fast (Non-Reasoning) - Speed optimized, 2M ctx", "grok-4-1-fast-non-reasoning"),
            ("Grok 4 Fast (Non-Reasoning) - Speed optimized", "grok-4-fast-non-reasoning"),
            ("Custom model ID", "custom"),
        ],
        "deep": [
            ("Grok 4.3 - Latest recommended general model", "grok-4.3"),
            ("Grok 4 - Flagship reasoning model", "grok-4"),
            ("Grok Build 0.1 - Specialized coding agent model", "grok-build-0.1"),
            ("Grok 4.1 Fast (Reasoning) - High-performance, 2M ctx", "grok-4-1-fast-reasoning"),
            ("Custom model ID", "custom"),
        ],
    },
    "deepseek": {
        "quick": [
            ("DeepSeek V4 Flash - Latest V4 fast model", "deepseek-v4-flash"),
            ("DeepSeek V3.2", "deepseek-chat"),
            ("Custom model ID", "custom"),
        ],
        "deep": [
            ("DeepSeek V4 Pro - Latest V4 flagship model", "deepseek-v4-pro"),
            ("DeepSeek V3.2 (thinking)", "deepseek-reasoner"),
            ("DeepSeek V3.2", "deepseek-chat"),
            ("Custom model ID", "custom"),
        ],
    },
    "qwen": {
        "quick": [
            ("Qwen 3.5 Flash - Latest fast Qwen model", "qwen3.5-flash"),
            ("Qwen 3.5 Plus - Latest balanced model", "qwen3.5-plus"),
            ("Qwen Plus - Stable fallback", "qwen-plus"),
            ("Custom model ID", "custom"),
        ],
        "deep": [
            ("Qwen 3 Max - Latest flagship model", "qwen3-max"),
            ("Qwen 3.5 Plus", "qwen3.5-plus"),
            ("Qwen 3.6 Plus - Compatibility fallback", "qwen3.6-plus"),
            ("Custom model ID", "custom"),
        ],
    },
    "glm": {
        "quick": [
            ("GLM-5.2 - Latest flagship model", "glm-5.2"),
            ("GLM-5-Turbo - Latest efficient GLM-5 model", "glm-5-turbo"),
            ("GLM-4.7-FlashX - Fast lightweight fallback", "glm-4.7-flashx"),
            ("Custom model ID", "custom"),
        ],
        "deep": [
            ("GLM-5.2 - Latest flagship model", "glm-5.2"),
            ("GLM-5-Plus - Strong stable GLM-5 fallback", "glm-5-plus"),
            ("GLM-5-Turbo - Efficient GLM-5 fallback", "glm-5-turbo"),
            ("Custom model ID", "custom"),
        ],
    },
    "minimax": {
        "quick": [
            ("MiniMax-M3 - Latest model, thinking can be disabled for speed", "MiniMax-M3"),
            ("MiniMax-M2.7-highspeed - Fast fallback", "MiniMax-M2.7-highspeed"),
            ("MiniMax-M2.5-highspeed - Stable fast model", "MiniMax-M2.5-highspeed"),
            ("Custom model ID", "custom"),
        ],
        "deep": [
            ("MiniMax-M3 - Latest flagship model", "MiniMax-M3"),
            ("MiniMax-M2.7 - Previous flagship fallback", "MiniMax-M2.7"),
            ("MiniMax-M2.5 - Stable flagship model", "MiniMax-M2.5"),
            ("Custom model ID", "custom"),
        ],
    },
    # OpenRouter: fetched dynamically. Azure: any deployed model name.
    "ollama": {
        "quick": [
            ("Qwen3:latest (8B, local)", "qwen3:latest"),
            ("GPT-OSS:latest (20B, local)", "gpt-oss:latest"),
            ("GLM-4.7-Flash:latest (30B, local)", "glm-4.7-flash:latest"),
        ],
        "deep": [
            ("GLM-4.7-Flash:latest (30B, local)", "glm-4.7-flash:latest"),
            ("GPT-OSS:latest (20B, local)", "gpt-oss:latest"),
            ("Qwen3:latest (8B, local)", "qwen3:latest"),
        ],
    },
}


def get_model_options(provider: str, mode: str) -> List[ModelOption]:
    """Return shared model options for a provider and selection mode."""
    return MODEL_OPTIONS[provider.lower()][mode]


def get_known_models() -> Dict[str, List[str]]:
    """Build known model names from the shared CLI catalog."""
    return {
        provider: sorted(
            {
                value
                for options in mode_options.values()
                for _, value in options
                if value != "custom"
            }
        )
        for provider, mode_options in MODEL_OPTIONS.items()
    }
