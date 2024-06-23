import requests
import time
import hmac
import hashlib

# Binance API密钥和端点
# Binance API Keys and Endpoints
binance_api_key = 'YOUR_BINANCE_API_KEY'
binance_secret_key = 'YOUR_BINANCE_SECRET_KEY'
binance_base_url = 'https://api.binance.com'

# LBank API密钥和端点
# LBank API Keys and Endpoints
lbank_api_key = 'YOUR_LBANK_API_KEY'
lbank_secret_key = 'YOUR_LBANK_SECRET_KEY'
lbank_base_url = 'https://api.lbkex.com'

# 获取Binance现货市场价格
# Get spot market prices from Binance
def get_binance_spot_price(symbol):
    endpoint = f'/api/v3/ticker/price?symbol={symbol}'
    url = binance_base_url + endpoint
    response = requests.get(url)
    return float(response.json()['price'])

# 获取LBank合约市场价格
# Get futures market prices from LBank
def get_lbank_futures_price(symbol):
    endpoint = f'/v2/futures/price?symbol={symbol}'
    url = lbank_base_url + endpoint
    response = requests.get(url)
    return float(response.json()['data']['price'])

# 签名请求（LBank需要）
# Sign request (needed for LBank)
def sign_request(params, secret_key):
    query_string = '&'.join([f"{key}={value}" for key, value in sorted(params.items())])
    signature = hmac.new(secret_key.encode(), query_string.encode(), hashlib.sha256).hexdigest()
    return signature

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

# 发送Binance订单
# Place an order on Binance
def send_binance_order(symbol, side, quantity):
    endpoint = '/api/v3/order'
    url = binance_base_url + endpoint
    timestamp = int(time.time() * 1000)
    params = {
        'symbol': symbol,
        'side': side,  # BUY or SELL
        'type': 'MARKET',
        'quantity': quantity,
        'timestamp': timestamp,
        'recvWindow': 5000
    }
    query_string = '&'.join([f"{key}={value}" for key, value in params.items()])
    signature = hmac.new(binance_secret_key.encode(), query_string.encode(), hashlib.sha256).hexdigest()
    headers = {
        'X-MBX-APIKEY': binance_api_key
    }
    params['signature'] = signature
    response = requests.post(url, headers=headers, params=params)
    return response.json()

# 主策略逻辑
# Main strategy logic
def arbitrage_strategy():
    symbol = 'BTCUSDT'
    while True:
        # 获取现货和合约市场价格
        # Fetch spot and futures market prices
        spot_price = get_binance_spot_price(symbol)
        futures_price = get_lbank_futures_price(symbol)

        # 计算套利机会
        # Calculate arbitrage opportunity
        threshold = 0.01  # Arbitrage threshold (1%)
        if futures_price > spot_price * (1 + threshold):
            # 在Binance买入，在LBank卖出
            # Buy on Binance, sell on LBank
            quantity = 0.001  # Trade quantity
            send_binance_order(symbol, 'BUY', quantity)
            send_lbank_order(symbol, quantity, '2')
        elif spot_price > futures_price * (1 + threshold):
            # 在LBank买入，在Binance卖出
            # Buy on LBank, sell on Binance
            quantity = 0.001  # Trade quantity
            send_lbank_order(symbol, quantity, '1')
            send_binance_order(symbol, 'SELL', quantity)

        # 等待一段时间再检查
        # Wait for a while before checking again
        time.sleep(60)

# 启动策略
# Start the strategy
if __name__ == "__main__":
    arbitrage_strategy()
