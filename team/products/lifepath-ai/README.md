# LifePath AI - MVP

一个帮助你“晨间定动作 + 晚间做复盘 + 看板推进任务”的轻量系统。

## 🚀 现在已实现

- 账号注册/登录（JWT）
- 晨间建议：`POST /api/advice/morning`
- 晚间复盘：`POST /api/advice/evening`
- 记录分页：`GET /api/advice/journal?limit=&offset=`
- 前端任务看板：添加 / 勾选 / 删除（本地持久化）
- 新手引导：1 分钟看懂怎么用

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
