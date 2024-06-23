# Binance-LBank_spot_future_arbitrage
这是一个利用Binance现货API和LBank合约API进行期现套利的Python策略。

# Arbitrage Strategy for Binance and LBank

这是一个利用Binance现货API和LBank合约API进行期现套利的Python策略。

This is a Python strategy for arbitrage between Binance Spot API and LBank Futures API.

## 需求

- Python 3.7+
- `requests`库

## 安装

1. 克隆该存储库：

    ```bash
    git clone https://github.com/yourusername/arbitrage-strategy.git
    cd arbitrage-strategy
    ```

2. 安装依赖：

    ```bash
    pip install requests
    ```

## 使用

1. 在`arbitrage_strategy.py`文件中填入您的API密钥：

    ```python
    binance_api_key = 'YOUR_BINANCE_API_KEY'
    binance_secret_key = 'YOUR_BINANCE_SECRET_KEY'
    lbank_api_key = 'YOUR_LBANK_API_KEY'
    lbank_secret_key = 'YOUR_LBANK_SECRET_KEY'
    ```

2. 运行策略：

    ```bash
    python arbitrage_strategy.py
    ```

## 策略说明

该策略会持续监控Binance现货市场和LBank合约市场的价格差异，并在检测到套利机会时执行交易。

## 贡献

欢迎提交问题和请求合并！Telegram: @ChildrenQ

## 许可证

MIT 许可证
