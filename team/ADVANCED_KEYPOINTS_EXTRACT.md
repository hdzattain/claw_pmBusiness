# Advanced Docs Keypoints Extract

Source root: C:\Users\70924\JohnsonWork\research_project\vibevibe\vibe-vibe\docs\Advanced

Total files read: 101

## 01-environment-setup\00-quick-start.md
- Summary line: title: "1.0 快速开始"
- Headings: 1.0 快速开始 | Windows 用户 {#windows-users} | 1. 安装 [Git](https://git-scm.com/install/windows) | 2. 安装 [Node.js](https://nodejs.org/zh-cn/download)![image-20260203180429883](/images/Advanced/image-20260203180429883.png) | 3. 验证安装 | 4. 配置国内镜像源并安装 pnpm | 5. 安装 Claude Code | Mac/Linux 用户 {#mac-linux-users}
- Key bullets: 首次在终端输入 `git` 会提示安装 Xcode 命令行工具，点击安装即可 | 或主动执行：`xcode-select --install` | 如需最新版本，可用 Homebrew：`brew install git` | **Mac**：按 `Cmd + Space`，输入 "Terminal" | **Linux**：按 `Ctrl + Alt + T` | [1.1 代码格式演变](./01-code-formats.md)

## 01-environment-setup\01-code-formats.md
- Summary line: title: "1.1 代码格式演变"
- Headings: 1.1 代码格式演变 | 网页的三层结构 | 为什么保存的网页有的打不开？ | 代码格式的四个阶段 | 阶段 1：单文件 HTML | 阶段 2：文件分离 | 阶段 3：模块化 | 阶段 4：TypeScript 工程化
- Key bullets: 类型系统减少错误 | AI 更擅长生成类型安全的代码 | 现代前端开发的标配 | `.ts` 或 `.tsx` 文件需要通过 `pnpm dev` 运行 | 看到 `: string` 这种类型标注时，知道这是 TypeScript 即可 | 详见：[1.2 技术栈概念](./02-tech-stack.md)

## 01-environment-setup\02-tech-stack.md
- Summary line: title: "1.2 技术栈概念"
- Headings: 1.2 技术栈概念 | 技术栈是什么 | 本教程的技术栈 | 为什么选这套技术栈 | 需要用户认证？现成的 | 需要处理时间？现成的 | 需要验证数据？现成的 | 快速识别项目技术栈
- Key bullets: **前端**：用户看到的界面（HTML、CSS、JavaScript） | **后端**：服务器端逻辑，处理数据（Node.js、Python） | **数据库**：存储数据（PostgreSQL、MongoDB） | 用户系统（登录、注册、权限） | 数据持久化（保存用户数据） | 业务逻辑（支付、通知、邮件）

## 01-environment-setup\03-browser-server.md
- Summary line: title: "1.3 浏览器与服务器基础"
- Headings: 1.3 浏览器与服务器基础 | 基本概念 | Web 应用工作流程 | 浏览器 vs 服务器 | 为什么需要 Node.js | 开发环境 vs 生产环境 | 运行环境差异 | 相关内容
- Key bullets: 在你的电脑上运行构建工具 | 编译 TypeScript 为 JavaScript | 打包代码 | 启动开发服务器 | TypeScript 项目（需要编译） | 使用 npm 包（需要管理依赖）

## 01-environment-setup\04-terminal-basics.md
- Summary line: title: "1.4 Terminal 终端入门"
- Headings: 1.4 Terminal 终端入门 | 前置知识 | 核心概念 | 实战步骤 | 打开终端 | 提示符是什么？ | 复制粘贴操作 | 基本文件操作
- Key bullets: **终端（Terminal）**：你看到的**界面窗口**，用来输入命令。Windows 上叫 PowerShell/CMD，Mac 上叫 Terminal/iTerm2 | **Shell（壳）**：隐藏在终端后的**命令解释器**，读取你的输入并执行。常见的是 bash、zsh（Mac 默认）、PowerShell（Windows） | **命令行（CLI）**：通过文本指令操作计算机的**方式**，相比图形界面更高效、更精确 | 按 `Command + Space`，输入 "Terminal" | 或在 Finder → 应用程序 → 实用工具 → 终端 | 按 `Win + R`，输入 `powershell` 或 `Windows Terminal`

## 01-environment-setup\05-package-manager-and-config.md
- Summary line: title: "1.5 包管理与项目配置"
- Headings: 1.5 包管理与项目配置 | 基本概念 | 为什么选择 pnpm？ | pnpm 常用命令 | 项目依赖命令 | 全局安装命令 | 安装全局 CLI 工具 | 核心配置文件
- Key bullets: **add xxx**：生产依赖，项目运行时需要 | **add -D xxx**：开发依赖，仅开发时需要 | **CLI 工具**：如 Claude Code、http-server、create-react-app | **系统级工具**：如 nrm（镜像源管理）、vercel（部署工具） | 自动生成，**不要手动修改** | 必须提交到 Git

## 01-environment-setup\06-models-and-tools.md
- Summary line: title: "1.6 模型与工具"
- Headings: 1.6 模型与工具 | 基本概念 | AI 模型 | 主流工具概览 | 配置 GLM 模型 | 步骤 1：购买编码套餐 | 步骤 2：自动配置 | 输入获取到的 API Key，工具会自动完成所有配置
- Key bullets: 左边是 VS Code/Trae 等编辑器，方便浏览和查看文件 | 底部终端运行 Claude Code 等 CLI 工具，让它帮你改代码 | 一边看文件结构，一边让 CLI 工具干活 | **公开可用**：发布在 npm 仓库，无地域限制 | **多模型支持**：可接入国内模型（GLM、DeepSeek 等） | **工作流强大**：文件操作、代码搜索、Git 集成、子代理协作

## 01-environment-setup\07-creating-project.md
- Summary line: title: "1.7 创建项目"
- Headings: 1.7 创建项目 | 准备工作 | 创建项目文件夹 | 在文件夹中打开终端 | 什么是文件路径 | 命名规范 | 创建项目 | 创建 Next.js 项目（my-app 是项目名，可以改）
- Key bullets: ✅ 使用小写英文字母 | ✅ 使用连字符 `-` 分隔单词 | ❌ 避免中文字符、空格、特殊字符 | **TypeScript**：推荐选择 Yes | **ESLint**：推荐选择 Yes | **Tailwind CSS**：根据需要选择

## 01-environment-setup\08-localhost-and-ports.md
- Summary line: title: "1.8 Localhost 与端口"
- Headings: 1.8 Localhost 与端口 | 基本概念 | Localhost 本地主机 | 端口 Port | 启动开发服务器 | 进入项目目录（my-app 改为你创建的项目名） | 安装依赖（首次运行） | 启动开发服务器
- Key bullets: **0-1023**：系统端口，需要管理员权限 | **1024-49151**：注册端口，常见服务使用 | **49152-65535**：动态端口，临时使用 | Local:        http://localhost:3000 | Network:      http://192.168.1.100:3000 | 第一次打开项目

## 01-environment-setup\index.md
- Summary line: title: "第一章：环境搭建与代码运行基础"
- Headings: 第一章：环境搭建与代码运行基础 | 序言 | 代码格式 | TypeScript 与 Node.js | nvm 版本管理 | 终端入门 | 开源代码包 | pnpm 包管理器

## 02-ai-tuning-guide\00-recommended-config.md
- Summary line: title: "2.0 推荐配置"
- Headings: 2.0 推荐配置 | 1. 安装插件 | 推荐插件 | 2. 安装 CC-SWITCH | Windows 用户 | macOS 用户 | Linux 用户 | 3. 基本配置
- Key bullets: **主界面**：选择供应商 → 点击"启用" | **系统托盘**：直接点击供应商名称（立即生效） | **发现技能**：自动扫描预配置的 GitHub 仓库（Anthropic 官方、ComposioHQ、社区等） | **自定义仓库**：支持添加自定义仓库（支持子目录扫描） | **安装技能**：点击"安装"一键安装到 `~/.claude/skills/` | **卸载技能**：点击"卸载"安全移除并清理状态

## 02-ai-tuning-guide\01-ai-economics.md
- Summary line: title: "2.1 AI 编程的经济学"
- Headings: 2.1 AI 编程的经济学 🔴 | 前置知识 | 核心概念 | 花费从哪里来 | 成本与质量优化策略 | 优化原则 | 示例对比 | 实战建议
- Key bullets: 1 个汉字 ≈ 1 Token | 1 个英文单词 ≈ 0.75 Token | 1 行代码 ≈ 5-15 Token | 单次调用很便宜，但累积起来也是钱 | **上下文越大 = 花费越高**：读取整个项目 vs 只读一个文件，差异是数量级的 | 频繁调试时要注意：循环修改会不断累积 Token

## 02-ai-tuning-guide\02-vibecoding-workflow.md
- Summary line: title: "2.2 VibeCoding 工作流"
- Headings: 2.2 VibeCoding 工作流 | 前置知识 | 传统思维 vs Agent Native | VibeCoding 的核心哲学：你是导演，AI 是演员 | AI 与人的分工：预测与判断 | Agent Native 的三大原则 | 你设定目标，AI 自主执行 | 从开发者到编排者
- Key bullets: 功能测试：跑一下看看能不能用 | 类型检查：`tsc` 有没有报错 | 代码审查：只看关键逻辑，不看实现细节 | 不要让 AI 猜 → 提供明确上下文 | 不要含糊其辞 → 给出具体要求 | 不要强行编造 → 给 AI 一个"不确定"的出口

## 02-ai-tuning-guide\03-mcp-and-skills.md
- Summary line: title: "2.3 MCP、插件与 Skills"
- Headings: 2.3 MCP、插件与 Skills 🟡 | 前置知识 | 你必须知道的 AI 能力范围 | AI 有哪些能力 | 按类型分类的工具表 | 打开插件管理界面 | 搜索 typescript-lsp 或 pyright-lsp 并安装 | 判断标准：内置够用还是需要扩展？
- Key bullets: 插件市场：[claude-plugins.dev](https://claude-plugins.dev/) - 浏览和搜索插件 | Skills 市场：[skillsmp.com](https://skillsmp.com/zh) - 2300+ Skills 搜索目录 | Agent Skills：[agentskills.io](https://agentskills.io/home) - Agent Skills 规范和市场 | 官方插件库：[GitHub - anthropics/claude-code/plugins](https://github.com/anthropics/claude-code/tree/main/plugins) | 官方 Skills 库：[GitHub - anthropics/skills](https://github.com/anthropics/skills) | **Skills**：模型调用 —— AI 根据描述自动决定

## 02-ai-tuning-guide\04-project-config.md
- Summary line: title: "2.4 项目规则配置"
- Headings: 2.4 项目规则配置 🟡 | 什么时候需要配置 | 更简单的方法：让 AI 自己写 | 配置文件的本质 | CLAUDE.md 模板 | 项目：[项目名称] | 技术栈 | 规范
- Key bullets: Next.js 16 + TypeScript | 使用 shadcn/ui 组件库 | 用 pnpm 包管理器 | 5人团队，需要统一规范 | 都是写给 AI 看的项目说明书 | 核心内容：技术栈 + 编码规范 + 禁止行为

## 02-ai-tuning-guide\05-debugging-tips.md
- Summary line: title: "2.5 高效调试心法"
- Headings: 2.5 高效调试心法 🟢 | 前置知识 | 调试沟通公式：完整日志 + 操作步骤 + 预期结果 | 终极大招：让 AI 自己 Build | 实战案例 | 案例 1：类型错误 | 案例 2：运行时错误 | 案例 3：构建错误
- Key bullets: AI 直接看到真实错误，不用你转述 | 小问题（版本冲突、缺失依赖）AI 自己解决 | 你看结果就行 | ✅ 先 `git commit`，AI 改坏能回滚 | ✅ 第一次可能慢，耐心等待 | ⚠️ AI 陷入死循环（来回改同一处）→ 及时打断

## 02-ai-tuning-guide\index.md
- Summary line: title: "第二章：AI 使用说明书"
- Headings: 第二章：AI 使用说明书 | 序言 | AI 编程的经济学 | VibeCoding 工作流 | 版本控制 Git | 配置技巧 | 调试心法 | 拓展知识

## 03-prd-doc-driven\00-prd-template.md
- Summary line: title: "3.0 PRD 模板"
- Headings: 3.0 PRD 模板 | [产品/功能名称] - 产品需求文档 (PRD) | 0. 文档信息 | 0.1 文档状态 | 0.2 更新记录 | 0.3 相关文档 | 0.4 名词解释 | 一、 需求背景与目标 (对应"需求初稿"核心内容)
- Key bullets: **当前版本**: `[例如：5.1稿]` | **当前阶段**: `[例如：需求评审 / UI设计中 / 开发中 / 已上线]` | **创建人**: `[你的名字]` | **创建日期**: `[YYYY-MM-DD]` | **最后更新**: `[YYYY-MM-DD]` | **核心干系人**: `[产品、研发、设计、测试、业务等关键角色的负责人姓名]`

## 03-prd-doc-driven\01-product-validation.md
- Summary line: title: "3.1 想法验证实战"
- Headings: 3.1 想法验证实战 🔴 | 本节适用说明 | 前置知识 | 为什么要验证想法 | 灵魂三问 | 问题一：用户是谁？ | 问题二：痛点在哪？ | 需求的三个层次
- Key bullets: "你觉得这是个好主意吗？" | "你会买这个产品吗？" | "你会愿意付多少钱？" | "如果有一个功能能做 X，你会用吗？" | "你不觉得这个问题很烦人吗？" | "你也遇到过这个问题吧？"

## 03-prd-doc-driven\02-discuss-with-ai.md
- Summary line: title: "3.2 与 AI 确认需求"
- Headings: 3.2 与 AI 确认需求 🔴 | AI 的理解盲区 | 确认理解的提示词模板 | 为什么这样有效 | 让 AI 主动追问 | 为什么让 AI 主动追问 | 如何启动 | 追问示例
- Key bullets: **AI 能发现你忽略的问题** —— 基于训练数据中的常见模式，AI 知道哪些地方容易有歧义 | **对话更自然** —— 像讨论一样，一问一答，逐步深入 | **减少你的认知负担** —— 不需要一次性想清楚所有细节 | 结果：跳过了关键确认，理解偏差被隐藏 | 正确做法：即使是基础问题，也明确回答，消除歧义 | 结果：AI 按默认方式处理，不符合你的特定需求

## 03-prd-doc-driven\03-prd-template-guide.md
- Summary line: title: "3.3 PRD 编写实战"
- Headings: 3.3 PRD 编写实战 🔴 | PRD 的价值 | PRD 的五部分结构 | 第0部分：文档信息 | 文档状态 | 语义化版本号 | 更新记录 | 第一部分：需求背景与目标
- Key bullets: **当前版本**：如 "内部评审版-修订一" — 记录当前阶段和修订次数 | **当前阶段**：需求评审 / UI设计中 / 开发中 / 已上线 | **核心干系人**：产品、研发、设计、测试等负责人 | **主版本号**：重大变更，不兼容之前的版本（如产品方向调整） | **次版本号**：新增功能，向下兼容（如新增一个功能模块） | **修订号**：问题修复或小改动（如修正错别字、补充细节）

## 03-prd-doc-driven\04-coding-agents.md
- Summary line: title: "3.4 从 PRD 到代码"
- Headings: 3.4 从 PRD 到代码 🟡 | AI 的"阅读"方式 | 人与 AI 的阅读差异 | AI 的执行流程 | PRD 细节如何影响代码 | 提取关键信息阶段 | 构建数据模型阶段 | 设计业务逻辑阶段
- Key bullets: 用户是谁 → 影响 UI 设计风格 | 核心功能 → 决定代码结构 | 业务流程 → 决定逻辑顺序 | Out-of-Scope → 防止"自由发挥" | 登录功能 | 云同步

## 03-prd-doc-driven\index.md
- Summary line: title: "第三章：产品思维与文档驱动"
- Headings: 第三章：产品思维与文档驱动 | 序言：为什么先写文档再写代码？ | 产品验证三步法 | 与 AI 确认需求 | PRD 编写实战 | 从 PRD 到代码 | 需求管理与工具 | 学习目标
- Key bullets: ✅ 掌握跟 AI 讨论需求时必须确认的细节清单 | ✅ 用产品验证三步法判断想法是否值得做 | ✅ 使用标准模板写出 AI 友好的 PRD | ✅ 理解哪些细节会影响 AI 生成的代码质量 | ✅ 训练问题定义能力，提高 AI 协作效率

## 04-dev-fundamentals\00-build-basics.md
- Summary line: title: "4.0 代码运行的三种状态"
- Headings: 4.0 代码运行的三种状态 🟢 | 三种状态 | Dev（开发模式） | Build（构建模式） | Production（生产模式） | 热重载 | package.json | Scripts（脚本）
- Key bullets: 保存代码后浏览器自动更新 | 支持热重载，表单内容不会丢失 | 包含详细的报错信息，方便调试 | 运行速度较慢 | 压缩代码体积 | 优化运行速度

## 04-dev-fundamentals\01-tech-stack-decision.md
- Summary line: title: "4.1 技术栈决策框架"
- Headings: 4.1 技术栈决策框架 🟡 | 技术栈决策的核心原则 | 编程语言的世界 | 我们的选择：为什么是 TypeScript + Next.js？ | AI 时代的技术栈选择 | 决策框架：三个问题 | 常见技术方案速查 | 前端框架
- Key bullets: 展示内容为主 → 静态站点或纯前端框架 | 需要用户登录 → 需要后端能力 | 需要持久化存储 → 需要数据库 | 需要 AI 能力 → 需要集成 AI API | 个人使用或小规模 → 可以选择简单方案 | 预期中等规模 → 需要考虑扩展性

## 04-dev-fundamentals\02-prd-and-tech-docs.md
- Summary line: title: "4.2 从 PRD 到技术文档"
- Headings: 4.2 从 PRD 到技术文档 🟢 | 引言 | PRD 与技术文档的分工 | PRD（产品需求文档） | 技术文档 | 两者的关系 | 技术文档的五大组成部分 | 1. 数据模型
- Key bullets: 系统有哪些数据，它们之间什么关系 | 前后端通过哪些接口通信 | 系统由哪些组件构成，业务流程怎么走 | 依赖哪些外部服务 | 它是 AI 生成数据库代码的基础上下文 | 它是前后端对接的数据契约

## 04-dev-fundamentals\03-programming-basics.md
- Summary line: title: "4.3 如何读懂 AI 生成的代码"
- Headings: 4.3 如何读懂 AI 生成的代码 🟢 | 引言 | 代码的四个基本构件 | 变量：数据的容器 | 函数：可复用的指令块 | 条件判断：分叉的路口 | 循环：重复的力量 | 图灵完备：四种构件的威力
- Key bullets: 输入：单价、数量 | 处理：单价 × 数量 | 输出：总价 | 数据存在哪里？→ **变量** | 操作被封装在哪里？→ **函数** | 什么情况下执行什么？→ **条件**

## 04-dev-fundamentals\04-api-and-http.md
- Summary line: title: "4.4 API 与 HTTP 基础"
- Headings: 4.4 API 与 HTTP 基础 🟢 | 引言 | 什么是 API | HTTP 通信流程 | HTTP 请求的组成 | 请求方法（Method） | URL（路径） | Headers（头信息）
- Key bullets: **函数**：定义在代码里，接收参数，返回结果 | **API**：定义在服务器上，接收 HTTP 请求（参数），返回 HTTP 响应（结果） | 函数调用：`calculatePrice(100, 2)` → 返回 `200` | API 调用：`GET /api/price?unit=100&quantity=2` → 返回 `{ "total": 200 }` | 前端是顾客 | 后端是厨房

## 04-dev-fundamentals\05-frontend-backend-separation.md
- Summary line: title: "4.5 前后端分离概念"
- Headings: 4.5 前后端分离概念 🟢 | 前端和后端的职责 | 前端（Frontend） | 后端（Backend） | 传统模式 vs 前后端分离 | 传统模式（服务端渲染） | 前后端分离模式 | 前后端分离的优势
- Key bullets: 服务器生成完整 HTML | 浏览器只负责展示 | 页面切换需要重新加载 | 前后端代码耦合在一起 | 前端负责页面渲染 | 后端只提供数据 API

## 04-dev-fundamentals\06-config-formats.md
- Summary line: title: "4.6 配置文件格式"
- Headings: 4.6 配置文件格式 🟢 | 什么是结构化数据格式 | JSON 格式 | 语法规则 | 数据类型 | JSON 的优势 | YAML 格式 | 语法规则
- Key bullets: 格式统一，没有歧义 | 易于程序解析和生成 | 跨语言、跨平台通用 | AI 能够准确理解 | 使用大括号 `{}` 表示对象 | 使用方括号 `[]` 表示数组

## 04-dev-fundamentals\07-api-integration.md
- Summary line: title: "4.7 API 集成实战"
- Headings: 4.7 API 集成实战 🟢 | API 集成概述 | 为什么 API 如此重要？ | 异步通信与数据格式 | 常见的 API 能力 | API 集成六步法 | 第一步：获取凭证 | 第二步：选择技术路线
- Key bullets: **不要**提交到 Git 仓库 | **不要**写在前端代码中（用户能看到） | **不要**发布在公开场合 | 程序运行时自动读取配置 | `.env` 文件不提交到 Git | 不同环境使用不同密钥

## 04-dev-fundamentals\08-readme-structure.md
- Summary line: title: "4.8 项目说明书结构"
- Headings: 4.8 项目说明书结构 🟢 | README.md 的价值 | README 的核心结构 | 1. 项目简介 | 极简待办清单 | 2. 快速开始 | 快速开始 | 安装依赖
- Key bullets: **任务管理**：添加、完成、删除待办任务 | **数据持久化**：刷新页面数据不丢失 | **极简界面**：专注核心体验，无干扰 | **框架**：Next.js 14 (App Router) | **语言**：TypeScript | **样式**：Tailwind CSS

## 04-dev-fundamentals\09-finding-libraries.md
- Summary line: title: "4.9 别再重复造轮子"
- Headings: 4.9 别再重复造轮子 | 一个真实项目遇到的问题和解决方案 | 问题 1：用户数据频繁变化，每次都重新 fetch 太慢 | 问题 2：表单验证逻辑散落在各处，改一个地方要改好几个文件 | 问题 3：用户认证要处理 session、cookie、密码加密……太复杂了 | 问题 4：数据库查询写 SQL 太繁琐，还容易出错 | 问题 5：用户上传的内容可能包含恶意脚本 | 问题 6：表单状态管理太复杂，每个字段都要写一堆代码
- Key bullets: 成熟库经过几百万次生产验证，AI 写的代码只经过你的测试 | 成熟库有完整的边界情况处理，AI 写的代码可能漏掉 90% 的边界情况 | 成熟库有持续维护和安全更新，AI 写的代码出了问题只能你自己修 | 你以为写完就完了？依赖更新、安全漏洞、新需求……都得你自己处理 | 成熟库有社区帮你解决这些问题，你的代码只有你自己 | 找到最合适的库

## 04-dev-fundamentals\index.md
- Summary line: title: "第四章：你必须知道的开发基础"
- Headings: 第四章：你必须知道的开发基础 | 序言 | 代码运行的三种状态 | 技术栈选择 | 编程的基本构件 | PRD 与技术文档的关系 | API 与 HTTP 基础 | 前后端分离概念
- Key bullets: 目标用户是谁？ | 核心功能有哪些？ | 用户如何交互？ | 边缘场景怎么处理？ | 用什么技术栈？（Next.js + PostgreSQL） | 数据库表结构怎么设计？（用户表、文章表、评论表）

## 05-ui-ux\01-ai-design-tools.md
- Summary line: title: "5.1 AI 设计工具"
- Headings: 5.1 AI 设计工具 | Google AI Studio —— AI 应用开发平台（强烈推荐） | Google Stitch —— AI 原型设计 | v0.app —— AI UI 代码生成器 | Figma —— 设计界的标准工具 | Lovable —— 全栈应用生成器 | 工具选择指南与推荐工作流 | 让 AI 帮你选工具
- Key bullets: 快速搭建 AI 驱动的应用原型 | 需要集成 Gemini 模型能力的项目 | 想要一站式从设计到部署 | 免费用户 | 从零开始设计页面布局 | 需要设计稿而不是代码（设计稿是一张可以看但不能跑的图，代码是可以直接运行的程序——Stitch 给你的是前者）

## 05-ui-ux\02-component-libraries.md
- Summary line: title: "5.2 组件库"
- Headings: 5.2 组件库 | shadcn/ui（推荐） | 其他主流组件库 | 组件库选择决策树 | 让 AI 帮你用组件库
- Key bullets: 代码在你项目里，AI 可以直接读取和修改 | 组件质量高，无障碍支持好——比如视障用户用屏幕朗读器也能正常操作按钮和表单 | 生态丰富，有大量扩展组件和模板

## 05-ui-ux\03-animation-libraries.md
- Summary line: title: "5.3 动画与交互库"
- Headings: 5.3 动画与交互库 | Motion（原 Framer Motion）—— React 动画首选 | GSAP —— 专业级动画引擎 | GSAP —— 专业级动画引擎 | Three.js —— 3D 效果的终极武器 | 轻量级动画方案 | 动画库选择决策树 | 动画的度
- Key bullets: 性能最强，复杂动画不掉帧 | 支持时间线（Timeline），可以编排多个动画的先后顺序——类似剪辑视频时的时间轴，你可以安排哪个动画先播、哪个后播、中间隔多久 | 插件丰富：ScrollTrigger（滚动触发）、Draggable（拖拽）、MorphSVG（SVG 变形） | 不限于 React，任何框架都能用 | 营销落地页的炫酷滚动动画 | 复杂的 SVG 动画和路径动画

## 05-ui-ux\04-ui-inspiration.md
- Summary line: title: "5.4 UI 风格与灵感"
- Headings: 5.4 UI 风格与灵感 | 灵感网站 | Awwwards —— 顶级网页设计奖 | Dribbble —— 设计师社区 | Mobbin —— 真实应用截图库 | Land-book —— 落地页灵感 | 风格关键词 | 如何向 AI 描述风格

## 05-ui-ux\05-advanced-effects.md
- Summary line: title: "5.5 让页面更高级的效果"
- Headings: 5.5 让页面更高级的效果 | 过渡效果 | 按钮特效 | 视觉特效 | 滚动效果 | 交互效果 | 使用原则

## 05-ui-ux\06-component-skills.md
- Summary line: title: "5.6 让 AI 记住你的设计规范"
- Headings: 5.6 让 AI 记住你的设计规范 | 小明的新烦恼 | 设计规范的困境 | 从"反复提醒"到"一劳永逸" | 你已经有了设计规范 | 第一步：让 AI 扫描生成设计规范 | 第二步：创建项目 Skill | AI 会帮你创建这样的结构
- Key bullets: **颜色**：主色是哪个蓝？成功用哪个绿？错误用哪个红？ | **间距**：组件之间隔多远？内边距多大？ | **圆角**：按钮用多大的圆角？卡片呢？ | **阴影**：卡片要不要阴影？多深？ | **字体**：标题多大？正文多大？用粗体还是常规？ | `tailwind.config.js` - 提取颜色、间距、圆角、阴影等设计 tokens

## 05-ui-ux\index.md
- Summary line: title: "第五章：界面(UI)与交互(UX)"
- Headings: 第五章：界面(UI)与交互(UX) | 序言 | CSS 与组件 | Tailwind 与 shadcn/ui | UX 体验 | 提示词技巧 | 响应式设计 | 性能意识
- Key bullets: **CSS (层叠样式表)**：如果说 HTML 是网页的**骨架**（素颜），那 CSS 就是**化妆品**。它决定了按钮是圆角还是直角，背景是渐变还是纯色。 | **组件 (Component)**：现代网页不是画出来的，而是**搭**出来的。导航栏、按钮、输入框，这些都是预先做好的**乐高积木**。你不需要每次都手写一个"带圆角、有阴影、鼠标悬停变色的红色按钮"，而是直接拿来一个叫做 `<Button />` 的积木就能用。 | **布局 (Layout)**：元素怎么摆放在页面上，由布局方式决定。你刷朋友圈时内容从上到下一条条排列，这就是 Flexbox 在做的事；打开小红书，照片像棋盘一样填满屏幕，这是 Grid 的效果。你只需要告诉 AI"把这三个按钮横向排列"或"把页面分成左右两列"，具体属性让它处理。 | **按钮的反馈状态**： | *错误示范*：点击"支付"按钮后，页面毫无反应，用户以为没点上，于是疯狂点击，导致扣款两次。 | *AI 指令*："请给这个提交按钮加上 **Loading 状态**。当用户点击后，按钮应变灰并显示转圈动画，且不可再次点击，直到请求结束。"

## 06-data-persistence-database\00-get-your-database.md
- Summary line: title: "6.0 领取你的数据库"
- Headings: 6.0 领取你的数据库 | 为什么用云端数据库 | 方案一：Neon（推荐） | 注册步骤 | Neon 免费套餐包含什么 | 方案二：Supabase | 注册步骤 | Supabase 免费套餐包含什么
- Key bullets: 本地安装配置繁琐，容易踩坑 | 部署到线上时还要迁移数据 | 云端数据库**免费套餐**对个人项目完全够用 | **Project Name**：随便起，比如 `my-first-app` | **Region**：选择离你最近的区域。国内用户推荐选 **Singapore（新加坡）**，延迟最低 | **Database Name**：默认 `neondb` 即可

## 06-data-persistence-database\01-storage-evolution.md
- Summary line: title: "6.1 数据存储演进"
- Headings: 6.1 数据存储演进 | 小明的豆瓣电影梦 | 第一阶段：CSV / Excel — 能用，但很快就不够 | 第二阶段：JSON 文件 — 程序员的本能选择 | 第三阶段：数据库 — 专业的事交给专业的工具 | 演进规律：什么时候该升级？
- Key bullets: `movies` 表：存电影基本信息（片名、年份、评分、简介） | `directors` 表：存导演信息（姓名、国籍） | `actors` 表：存演员信息（姓名、国籍） | `movie_actors` 表：记录哪个演员演了哪部电影（中间表，解决多对多关系） | `tags` 表：存标签（科幻、动作、文艺……） | `movie_tags` 表：记录哪部电影有哪些标签（又一个中间表）

## 06-data-persistence-database\02-database-basics.md
- Summary line: title: "6.2 数据库基础概念"
- Headings: 6.2 数据库基础概念 | 小红的外卖创业 | 表：比 Excel 强大一百倍的"工作表" | 主键：每行数据的身份证 | 外键：表与表之间的线索 | 关系类型详解 | 一对多（1:N）— 最常见 | 多对多（M:N）— 需要中间表
- Key bullets: 学生用户：谁在用这个平台？手机号、昵称、宿舍地址 | 校园商家：食堂档口、奶茶店、水果店，每家有名字、评分、营业时间 | 菜品菜单：每家店卖什么、多少钱、有没有图片 | 订单记录：谁在哪家店买了什么、花了多少钱、现在什么状态 | 订单明细：一个订单里具体点了哪些菜、各几份 | **唯一**：不能有两行的主键值相同（就像不能有两个人的身份证号一样）

## 06-data-persistence-database\03-database-operations.md
- Summary line: title: "6.3 如何操作数据库"
- Headings: 6.3 如何操作数据库 | 小红的第一个需求 | ORM：用代码操作数据库的翻译官 | CRUD：数据库操作的四个基本动作 | 审查 AI 生成的 CRUD 代码 | 常见性能陷阱 | N+1 查询：最隐蔽的性能杀手 | 分页越翻越慢：OFFSET 的陷阱
- Key bullets: 语法贴近 SQL，学过 SQL 概念就能看懂 | TypeScript 类型安全，AI 生成的代码更容易审查 | 同时支持 PostgreSQL 和 SQLite，方便切换 | 社区活跃，文档完善 | 用户注册 → **Create** 一条 users 记录 | 浏览菜单 → **Read** dishes 表，按商家筛选

## 06-data-persistence-database\05-database-design.md
- Summary line: title: "6.4 数据库设计与优化"
- Headings: 6.4 数据库设计与优化 | 老王的微信读书笔记翻车记 | AI 交叉论证法（炼蛊） | 索引：数据库的目录 | 什么是索引，解决什么问题 | 哪些列需要索引 | 不同类型的索引 | 行级安全（RLS）：防止数据泄露的最后一道墙
- Key bullets: **是否真的启用了？** 光定义策略不够，还要 `ALTER TABLE ... ENABLE ROW LEVEL SECURITY`，否则策略不生效——就像手机设了密码但没开启锁屏，密码形同虚设。这是最常见的遗漏——策略定义和启用是两个独立步骤，缺一不可 | **策略覆盖全了吗？** SELECT、INSERT、UPDATE、DELETE 各需要单独的策略，漏一个就是安全漏洞。比如你定义了"用户只能查看自己的订单"（SELECT 策略），但忘了定义 UPDATE 策略，那用户就能修改别人的订单 | **会不会拖慢查询？** RLS 策略里用到的列（比如 `user_id`）必须有索引，否则每次查询都要全表扫描来做权限过滤。这又回到了索引的重要性——没有索引的 RLS 策略，安全是安全了，但慢得让人受不了 | **自动备份**：Neon 和 Supabase 都提供自动备份，确认已开启。不要依赖手动备份——你一定会忘的 | **多地备份**：重要数据不要只存一个地方。云服务商的数据中心也可能出故障（虽然概率很低），鸡蛋不要放在一个篮子里 | **恢复演练**：这是最容易被忽视的一点。定期测试从备份恢复，确认备份真的能用。太多人做了备份但从没测试过，等到需要恢复时才发现备份文件损坏、格式不兼容、或者恢复流程根本跑不通。备份的价值不在于"有没有做"，而在于"能不能恢复"

## 06-data-persistence-database\index.md
- Summary line: title: "第六章：数据持久化与数据库"
- Headings: 第六章：数据持久化与数据库 | 序言 | JSON 文件存储 | 关系型数据库 | Drizzle Schema | 数据库操作 | 数据完整性与校验 | 数据备份
- Key bullets: **Table (表)**：就是一个 Excel Sheet（工作表），比如 `Users` 表。 | **Row (行)**：表里的一行，代表一条具体的数据（比如用户张三）。 | **Column (列)**：表里的表头，定义了数据有哪些属性（姓名、年龄、邮箱）。 | **Primary Key (主键)**：每一行数据的唯一身份证号（通常是 `id`），绝对不能重复。 | **Foreign Key (外键)**：用来关联其他表的线索。比如在 `Orders`（订单）表中记录一个 `user_id`，就能顺藤摸瓜找到这个订单属于哪个用户。 | **`pgTable`**：定义 PostgreSQL 表结构

## 07-backend-api\00-crud-example.md
- Summary line: title: "7.0 跑通你的第一个全栈应用"
- Headings: 7.0 跑通你的第一个全栈应用 | 全栈数据流：一张图看懂 | 告诉 AI 创建项目 | 检查 AI 的作业 | 1. 数据库表结构（schema.ts） | 2. API 路由（route.ts） | 3. 前端页面（page.tsx） | 动手跑起来
- Key bullets: 页面加载时，调用 `GET /api/todos` 获取列表 | 用户输入标题点"添加"，调用 `POST /api/todos` | 用户点勾选框，调用 `PATCH /api/todos/[id]` 更新状态 | 用户点删除，调用 `DELETE /api/todos/[id]` | **前端**：用户界面、事件处理、API 调用 | **后端**：API 路由、请求处理、数据校验

## 07-backend-api\01-api-growing-pains.md
- Summary line: title: "7.1 一个接口不够用了"
- Headings: 7.1 一个接口不够用了 | 小明的电影详情页难题 | 先问自己：这个页面需要 API 吗？ | 嵌套 vs 扁平：两种数据组织方式 | 嵌套结构 | 扁平结构 | 怎么选？ | 500 条记录一次全返回，页面卡死了
- Key bullets: **前端需要动态交互时**——比如用户点了"收藏"按钮，前端需要告诉后端"我要收藏这部电影"。这种用户触发的写操作，需要通过某种方式调用后端逻辑 | **外部消费者**——比如老王想用小明的数据做小程序，他需要一个可以调用的 HTTP 接口 | 只想排序不想筛选？`GET /api/movies?sort=rating&order=desc` | 只想筛选不想排序？`GET /api/movies?tag=动画` | 想同时按多个标签筛选？`GET /api/movies?tag=动画&tag=日本` | 什么都不传？`GET /api/movies` 返回默认排序的全部数据（带分页）

## 07-backend-api\02-when-things-go-wrong.md
- Summary line: title: "7.2 当接口出了问题"
- Headings: 7.2 当接口出了问题 | 小明的应用上线了 | 数据库里多了一条空标题的电影 | Zod——AI 会用的校验库 | 校验应该严格到什么程度？ | 同一部电影被添加了 10 次 | 前端拦一道，后端兜一道 | 怎么让创建接口变幂等？
- Key bullets: **它做什么**：定义"数据应该长什么样"的规则（比如标题必须是 1-100 个字符的字符串，年份必须是 1888-2030 之间的整数），然后自动校验传入的数据 | **校验失败怎么办**：返回具体的错误信息给前端，告诉它哪个字段不对、为什么不对 | **为什么用它而不是手写 if-else**：Zod 把校验规则和 TypeScript 类型合二为一——定义了校验规则，TypeScript 类型自动推导出来，不用写两遍。而且 Zod 的错误信息格式统一，前端处理起来方便 | **电梯按钮**是幂等的。你按一次"3 楼"，电梯去 3 楼。你着急多按了 5 次，电梯还是只去 3 楼，不会去 5 个 3 楼。 | **开灯开关**是幂等的。灯已经开着，你再按一次开关，灯还是开着，不会变成"双倍亮"。 | **投币机**不是幂等的。你投一次币出一瓶水，投两次出两瓶。

## 07-backend-api\03-api-as-product.md
- Summary line: title: "7.3 让接口更好用"
- Headings: 7.3 让接口更好用 | 小明的新烦恼 | 自己都记不清有哪些接口了 | 让 AI 生成接口文档 | 改了一个字段名，前端好几个页面崩了 | 向后兼容：改接口的安全姿势 | 一次删 50 条 vs 调 50 次删除接口 | 批量操作接口
- Key bullets: `/api/v1/movies` —— 旧版接口，保持不变 | `/api/v2/movies` —— 新版接口，新的数据结构 | **限制文件大小**：不限制的话，有人上传一个 1GB 的文件就能把你的服务器内存撑爆 | **限制文件类型**：只允许你需要的格式（图片就只允许 jpg/png/webp），不要接受 .exe、.sh 等可执行文件 | **不要用用户提供的文件名**：用户可能上传一个叫 `../../../etc/passwd` 的文件来搞路径穿越攻击。后端应该自己生成文件名（比如用 UUID） | **有文档**——使用者知道怎么用，不需要翻代码或问人

## 07-backend-api\index.md
- Summary line: title: "第七章：后端API开发"
- Headings: 第七章：后端API开发 | 序言 | 什么是后端 | 什么是 API Route | 路由：URL 决定你看到什么 | 从页面路由到 API 路由 | 导出处理函数 | 跟 AI 聊后端之前，先认识几个关键词
- Key bullets: 访问 `movie.douban.com/` → 看到豆瓣电影首页 | 访问 `movie.douban.com/subject/37311135/` → 看到《飞驰人生 3》的详情页 | 访问 `movie.douban.com/subject/37311135/comments?status=P` → 看到这部电影的短评（`?status=P` 表示"看过的人的评论"） | 访问 `movie.douban.com/chart` → 看到排行榜 | `app/api/movies/route.ts` → `yourdomain.com/api/movies`（返回电影列表的 JSON 数据） | `app/api/movies/[id]/route.ts` → `yourdomain.com/api/movies/123`（返回某部电影的 JSON 数据）

## 08-auth-security\00-user-system-example.md
- Summary line: title: "8.0 用户系统快速示例"
- Headings: 8.0 用户系统快速示例 | 认证 vs 授权 | 为什么选 Better Auth | 告诉 AI 搭建用户系统 | 理解认证流程 | 注册流程 | 登录流程 | 受保护路由
- Key bullets: **认证（Authentication）**：你是谁？——验证身份（登录） | **授权（Authorization）**：你能做什么？——检查权限（管理员 vs 普通用户） | **密码安全**：存储的是哈希值，不是明文 | **会话管理**：通过 Cookie + Session 维持登录状态 | **路由保护**：服务端检查，未登录无法访问 | **数据自主**：所有用户数据存在你自己的数据库里

## 08-auth-security\01-env-and-secrets.md
- Summary line: title: "8.1 密钥管理与环境变量"
- Headings: 8.1 密钥管理与环境变量 | 小明的教训 | 从硬编码到 .env | 敏感配置 | 依赖包（太大，队友自己装） | 构建产物（编译生成的临时文件） | 系统垃圾 | .env.example——给未来的自己留个模板
- Key bullets: 密钥放 `.env`，代码里用 `process.env.XXX` 读取 | `.gitignore` 屏蔽 `.env`，防止提交到 Git | `.env.example` 列出变量名不填值，提交到 Git 当模板 | 不加 `NEXT_PUBLIC_` 前缀的变量只在服务端可用——这是安全机制，不是 bug | 改了 `.env` 要重启服务 | 部署时在平台的环境变量页面配置，不要上传 `.env` 文件

## 08-auth-security\02-auth-methods.md
- Summary line: title: "8.2 认证方式与方案选择"
- Headings: 8.2 认证方式与方案选择 | 登录之后，服务器怎么记住我？ | 不只是密码：现代认证方式 | 为什么不自己写认证 | 认证库怎么选 | 开发中的另一种认证：公私钥
- Key bullets: Session 存服务端可控性强，Token 不存服务端扩展性好——认证库会帮你选择 | OAuth 让用户用已有账号登录，Passkeys 是无密码的未来趋势 | 不要自己写认证逻辑，用成熟的认证库 | 新项目首选 Better Auth，加载 `better-auth-best-practices` Skill 提升 AI 输出质量

## 08-auth-security\03-route-protection.md
- Summary line: title: "8.3 路由保护与权限控制"
- Headings: 8.3 路由保护与权限控制 | 前端隐藏不是安全 | Middleware——Next.js 的守门员 | 页面保护和接口保护缺一不可 | CORS——浏览器的跨域安全机制 | 角色权限控制
- Key bullets: 前端隐藏入口不是安全措施，真正的保护在服务端 | Middleware 是 Next.js 的统一拦截层，用 `matcher` 指定保护范围 | 页面保护和接口保护缺一不可 | CORS 是浏览器的安全机制，同项目内通常不需要配置 | 角色权限从简单的 admin/user 开始，需要时再扩展

## 08-auth-security\04-security-checklist.md
- Summary line: title: "8.4 安全检查与问题排查"
- Headings: 8.4 安全检查与问题排查 | 安全清单 | 问题排查手册
- Key bullets: 安全清单按阶段执行：开发前配好 `.gitignore`，开发中检查边界和校验，上线前审计依赖，上线后定期轮换 | 90% 的 `.env` 问题重启就能解决 | `.gitignore` 只对未追踪的文件生效，已追踪的要先 `git rm --cached` | 密钥泄露后必须重置密钥 + 清洗 Git 历史，光删文件不够

## 08-auth-security\05-advanced-security.md
- Summary line: title: "8.5 进阶安全防护"
- Headings: 8.5 进阶安全防护 | 基础安全之上 | SQL 注入——让数据库执行恶意代码 | XSS——在别人的页面上执行恶意脚本 | CSRF——冒充你发请求 | AI 应用的特有安全问题 | 依赖安全与数据加密
- Key bullets: SQL 注入：用 ORM 自动防护，不要手写 SQL 拼接用户输入 | XSS：React 自动转义，不要用 `dangerouslySetInnerHTML` | CSRF：Next.js + Better Auth 内置防护 | AI 应用：注意提示注入、输出过滤、速率限制 | 依赖安全：定期 `pnpm audit`，敏感数据加密存储 | 选对技术栈（Next.js + Drizzle + React），80% 的常见攻击已经被挡住了

## 08-auth-security\index.md
- Summary line: title: "第八章：安全与用户认证"
- Headings: 第八章：安全与用户认证 | 序言 | 本章小节
- Key bullets: **密钥怎么管**——环境变量、`.gitignore`、云端配置，让密钥永远不出现在代码里 | **用户怎么认**——注册登录背后的原理，以及为什么要用成熟的认证库而不是自己写 | **路由怎么守**——Middleware、CORS、权限控制，确保每个请求都经过检查 | **出了问题怎么查**——从"配置没生效"到"密钥已泄露"的排查手册 | **更深的威胁怎么防**——SQL 注入、XSS、CSRF，以及 AI 应用特有的安全问题

## 09-testing-automation\01-testing-strategy.md
- Summary line: title: "9.1 为什么需要测试"
- Headings: 9.1 为什么需要测试 | "安全网"到底是什么 | 测试金字塔——不是所有测试都一样 | 什么时候该引入自动化测试 | AI 辅助测试的正确姿势
- Key bullets: 回归测试的核心问题：以前能用的功能，改了别的代码之后还能用吗？ | 测试金字塔：单元测试多而快（测函数）、集成测试适量（测接口）、E2E 测试少而精（测流程） | 自动化测试是投资：5+ 页面、核心流程 3+ 步、遇到过"修 A 坏 B"——这些信号说明该上了 | AI 帮你写测试代码，你负责判断"测的对不对"——业务特有的边界情况需要你补充

## 09-testing-automation\02-api-and-e2e-testing.md
- Summary line: title: "9.2 API 测试与 E2E 测试"
- Headings: 9.2 API 测试与 E2E 测试 | 为什么先测 API | 一个接口该测什么 | 让 AI 帮你生成 API 测试 | 从接口到界面：E2E 测试 | Flaky 测试——测试界的"玄学" | 测试失败了怎么看日志 | 什么时候用 E2E，什么时候用 API 测试
- Key bullets: 先测 API：快、稳定、容易定位问题。一个接口至少测四类场景：正常、校验、权限、边界 | E2E 测试测"用户体验"：只覆盖最关键的流程，不要过度使用 | Flaky 测试三大原因：异步时序、数据竞争、环境差异。用显式等待、数据隔离、合理超时来解决 | 测试失败三步定位：错误信息 → 截图 → 网络请求

## 09-testing-automation\03-automation-workflow.md
- Summary line: title: "9.3 自动化工作流"
- Headings: 9.3 自动化工作流 | 有了测试，但忘了跑 | Git Hooks——提交前自动检查 | 安装 Husky | 初始化 | .husky/pre-commit 文件内容 | GitHub Actions——推送后自动验证 | .github/workflows/test.yml
- Key bullets: uses: actions/checkout@v4 | name: Setup Node.js | name: Setup pnpm | name: Install dependencies | name: Run tests | Git Hooks（Husky）：提交前自动跑测试，测试失败阻止提交——第一道防线

## 09-testing-automation\index.md
- Summary line: title: "第九章：功能测试与自动化"
- Headings: 第九章：功能测试与自动化 | 序言 | 本章小节

## 10-localhost-public-access\01-network-layers.md
- Summary line: title: "10.1 从 Localhost 到互联网"
- Headings: 10.1 从 Localhost 到互联网 | Localhost：每个设备的"自言自语" | 局域网：同一个 WiFi 下的设备互通 | 找到你的局域网 IP | 手机访问电脑上的项目 | Next.js | Vite | 防火墙：为什么手机还是打不开？

## 10-localhost-public-access\02-tunneling.md
- Summary line: title: "10.2 内网穿透：临时让朋友看看"
- Headings: 10.2 内网穿透：临时让朋友看看 | 为什么需要内网穿透 | 隧道是怎么工作的 | Cloudflare Tunnel（推荐） | 安装 | 启动隧道 | 让 AI 一步到位 | 常见问题
- Key bullets: [ ] 项目的登录功能是否已启用（第八章的成果） | [ ] `.env` 文件是否包含敏感信息（API 密钥、数据库密码）——这些不会通过隧道泄露，但确认一下总没错 | [ ] 隧道只指向 Web 应用端口，没有暴露其他服务 | [ ] 演示完成后会立即关闭隧道 | 每次重启 cloudflared，链接就变了，得重新发给朋友 | 他的电脑必须一直开着，合上笔记本盖子朋友就断了

## 10-localhost-public-access\index.md
- Summary line: title: "第十章：Localhost 与公网访问"
- Headings: 第十章：Localhost 与公网访问 | 序言 | 本章小节

## 11-git-collaboration\01-why-git.md
- Summary line: title: "11.1 为什么需要 Git"
- Headings: 11.1 为什么需要 Git | "最终版"困境 | 你可能已经在用 Git 了 | commit：给代码存档 | 三区模型：你的修改在哪里 | 回滚：无限的 Ctrl+Z | 查看历史：AI 到底改了什么 | 提交信息：给未来的自己留线索

## 11-git-collaboration\02-remote-and-collaboration.md
- Summary line: title: "11.2 推上云端，开始协作"
- Headings: 11.2 推上云端，开始协作 | 所有鸡蛋在一个篮子里 | 平台选择与注册 | SSH 认证：配一次，永久免密 | 第一次推送 | push 和 pull：保持同步 | clone：朋友第一次获取代码 | 冲突：两个人改了同一行

## 11-git-collaboration\03-branch-and-workflow.md
- Summary line: title: "11.3 分支、PR 与团队工作流"
- Headings: 11.3 分支、PR 与团队工作流 | "复制一份再改"的本能 | 分支：Git 版的"复制文件夹" | 完整的分支工作流 | Pull Request：帮我看看再合并 | GitHub PR 页面导览 | 个人项目也需要分支吗 | 跨平台协作：Windows 遇上 Mac

## 11-git-collaboration\index.md
- Summary line: title: "第十一章：Git 版本控制与协作开发"
- Headings: 第十一章：Git 版本控制与协作开发 | 序言 | 本章小节

## 12-serverless-deploy-cicd\01-deploy-edgeone.md
- Summary line: title: "12.1 部署到 EdgeOne Pages"
- Headings: 12.1 部署到 EdgeOne Pages | 部署前的三个确认 | 注册并连接 GitHub | 配置构建设置 | 配置环境变量 | 选择加速区域 | （可选）如果构建失败，怎么排查 | 部署成功：拿到链接

## 12-serverless-deploy-cicd\02-deploy-vercel-platforms.md
- Summary line: title: "12.2 部署到类 Vercel 平台"
- Headings: 12.2 部署到类 Vercel 平台 | 平台速览 | Vercel：Next.js 的"亲爹" | 部署流程 | 安装 Vercel CLI | 登录（会打开浏览器授权） | 部署（首次会询问项目配置） | 部署到生产环境

## 12-serverless-deploy-cicd\03-cicd-automation.md
- Summary line: title: "12.3 CI/CD 与自动化"
- Headings: 12.3 CI/CD 与自动化 | 你已经在用 CI/CD 了 | 平台内置的 CI/CD | 什么时候需要自定义流水线 | GitHub Actions：自动化菜谱 | 分支与部署环境 | 个人项目需要 GitHub Actions 吗 | 实战案例：本教程的 CI/CD 配置
- Key bullets: **CI（持续集成）**：每次推送代码，自动运行检查和构建，确保代码没问题 | **CD（持续部署）**：检查通过后，自动发布到线上 | **推送到 `main` 分支** → 自动部署到生产环境（用户访问的正式版本） | **创建 Pull Request** → 自动构建并生成预览链接 | 自动运行测试，确保新代码没有破坏已有功能 | 自动检查代码风格，保持代码整洁

## 12-serverless-deploy-cicd\04-operations-cost.md
- Summary line: title: "12.4 运维基础与成本优化"
- Headings: 12.4 运维基础与成本优化 | 上线之后谁来看着它 | 看懂你的数据 | 日志：出了问题去哪里看 | 平台已经帮你做的优化 | 你可以关注的优化 | 成本：免费额度够用吗 | 分阶段决策
- Key bullets: **EdgeOne**：控制台 → 项目 → 数据分析 | **Vercel**：Dashboard → 项目 → Analytics | **Cloudflare**：Dashboard → Workers & Pages → 分析 | **EdgeOne**：控制台 → 项目 → 部署日志 + 运行日志 | **Vercel**：Dashboard → 项目 → Logs，可以按时间和关键词筛选 | **Cloudflare**：Dashboard → Workers & Pages → 实时日志

## 12-serverless-deploy-cicd\index.md
- Summary line: title: "第十二章：无服务器部署与 CI/CD 自动化"
- Headings: 第十二章：无服务器部署与 CI/CD 自动化 | 序言 | 零成本部署 | CI/CD 自动化 | 部署配置 | 部署踩坑 | 灰度发布——降低风险 | 平台自动优化
- Key bullets: **腾讯云 EdgeOne Pages**：国内可访问，基于腾讯全球边缘网络，连接 GitHub 后自动部署，对 Next.js 支持很好 | **阿里云 ESA 函数和 Pages**：阿里云的一站式全栈开发平台，深度集成 Git 工作流，国内访问速度快 | **Vercel**：Next.js 的官方部署平台，体验极佳，但国内访问较慢，适合海外用户或有自定义域名的项目 | **Cloudflare Pages**：全球 CDN 加速，免费额度慷慨，支持边缘函数 | **GitHub Pages**：最简单的静态网站托管，适合纯前端项目 | **框架预设**：选择你用的框架（如 Next.js），平台会自动填充推荐配置

## 13-domain-dns\01-domain-setup.md
- Summary line: title: "13.1 域名购买与 DNS 配置"
- Headings: 13.1 域名购买与 DNS 配置 | 域名购买 | 选择注册商 | 域名怎么选 | 域名结构 | 购买流程 | DNS 解析配置 | DNS 是什么
- Key bullets: **类型**：CNAME | **名称**：`@`（代表根域名）或 `www`，或者别的自定义前缀。 | **目标**：平台给你的 CNAME 值 | **TTL**：自动 | **Vercel / Cloudflare Pages**：绑定自定义域名后自动申请，全自动，不需要你操心 | **EdgeOne Pages**：需要你在域名管理页面手动点击"申请免费证书"。证书申请成功后会自动续期，不用担心过期

## 13-domain-dns\02-compliance-access.md
- Summary line: title: "13.2 备案与访问问题排查"
- Headings: 13.2 备案与访问问题排查 | 备案是什么 | 备案 vs 免备案 | 免备案方案（推荐新手） | 备案流程（简介） | 常见访问问题排查 | HTTP 状态码：快递查询式理解 | 排查决策树
- Key bullets: 个人备案的网站名称不能包含"公司""商城"等企业性质词汇 | 备案期间域名不能访问（部分省份要求） | 备案号需要每年年审，否则可能被注销 | 更换接入商（比如从阿里云换到腾讯云）需要做"接入备案" | **2xx = 已签收**。一切正常，包裹到手了。`200 OK` 是最常见的"签收成功"。 | **3xx = 转寄中**。包裹搬家了，快递员帮你送到新地址。`301` 是永久搬家，`302` 是临时转寄。

## 13-domain-dns\index.md
- Summary line: title: "第十三章：域名、DNS 与网络接入"
- Headings: 第十三章：域名、DNS 与网络接入 | 序言 | 本章学习路径

## 14-vps-ops-deploy\01-vps-selection.md
- Summary line: title: "14.1 VPS 选购指南"
- Headings: 14.1 VPS 选购指南 | 主流云厂商 | 配置选择建议 | 机房位置选择 | 操作系统选择 | 购买注意事项
- Key bullets: [阿里云 ECS / 轻量应用服务器](https://www.aliyun.com/) — 国内生态最全，文档丰富 | [腾讯云轻量应用服务器](https://cloud.tencent.com/) — 新用户优惠力度大，控制台对新手友好 | [AWS](https://aws.amazon.com/) — 全球节点多，大厂稳定 | [DigitalOcean](https://www.digitalocean.com/) — 界面简洁，开发者体验好 | [搬瓦工（BandwagonHost）](https://bandwagonhost.com/) — 香港/日本节点对国内访问友好 | [RackNerd](https://www.racknerd.com/) — 性价比高，黑五/新年常有特价

## 14-vps-ops-deploy\02-vps-setup.md
- Summary line: title: "14.2 VPS 初始化与安全配置"
- Headings: 14.2 VPS 初始化与安全配置 | 第一步：连接服务器 | 方法一：云厂商控制台免密登录（推荐新手） | 方法二：本地终端 SSH 登录 | 方法三：FinalShell（日常管理更方便） | 第二步：系统更新 | 第三步：安装常用工具 | 第四步：安装 1Panel 面板
- Key bullets: **面板端口**：建议改成一个不常见的端口（如 `29876`），不要用默认的 | **面板用户名**：不要用 `admin` | **面板密码**：设置一个强密码 | 开启防火墙，并添加规则，放行刚刚在云厂商那里开放的端口（80、443、面板端口等） | **公钥**（`id_rsa.pub`）可以公开，上传到服务器 | **私钥**（`id_rsa`）必须妥善保存，不可泄露。私钥就是你的"钥匙"，丢了就等于把家门钥匙丢了

## 14-vps-ops-deploy\03-1-docker-apps.md
- Summary line: title: "14.3.1 应用商店与 Docker 基础"
- Headings: 14.3.1 应用商店与 Docker 基础 | Docker 到底是什么？ | 1Panel 应用商店 | DBMS vs Database：装完数据库后的第一步 | 容器管理 | 数据持久化：Volume 挂载 | 查看所有 Volume | 查看某个 Volume 的详细信息
- Key bullets: **镜像（Image）**：就像应用商店里的安装包。"PostgreSQL 18 镜像"就是一个打包好的数据库安装包，里面包含了所有需要的文件和配置。 | **容器（Container）**：就像你手机上运行的 App。不同的是，在这里同一个安装包可以装多次，每个都是独立运行的，互不影响。 | **仓库（Registry）**：就像应用商店。Docker Hub 是最大的"服务器应用商店"，里面有几十万个现成的应用安装包。 | **DBMS**（数据库管理系统）：如 PostgreSQL、MySQL，是管理数据的软件 | **Database**（数据库）：DBMS 里创建的具体数据库，如 `myapp_db` | **「应用商店 - 已安装」**：管理通过应用商店安装的应用，支持重建、重启、启动、停止、卸载、查看参数等操作。点击「参数」按钮可以查看和修改应用的配置参数。

## 14-vps-ops-deploy\03-2-deploy-nextjs.md
- Summary line: title: "14.3.2 部署 Next.js 应用"
- Headings: 14.3.2 部署 Next.js 应用 | 前置准备 | 第一步：上传代码到服务器 | SSH 登录后，克隆代码到指定目录 | 进入项目目录，先把依赖装好 | 第二步：理解端口映射 | 前置准备：内存不足的解决方案 | 创建 2GB Swap 文件
- Key bullets: 服务器上安装了 1Panel（参考 [14.2](./02-vps-setup.md)） | 通过应用商店安装了 **OpenResty** 和 **PostgreSQL**（如果项目需要数据库） | 项目代码已推送到 GitHub | **Git Clone**：SSH 登录服务器，`git clone` 你的仓库到指定目录 | **1Panel 文件管理**：通过面板的「文件」功能上传压缩包并解压 | 1GB 内存：强烈建议创建 2GB Swap

## 14-vps-ops-deploy\03-3-deploy-static.md
- Summary line: title: "14.3.3 部署静态网站"
- Headings: 14.3.3 部署静态网站 | 什么是静态网站？ | 第一步：本地构建 | VitePress | Next.js (静态导出) | Vite / React / Vue | 第二步：在 1Panel 创建网站 | 第三步：上传构建产物
- Key bullets: 用 VitePress / Astro / Hugo 生成的文档站、博客 | React / Vue 的 SPA（单页应用）构建产物 | 纯 HTML 的落地页、作品集 | 如果只有一个 `index.html` + 一堆 JS/CSS 文件 → **是 SPA** | 如果有多个 HTML 文件（如 `about.html`、`contact.html`）→ **不是 SPA** | React（用 Vite 或 Create React App 创建）

## 14-vps-ops-deploy\03-4-deploy-fullstack.md
- Summary line: title: "14.3.4 部署前后端分离应用"
- Headings: 14.3.4 部署前后端分离应用 | 前后端分离架构 | 通用部署流程 | 第一步：部署数据库 | 第二步：部署后端服务 | 第三步：构建并部署前端 | 在本地电脑上 | 设置环境变量（指向服务器的后端 API）
- Key bullets: **14.3.2**：适合 Next.js 这种"前后端一体"的全栈框架，一个容器搞定 | **本节（14.3.4）**：适合"前后端分离"的架构，前端和后端是独立的项目，需要分别部署 | **OpenResty**：对外的唯一入口，负责分发请求 | **后端服务**：处理业务逻辑和数据库操作（Node.js / Python / Java / Go 等） | **数据库**：存储数据 | 用户的所有请求都先到前台（OpenResty）

## 14-vps-ops-deploy\04-domain-ssl.md
- Summary line: title: "14.4 配置域名与证书"
- Headings: 14.4 配置域名与证书 | 第一步：DNS A 记录——让域名找到服务器 | 在你的电脑上执行 | 或 | 或（更详细） | 第二步：创建网站——让服务器认这个域名 | 第三步：申请 Let's Encrypt 免费 SSL 证书 | 第四步：HTTPS 强制跳转
- Key bullets: `@` 表示根域名（如 `yourdomain.com`） | `www` 表示 `www.yourdomain.com` | **访问HTTP自动跳转到HTTPS**：推荐选项，所有 HTTP 请求自动重定向到 HTTPS | **HTTP可直接访问**：HTTP 和 HTTPS 同时可用，不强制跳转 | **禁止 HTTP**：只允许 HTTPS 访问，HTTP 请求直接拒绝

## 14-vps-ops-deploy\05-cool-apps.md
- Summary line: title: "14.5 其他好玩的应用"
- Headings: 14.5 其他好玩的应用 | Umami：网站统计 | n8n：自动化工作流 | Bitwarden：密码管理器 | Alist：文件管理器 | 应用推荐速查
- Key bullets: 不追踪用户隐私，符合 GDPR | 界面简洁，数据一目了然 | 自己托管，数据完全在你手里 | 新用户注册时自动发欢迎邮件 | GitHub 有新 Issue 时自动通知到微信/飞书 | 定时抓取数据并生成报告

## 14-vps-ops-deploy\index.md
- Summary line: title: "第十四章：云服务器运维与项目部署"
- Headings: 第十四章：云服务器运维与项目部署 | 序言 | SSH | 锁好门窗 | 1Panel 面板 | Docker 容器 | 安全组 | 自建数据库
- Key bullets: **DBMS（PostgreSQL）**：就像 Excel 软件本身。 | **Database**：就像 Excel 里打开的一个个 `.xlsx` 文件。安装一次 PostgreSQL，可以创建无数个独立的数据库供不同项目使用。 | **容器找邻居**：用容器名（如 `postgresql`） | **主机找容器**：用 `localhost` 或 `127.0.0.1` | **外部访问**：用服务器公网 IP + 映射端口 | **监控**：通过日志和统计工具了解系统状态

## 15-seo-analytics\01-opengraph-sharing.md
- Summary line: title: "15.1 Open Graph 与社交分享"
- Headings: 15.1 Open Graph 与社交分享 | 小明的蓝色链接 | 什么是 Open Graph | 核心 OG 标签 | 小明配好了 OG | OG 图片：分享卡片的视觉核心 | 各平台推荐尺寸 | 设计原则
- Key bullets: **设计工具**：Canva 有大量现成的社交媒体图片模板，选一个改改文字就行。Figma 适合有设计基础的人。这是最快的方式。 | **AI 生成**：用 AI 图片生成工具，描述你想要的风格和内容，生成一张封面图。效果取决于你的 prompt 质量。 | **动态生成**：Next.js 支持用 `next/og` 的 `ImageResponse` 在服务端动态生成 OG 图片。这对博客类网站特别有用——每篇文章自动生成一张带标题的封面图，不需要手动为每篇文章设计图片。如果你的网站有很多页面，动态生成是最省心的方案。 | `summary`：小图卡片，图片在左边，文字在右边 | `summary_large_image`：大图卡片，图片占据整个卡片上方（推荐）

## 15-seo-analytics\02-seo-guide.md
- Summary line: title: "15.2 SEO 全攻略"
- Headings: 15.2 SEO 全攻略 | 小明搜不到自己的网站 | SEO 是什么，为什么值得花时间 | 搜索引擎怎么工作 | 基础配置三件套：让爬虫找到你 | Metadata（元数据） | Sitemap（站点地图） | Robots.txt
- Key bullets: **`title`**：页面标题，会直接显示在搜索结果里。这是用户决定是否点击的第一要素。 | **`description`**：页面描述，显示在搜索结果标题下方的灰色文字。好的描述能显著提升点击率。 | **Experience（经验）**：作者是否有实际经验？写部署教程的人，自己部署过吗？ | **Expertise（专业）**：内容是否展示了专业知识？是泛泛而谈还是有深度？ | **Authoritativeness（权威）**：网站和作者在这个领域是否有权威性？ | **Trustworthiness（可信）**：内容是否可信？有没有引用来源？

## 15-seo-analytics\03-umami.md
- Summary line: title: "15.3 Umami 数据统计"
- Headings: 15.3 Umami 数据统计 | 小明看到了数据 | 为什么需要网站统计 | 为什么选 Umami | 快速上手 | 首次登录 | 添加网站并集成追踪代码 | 老师傅教小明看指标
- Key bullets: 如果 80% 的用户用手机访问，但你的移动端体验很差——你知道该优先优化什么了 | 如果某个页面的跳出率特别高——说明用户来了就走，页面内容可能没有满足他们的期望 | 如果大部分流量来自社交分享而不是搜索引擎——说明 SEO 还需要时间，但 OG 配置（15.1）确实有效 | 用户名：`admin` | 密码：`umami` | **PV 高但 UV 低**：说明少数用户在反复访问，你有一批忠实用户

## 15-seo-analytics\04-legal.md
- Summary line: title: "15.4 法律合规"
- Headings: 15.4 法律合规 | "个人项目也需要？" | 为什么需要法律合规 | 隐私政策：告诉用户你拿了什么数据 | 什么时候需要隐私政策 | 隐私政策该包含什么 | GDPR：如果你有欧盟用户 | 怎么生成隐私政策
- Key bullets: **账户信息**：邮箱地址、用户名、密码（哈希后的） | **行为数据**：页面浏览记录、点击行为——是的，Umami 统计也算 | **个人身份信息**：姓名、电话、地址 | **位置信息**：IP 地址、GPS 定位 | **Cookie 和类似技术**：如果你用了 Cookie（Umami 不用，但很多其他工具用） | 明确的数据处理法律依据（你凭什么收集这些数据？）

## 15-seo-analytics\index.md
- Summary line: title: "第十五章：SEO、分享与数据统计"
- Headings: 第十五章：SEO、分享与数据统计 | 序言 | 1. SEO 搜索引擎优化 | 2. Open Graph 分享 | 3. Umami 统计 | 4. 合规 | 本章小节
- Key bullets: **Metadata（元数据）**：在 Next.js 的 `layout.tsx` 里配置 `metadata` 对象，填上清晰的 `title` 和 `description`，告诉爬虫你是谁。 | **Sitemap（站点地图）**：给爬虫的一张地图，告诉它网站里有哪些页面，哪些是最新的。 | **Robots.txt**：给爬虫看的规则文件，告诉它哪些能爬，哪些不能爬。

## 16-user-feedback-iteration\01-facing-real-users.md
- Summary line: title: "16.1 面对真实用户"
- Headings: 16.1 面对真实用户 | 上线第一天 | 现实与期待的落差 | 早期用户的反应模式 | 心理调适 | 从开发者到运营者 | 早期该关注什么 | 建立支持系统

## 16-user-feedback-iteration\02-feedback-prioritization.md
- Summary line: title: "16.2 反馈分类与优先级"
- Headings: 16.2 反馈分类与优先级 | 20 条反馈，先做哪个？ | 第一步：分类 | 第二步：判断紧急程度 | RICE：更精确的排序 | 反馈管理流程 | 学会说"不" | 常见问题
- Key bullets: "登录的时候偶尔会崩溃" | "能不能加个深色模式？" | "导出功能什么时候有？" | "首页颜色太丑了" | "手机上按钮太小，点不到" | "加载好慢啊"

## 16-user-feedback-iteration\03-understanding-users.md
- Summary line: title: "16.3 理解用户"
- Headings: 16.3 理解用户 | "不好用"到底是哪里不好用？ | The Mom Test：怎么问才能得到真话 | 好问题 vs 坏问题 | 小明的第二次访谈 | 访谈实操 | 怎么问 | 怎么做一次完整的访谈

## 16-user-feedback-iteration\04-iteration-and-growth.md
- Summary line: title: "16.4 迭代与成长"
- Headings: 16.4 迭代与成长 | 一次性全改完的教训 | 更新节奏的平衡 | 三层更新策略 | 灰度发布 | 变更管理 | 迭代节奏 | 新功能 vs Bug 修复

## 16-user-feedback-iteration\index.md
- Summary line: title: "第十六章：用户反馈与产品迭代"
- Headings: 第十六章：用户反馈与产品迭代 | 序言 | 为什么需要反馈 | 收集反馈的渠道 | 反馈的分类与优先级 | 用户访谈 | 数据驱动决策 | 持续迭代
- Key bullets: 16.1 [面对真实用户](./01-facing-real-users.md)——上线后的心理调适与反馈渠道建设 | 16.2 [反馈分类与优先级](./02-feedback-prioritization.md)——用 RICE 框架给反馈排优先级 | 16.3 [理解用户](./03-understanding-users.md)——用户访谈与数据驱动的结合 | 16.4 [迭代与成长](./04-iteration-and-growth.md)——建立可持续的迭代节奏与产品思维

## 99-next-level\index.md
- Summary line: title: "NEXT LEVEL"
- Headings: Next Level
- Key bullets: **从依赖到掌控**——你不再是被动的需求方，而是懂得如何指挥 AI，把它从聊天玩具变成了真正的生产力工具。 | **从黑盒到透明**——你懂得了从环境搭建到服务器部署，每一层是如何运转的。虽然不需要精通，但你不再害怕任何"技术黑盒"。 | **从恐慌到从容**——面对报错，你不再手忙脚乱。你知道如何查看日志、如何分析问题、如何向 AI 描述问题。 | **不更新的浏览器**； | **怎么填都不对的环境变量**； | 第**发给朋友打不开的链接**；

## happy-coder.md
- Summary line: title: "随时随地 AI 编程"
- Headings: 随时随地 AI 编程：Happy Coder 工具链 | 一、为什么它是 AI 时代的开发神器 | 1、Happy Coder 解决了什么痛点 | 2、Happy Coder 工作原理解析 | 3、Happy Coder 的 运行逻辑 | 4、安全与隐私 | 5、安全性 与 FAQ | 二、使用 Happy Coder 前的准备工作
- Key bullets: Happy Coder 官网：[https://happy.engineering](https://happy.engineering) | Happy App：[Web UI + 移动客户端](https://github.com/slopus/happy/tree/main/packages/happy-app) | Happy CLI：[Claude Code 和 Codex 的命令行界面](https://github.com/slopus/happy-cli) | Happy Server：[加密同步的后端服务器](https://github.com/slopus/happy-server) | 真正的“生产力”：移动端良好 | 极致的隐私安全（信号级加密）

## index.md
- Summary line: title: "进阶篇"
- Headings: 进阶篇：从想法到产品的100小时 | 鸿沟正在消失 | 谁是老师 | 另一条路 | 一个人就是一支队伍 | 100 小时走完全程 | 停下来想，不如跑起来做 | 你需要做什么

## web-ide.md
- Summary line: title: "5 分钟搭建云端开发环境"
- Headings: 开局一个浏览器，代码环境全搞定 | 预装开发环境 | 基础概念 | 1. 注册与登录 | 实名认证（必须） | 2. 创建组织 | 3. 创建开发环境 | Fork 仓库
- Key bullets: 配置开发环境要花好几天？ | 电脑配置不够，Docker 跑不动？ | GitHub 下载慢，clone 一个仓库要半小时？ | **AI 编程**: Claude Code、OpenAI Codex、Gemini Code Assist | **运行时**: Node.js 24.x、Python 3.11+、Docker | **开发工具**: Git、GitHub CLI、VS Code (53 个扩展)
