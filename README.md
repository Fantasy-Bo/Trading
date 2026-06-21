# TradingAgents-波波个股分析

面向 A 股个股研究的多 Agent 分析系统。项目基于 TradingAgents-Astock 继续改造，保留 A 股数据层、7 类分析师、质量门控、多空辩论、风险评估和最终交易决策流程。

仓库地址：https://github.com/Fantasy-Bo/Trading.git

> 免责声明：本项目仅供学习研究与技术演示，不构成任何投资建议。投资决策请咨询持牌专业机构，使用本工具产生的任何损失由使用者自行承担。

## 功能概览

- A 股个股代码或中文名称输入
- 7 类分析师报告：市场、情绪、新闻、基本面、政策、游资、解禁
- 多空研究员辩论与风险三方辩论
- Research Manager 与 Portfolio Manager 汇总决策
- 支持 Web UI、CLI、Markdown/PDF 报告导出
- 支持多家 LLM 供应商模型选择

## 最新默认模型

Web 侧栏和 CLI 共用模型目录，当前首选模型包括：

| 供应商 | 快速模型 | 深度模型 |
| --- | --- | --- |
| OpenAI | `gpt-5.5` | `gpt-5.5` |
| Anthropic | `claude-fable-5` | `claude-fable-5` |
| Google Gemini | `gemini-3.5-flash` | `gemini-3.1-pro-preview` |
| xAI | `grok-4.3` | `grok-4.3` |
| DeepSeek | `deepseek-v4-flash` | `deepseek-v4-pro` |
| 通义千问 Qwen | `qwen3.5-flash` | `qwen3-max` |
| 智谱 GLM | `glm-5.2` | `glm-5.2` |
| MiniMax | `MiniMax-M3` | `MiniMax-M3` |

OpenRouter 走动态/自定义模型 ID；Azure 使用你自己的部署名；Ollama 使用本地模型。

## 安装

```powershell
cd "C:\Users\ZHANG BO\Desktop\codex workspace\TradingAgents-波波个股分析V1"
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e .
```

如果需要 Gemini：

```powershell
.\.venv\Scripts\python.exe -m pip install -e ".[google]"
```

## 配置 API Key

复制 `.env.example` 为 `.env`，按你使用的供应商填写：

```env
OPENAI_API_KEY=
GOOGLE_API_KEY=
ANTHROPIC_API_KEY=
XAI_API_KEY=
DEEPSEEK_API_KEY=
DASHSCOPE_API_KEY=
ZHIPU_API_KEY=
MINIMAX_API_KEY=
OPENROUTER_API_KEY=
BACKEND_URL=
```

每家供应商用各自的环境变量，不要混用 `OPENAI_API_KEY`。

## 启动 Web UI

```powershell
cd "C:\Users\ZHANG BO\Desktop\codex workspace\TradingAgents-波波个股分析V1"
.\.venv\Scripts\bobo-trading-web.exe
```

兼容原命令：

```powershell
.\.venv\Scripts\tradingagents-web.exe
```

浏览器访问：

```text
http://localhost:8501
```

## CLI

```powershell
.\.venv\Scripts\bobo-trading.exe
```

兼容原命令：

```powershell
.\.venv\Scripts\tradingagents.exe
```

## 项目结构

```text
TradingAgents-波波个股分析V1/
├─ tradingagents/          # 核心 Agent、图流程、数据层、LLM 客户端
├─ web/                    # Streamlit Web UI
├─ cli/                    # CLI 入口
├─ tests/                  # 单元测试
├─ scripts/                # Smoke 测试脚本
├─ assets/                 # 图片资源
├─ pyproject.toml          # Python 包元数据
├─ LICENSE                 # Apache 2.0 许可证
└─ NOTICE                  # 来源与衍生项目说明
```

## 许可证与来源

本项目为 Apache 2.0 许可下的衍生项目。

- 当前项目：TradingAgents-波波个股分析，仓库 `https://github.com/Fantasy-Bo/Trading.git`
- 基于 TradingAgents-Astock，原作者 Simon / simonlin1212
- TradingAgents-Astock 基于 TauricResearch/TradingAgents

根据 Apache 2.0 要求，`LICENSE` 和 `NOTICE` 文件需要随项目保留。

## Streamlit Cloud 部署

最小成本云访问推荐使用 Streamlit Community Cloud。部署入口文件为：

```text
web/app.py
```

部署前把代码推送到：

```text
https://github.com/Fantasy-Bo/Trading.git
```

然后在 Streamlit Cloud 中配置 Secrets。示例见：

```text
.streamlit/secrets.toml.example
```

完整步骤见：

```text
STREAMLIT_CLOUD_DEPLOY.md
```
