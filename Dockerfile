# 使用官方 Python 运行时作为基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 安装 uv 工具
RUN pip install uv

# 复制项目文件
COPY . .

# 安装依赖
RUN uv pip install --system -r requirements.txt || \
    uv pip install --system -e . -i https://mirrors.aliyun.com/pypi/simple/

# 暴露服务端口（根据实际应用调整）
EXPOSE 8000

# 启动命令
CMD ["mcp", "dev", "server.py"]
