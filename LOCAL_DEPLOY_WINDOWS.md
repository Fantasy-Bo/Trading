# TradingAgents-波波个股分析 本地部署包说明

这个压缩包用于换电脑后在 Windows 本地重新部署。包内包含完整项目源码、Web 页面、CLI、测试、示例、Docker 文件、requirements 和本地安装脚本。

## 不包含的内容

- `.env`：本地 API Key 文件，出于安全原因不打包。
- `.venv`：虚拟环境与本机路径绑定，换电脑后需要重新创建。
- `.git`、缓存、编译文件、egg-info：这些不影响运行。

## 新电脑部署步骤

1. 安装 Python 3.10 或 3.11，推荐 Python 3.11。
2. 解压本压缩包到一个固定目录，例如 `C:\Users\你的用户名\Desktop\TradingAgents-波波个股分析V1`。
3. 在项目目录打开 PowerShell。
4. 如果 PowerShell 阻止脚本运行，先执行：

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

5. 安装依赖并创建虚拟环境：

```powershell
.\INSTALL_LOCAL_WINDOWS.ps1
```

6. 打开 `.env`，填入你实际使用的模型 Key，例如：

```env
DEEPSEEK_API_KEY=你的DeepSeekKey
OPENAI_API_KEY=
ZHIPU_API_KEY=
```

7. 启动 Web：

```powershell
.\RUN_WEB_WINDOWS.ps1
```

8. 浏览器打开：

```text
http://localhost:8501/
```

## 常用命令

启动指定端口：

```powershell
.\RUN_WEB_WINDOWS.ps1 -Port 8502
```

安装时同时尝试安装 Google Gemini 依赖：

```powershell
.\INSTALL_LOCAL_WINDOWS.ps1 -WithGoogle
```

CLI 帮助：

```powershell
.\RUN_CLI_WINDOWS.ps1 --help
```

## 注意

- 修改 `.env` 后必须重启 Web 服务才会生效。
- DeepSeek 使用 `DEEPSEEK_API_KEY`，不是 `OPENAI_API_KEY`。
- 如果模型接口提示 `invalid api key`，说明服务端不接受该 Key，需要去对应供应商后台重新生成。
- 第一次安装依赖需要联网。安装完成后，正常运行仍需要联网访问行情、新闻和 LLM API。
