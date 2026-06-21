# Streamlit Cloud 部署说明

本文档用于把 `TradingAgents-波波个股分析` 部署到 Streamlit Community Cloud，部署后手机和电脑都可以通过公网链接访问。

## 1. 准备 GitHub 仓库

仓库地址：

```text
https://github.com/Fantasy-Bo/Trading.git
```

提交前确认不要把真实密钥提交到 GitHub：

- `.env`
- `.streamlit/secrets.toml`
- 任何包含 API Key 的截图或日志

项目已经包含：

- `requirements.txt`：Streamlit Cloud 安装依赖使用
- `.streamlit/secrets.toml.example`：Secrets 示例，不含真实密钥
- `web/app.py`：Streamlit 入口文件

## 2. 创建 Streamlit Cloud App

在 Streamlit Community Cloud 新建应用：

```text
Repository: Fantasy-Bo/Trading
Branch: main
Main file path: web/app.py
```

高级设置保持默认即可。项目要求 Python 3.10 或更高版本。

## 3. 配置 Secrets

进入 App 的 Settings -> Secrets，把 `.streamlit/secrets.toml.example` 里的内容复制进去，然后只填写需要使用的供应商。

至少建议填写：

```toml
APP_USERNAME = ""
APP_PASSWORD = "换成你自己的访问密码"

MINIMAX_API_KEY = ""
DEEPSEEK_API_KEY = ""
DASHSCOPE_API_KEY = ""
ZHIPU_API_KEY = ""
OPENAI_API_KEY = ""
ANTHROPIC_API_KEY = ""
GOOGLE_API_KEY = ""
XAI_API_KEY = ""
OPENROUTER_API_KEY = ""
BACKEND_URL = ""
ALPHA_VANTAGE_API_KEY = ""
```

说明：

- `APP_PASSWORD` 有值时，打开页面需要先输入密码。
- `APP_USERNAME` 可以留空；留空时只校验密码。
- 只填你实际使用的 LLM 供应商 API Key。
- 如果使用第三方中转或代理网关，填写 `BACKEND_URL`。

## 4. 部署后访问

部署完成后，Streamlit 会生成一个公网地址，类似：

```text
https://your-app-name.streamlit.app
```

手机直接打开这个地址即可，不需要电脑开机，也不需要本地端口 `8501`。

## 5. 本地测试登录

本地测试可以在 `.env` 中设置：

```env
APP_USERNAME=
APP_PASSWORD=your-local-password
```

然后启动：

```powershell
.\.venv\Scripts\bobo-trading-web.exe
```

如果 `APP_PASSWORD` 为空，本地不会显示登录页。

## 6. 常见问题

### 页面能打开，但模型报 API Key 缺失

检查 Streamlit Cloud 的 Secrets 是否填写了对应供应商的变量名。例如：

- OpenAI：`OPENAI_API_KEY`
- DeepSeek：`DEEPSEEK_API_KEY`
- 通义千问 Qwen：`DASHSCOPE_API_KEY`
- 智谱 GLM：`ZHIPU_API_KEY`
- MiniMax：`MINIMAX_API_KEY`
- Claude：`ANTHROPIC_API_KEY`
- Gemini：`GOOGLE_API_KEY`
- xAI：`XAI_API_KEY`
- OpenRouter：`OPENROUTER_API_KEY`

### 部署后网页空白或安装失败

先查看 Streamlit Cloud 的 Logs。常见原因是依赖安装失败、Python 版本过低，或某个包临时下载失败。

### 访问速度慢

Streamlit Community Cloud 的免费服务不适合高并发，也可能受网络线路影响。只给自己手机看通常够用；如果要给多人稳定使用，再考虑云服务器或付费托管。
