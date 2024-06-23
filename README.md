# CTA Strategy for LBank Futures

这是一个利用LBank合约API进行CTA（趋势跟踪策略）的Python实现。欢迎交流: @ChildrenQ

This is a Python implementation of a CTA (trend-following strategy) using LBank Futures API.

## 需求

- Python 3.7+
- `requests`库

## 安装

1. 克隆该存储库：

    ```bash
    git clone https://github.com/yourusername/cta-strategy.git
    cd cta-strategy
    ```

2. 安装依赖：

    ```bash
    pip install requests
    ```

## 使用

1. 在`cta_strategy.py`文件中填入您的API密钥：

    ```python
    lbank_api_key = 'YOUR_LBANK_API_KEY'
    lbank_secret_key = 'YOUR_LBANK_SECRET_KEY'
    ```

2. 运行策略：

    ```bash
    python cta_strategy.py
    ```

## 策略说明

该策略会持续监控LBank合约市场的数据，并基于均线（短期和长期）生成买卖信号。当短期均线上穿长期均线时买入，当短期均线下穿长期均线时卖出。

This strategy continuously monitors LBank futures market data and generates buy/sell signals based on moving averages (short-term and long-term). It buys when the short-term moving average crosses above the long-term moving average, and sells when the short-term moving average crosses below the long-term moving average.

## 贡献

欢迎提交问题和请求合并！

Feel free to submit issues and pull requests!

## 许可证

MIT 许可证

MIT License
