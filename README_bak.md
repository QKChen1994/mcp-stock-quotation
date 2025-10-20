# 创建并激活虚拟环境
````
uv venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
````
# 安装依赖包
````
# 安装单个包
uv pip install requests

# 安装指定版本
uv pip install requests==2.31.0

# 从 requirements.txt 安装
uv pip install -r requirements.txt

# 从pyproject.toml安装
uv pip install -e . -i https://mirrors.aliyun.com/pypi/simple/
````

# 运行
````
mcp dev server.py
````