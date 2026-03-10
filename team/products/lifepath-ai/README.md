# LifePath AI - MVP

一个帮助你“晨间定动作 + 晚间做复盘 + 看板推进任务”的轻量系统。

## 🚀 现在已实现

- 账号注册/登录（JWT）
- 晨间建议：`POST /api/advice/morning`
- 晚间复盘：`POST /api/advice/evening`
- 记录分页：`GET /api/advice/journal?limit=&offset=`
- 前端任务看板：添加 / 勾选 / 删除（本地持久化）
- 新手引导：1 分钟看懂怎么用
- 可插拔模型适配：`heuristic` / `ollama` / `openai_compat`（可接 DeepSeek / 兼容 OpenAI 协议服务）

## 🧱 技术栈

- Frontend: React + TypeScript + Vite
- Backend: FastAPI + SQLite
- Auth: JWT (PyJWT)

## 📁 目录结构

- `backend/` API 服务
- `frontend/` Web UI
- `docs/` 使用手册、开发记录

## ⚡ 快速启动

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

- 前端地址：`http://localhost:5173`
- 后端 docs：`http://localhost:8000/docs`

## 🔌 模型接入（OSS-first）

后端支持以下 provider（默认 `heuristic`）：

- `heuristic`：本地规则引擎（零依赖）
- `ollama`：接本地开源模型（如 qwen2.5 / llama3）
- `openai_compat`：接 OpenAI 协议兼容服务（可配置 DeepSeek）

环境变量示例：

```bash
LIFEPATH_MODEL_PROVIDER=openai_compat
LIFEPATH_OPENAI_BASE_URL=https://api.deepseek.com/v1
LIFEPATH_OPENAI_MODEL=deepseek-chat
# LIFEPATH_OPENAI_API_KEY 可不写，系统会尝试从 ~/.openclaw/secret/selfdeployDeepSeekV3Key 读取
```

> 安全：不要把 API key 提交到仓库。

## 📘 图文手册（高中生可读）

请看：`docs/GUIDE_ZH_CN.md`

包含：
- 一分钟新手流程
- 文本示意图
- 每天使用节奏图（mermaid）
- 常见问题与接口说明

## 🔐 API 约定

- 受保护接口需携带：`Authorization: Bearer <token>`
- 统一错误结构：

```json
{
  "success": false,
  "error": {
    "code": "HTTP_ERROR",
    "message": "Invalid credentials"
  }
}
```
