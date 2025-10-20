## 服务介绍

这是一个基于 Python 的项目，使用 `uv` 工具进行虚拟环境管理和依赖安装。项目包含了创建虚拟环境、安装依赖包以及运行服务的基本操作指南。

## 服务描述

该项目是一个 Python 应用程序，主要展示了如何使用 `uv` 工具来管理项目的虚拟环境和依赖项。它提供了详细的步骤说明，包括创建和激活虚拟环境、安装不同形式的依赖包（单个包、指定版本、从 requirements.txt 或 pyproject.toml 安装），以及如何运行服务（通过 `mcp dev server.py` 命令）。此外，还配置了使用阿里云镜像源来加速包的安装过程。

## 类型

Python Web 应用

## 服务配置
```bash
{
    "mcpServers": {
        "default-server": {
            "command": "uv",
            "args": [
                "run",
                "--with",
                "mcp",
                "mcp",
                "run",
                "server.py"
            ],
            "env": {
            }
        }
    }
}
 ```
## 服务配置

```bash
# 创建并激活虚拟环境
uv venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# 安装依赖包
# 安装单个包
uv pip install requests

# 安装指定版本
uv pip install requests==2.31.0

# 从 requirements.txt 安装
uv pip install -r requirements.txt

# 从pyproject.toml安装
uv pip install -e . -i https://mirrors.aliyun.com/pypi/simple/

# 运行
mcp dev server.py
```
