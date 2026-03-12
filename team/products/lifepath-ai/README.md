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

### 环境变量配置

#### 后端环境变量
```bash
cd backend
cp .env.example .env
# 编辑 .env 文件，设置你的配置
```

关键环境变量：
- `LIFEPATH_JWT_SECRET`: JWT 密钥（生产环境必改）
- `DATABASE_URL`: 数据库连接字符串
- `HOST`/`PORT`: 服务监听地址

#### 前端环境变量
```bash
cd frontend
# .env 文件已包含默认配置
# 如需修改 API 地址，编辑 .env 文件
```

关键环境变量：
- `VITE_API_BASE_URL`: 后端 API 地址

### 一键启动（推荐 - Docker）

```bash
# 构建并启动所有服务
docker-compose up --build

# 后台运行
docker-compose up -d --build

# 查看日志
docker-compose logs -f

# 停止服务
docker-compose down
```

### 本地开发启动

```bash
# 后端
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

# 前端（新终端）
cd frontend
npm install
npm run dev
```

### Docker 启动（Task 4 完成后可用）
```bash
docker-compose up --build
```

- 前端地址：`http://localhost:5173`
- 后端 docs：`http://localhost:8000/docs`
- 健康检查：`http://localhost:8000/health`

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
