import requests
import time
import hmac
import hashlib

# LBank API密钥和端点
# LBank API Keys and Endpoints
lbank_api_key = 'YOUR_LBANK_API_KEY'
lbank_secret_key = 'YOUR_LBANK_SECRET_KEY'
lbank_base_url = 'https://api.lbkex.com'

# 签名请求（LBank需要）
# Sign request (needed for LBank)
def sign_request(params, secret_key):
    query_string = '&'.join([f"{key}={value}" for key, value in sorted(params.items())])
    signature = hmac.new(secret_key.encode(), query_string.encode(), hashlib.sha256).hexdigest()
    return signature

# 获取市场数据
# Fetch market data
def get_market_data(symbol):
    endpoint = f'/v2/futures/market_depth?symbol={symbol}&size=1'
    url = lbank_base_url + endpoint
    response = requests.get(url)
    return response.json()['data']

# 计算均线
# Calculate moving average
def calculate_moving_average(prices, window):
    return sum(prices[-window:]) / window

# 发送LBank订单
# Place an order on LBank
def send_lbank_order(symbol, volume, direction):
    endpoint = '/v2/ownfutures/order'
    url = lbank_base_url + endpoint
    params = {
        'api_key': lbank_api_key,
        'symbol': symbol,
        'volume': volume,
        'direction': direction,  # 1 for buy, 2 for sell
    }
    params['sign'] = sign_request(params, lbank_secret_key)
    response = requests.post(url, data=params)
    return response.json()

# 主策略逻辑
# Main strategy logic
def cta_strategy():
    symbol = 'BTCUSDT'
    prices = []

    while True:
        market_data = get_market_data(symbol)
        current_price = float(market_data['bids'][0][0])
        prices.append(current_price)
        
        if len(prices) > 50:
            short_ma = calculate_moving_average(prices, 10)
            long_ma = calculate_moving_average(prices, 50)
            
            # 生成交易信号
            # Generate trading signals
            if short_ma > long_ma:
                send_lbank_order(symbol, 0.001, '1')  # 买入 Buy
            elif short_ma < long_ma:
                send_lbank_order(symbol, 0.001, '2')  # 卖出 Sell

        # 等待一段时间再检查
        # Wait for a while before checking again
        time.sleep(60)

# 启动策略
# Start the strategy
if __name__ == "__main__":
    cta_strategy()
