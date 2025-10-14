# # 将这行
# from fastmcp import FastMCP

# 改为
from mcp.server.fastmcp.server import FastMCP
import math
import requests
import json
from datetime import datetime

import akshare as ak

mcp = FastMCP("CalculatorService")

@mcp.tool()
def get_stock_quotation_eastmoney(identifier: str) -> dict:
    """使用东方财富API获取股票实时行情数据

    Args:
        identifier: 股票代码（如：000001, 600036）

    Returns:
        dict: 包含股票行情信息的字典
    """
    try:
        # 构造东方财富API请求URL
        # 深圳股票以sz开头，上海股票以sh开头
        if identifier.startswith(('6', '5')):  # 上海股票
            symbol = f"sh{identifier}"
        else:  # 深圳股票
            symbol = f"sz{identifier}"

        # 东方财富实时行情API
        url = f"http://push2.eastmoney.com/api/qt/stock/get"
        params = {
            'secid': f"{1 if 'sh' in symbol else 0}.{identifier}",
            'fields': 'f57,f58,f107,f43,f44,f45,f46,f47,f48,f49,f50,f51,f52,f53,f54,f55,f56,f59,f60,f61,f62,f63,f64,f65,f66,f67,f68,f69,f70,f71,f72,f73,f74,f75,f76,f77,f78,f79,f80,f81,f82,f83,f84,f85,f86,f87,f88,f89,f90,f91,f92,f127,f168,f169,f170,f171,f172,f173,f174,f175,f176,f177,f178,f179,f180,f181,f182,f183,f184,f185,f186,f187,f188,f189,f190,f191,f192,f193,f194,f195,f196,f197,f198,f199,f200,f201,f202,f203,f204,f205,f206,f207,f208,f209,f210,f211,f212,f213,f214,f215,f216,f217,f218,f219,f220,f221,f222,f223,f224,f225,f226,f227,f228,f229,f230,f231,f232,f233,f234,f235,f236,f237,f238,f239,f240,f241,f242,f243,f244,f245,f246,f247,f248,f249,f250,f251,f252,f253,f254,f255,f256,f257,f258,f259,f260,f261,f262,f263,f264,f265,f266,f267,f268,f269,f270,f271,f272,f273,f274,f275,f276,f277,f278,f279,f280,f281,f282,f283,f284,f285,f286,f287,f288,f289,f290,f291,f292,f293,f294,f295,f296,f297,f298,f299,f300'
        }
        
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if data.get('data'):
            stock_data = data['data']
            # 提取关键行情数据
            current_price = stock_data.get('f43', 0) / 100  # 当前价格（分转元）
            prev_close = stock_data.get('f60', 0) / 100     # 昨收价（分转元）
            open_price = stock_data.get('f46', 0) / 100     # 开盘价（分转元）
            high_price = stock_data.get('f44', 0) / 100     # 最高价（分转元）
            low_price = stock_data.get('f45', 0) / 100      # 最低价（分转元）
            volume = stock_data.get('f47', 0)               # 成交量
            amount = stock_data.get('f48', 0)               # 成交额

            # 计算涨跌幅度
            change = current_price - prev_close
            change_percent = (change / prev_close * 100) if prev_close > 0 else 0

            return {
                "name": stock_data.get('f58', identifier),    # 股票名称
                "code": identifier,
                "open": open_price,
                "current_price": current_price,
                "change_percent": f"{round(change_percent, 2)}%",
                "prev_close": prev_close,
                "high": high_price,
                "low": low_price,
                "change": round(change, 2),
                "volume": volume,
                "amount": amount,
                "time": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "source": "eastmoney"
            }
        else:
            return {
                "error": "未获取到股票数据",
                "input": identifier,
                "message": "东方财富API返回空数据",
                "source": "eastmoney"
            }

    except Exception as e:
        return {
            "error": "获取股票数据时出错",
            "message": str(e),
            "input": identifier,
            "source": "eastmoney"
        }


if __name__ == "__main__":
    mcp.run(transport="stdio")