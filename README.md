# PyTPS Web

Thomson Parabola Spectrometer (TPS) 数据分析 Web 应用。

## 快速开始

### Docker 部署（推荐）

```bash
# 构建并启动
docker-compose up --build

# 访问
http://localhost:8080
```

### 开发模式

```bash
# 后端
cd backend
pip install -r requirements.txt
cd ..
uvicorn backend.main:app --reload --port 8000

# 前端（另一个终端）
cd frontend
npm install
npm run dev
```

访问 `http://localhost:5173`（Vite 开发服务器，自动代理到后端）。

## 技术栈

- **后端**: FastAPI + uvicorn + WebSocket
- **前端**: Vue 3 + Element Plus + ECharts
- **计算**: numpy + scipy + scikit-image + matplotlib
- **部署**: Docker (multi-stage build)

## 项目结构

```
pytps-web/
├── backend/
│   ├── main.py          # FastAPI 入口
│   ├── config.py        # 环境变量
│   ├── core/            # 计算模块（从 PyTPS 迁移）
│   ├── api/             # REST 端点
│   ├── services/        # 业务逻辑
│   ├── ws/              # WebSocket 处理
│   ├── models/          # Pydantic 模型
│   └── data/            # 默认配置文件
├── frontend/
│   └── src/
│       ├── api/         # REST + WebSocket 客户端
│       ├── stores/      # Pinia 状态管理
│       ├── components/  # Vue 组件
│       └── views/       # 页面
├── Dockerfile
├── docker-compose.yml
└── data/                # Docker volume 挂载点
```

## 环境变量

| 变量 | 默认值 | 说明 |
|------|--------|------|
| PYTPS_IMAGE_DIR | /data/images | 图像文件目录 |
| PYTPS_OUTPUT_DIR | /data/output | 导出文件目录 |
| PYTPS_WORKERS | 4 | 工作线程数 |
| PYTPS_SESSION_MAX_AGE | 3600 | 会话超时(秒) |
