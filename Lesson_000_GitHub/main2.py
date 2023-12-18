import requests
import time

def get_gas_price():
    url = 'https://api.etherscan.io/api?module=gastracker&action=gasoracle'
    response = requests.get(url)
    data = response.json()
    gas_price = int(data['result']['FastGasPrice'])
    return gas_price

def get_eth_price():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    eth_price = data['ethereum']['usd']
    return eth_price


while True:
    gas_price = get_gas_price()
    eth_price = get_eth_price()
    print(f"Текущая стоимость газа в Ethereum: {gas_price} Gwei")
    print(f"Текущая цена Ethereum: ${eth_price:.2f}")
    print(f"Стоимость Газа в долларах - {((gas_price * eth_price)/1000000000)*eth_price} $")
    time.sleep(30)


# 21 000 газа * 35 гвеев / 1 000 000 000 = 0,000735 ETH * 497 долларов (цена1 ETH) = 0,36 доллара.

