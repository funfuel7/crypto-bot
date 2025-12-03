import requests


BASE = 'https://www.mexc.com/api-docs' # redirect; but we use MEXC public endpoints
MEXC_MARKET = 'https://api.mexc.com/api/v3'


def get_futures_tickers():
# fetch futures tickers; MEXC has multiple endpoints — this uses spot/v3 market endpoints as fallback
url = 'https://www.mexc.com/open/api/v2/market/ticker' # example; adapt if MEXC changes
r = requests.get(url, timeout=10)
r.raise_for_status()
return r.json()


def get_24h_volume(symbol: str):
# return 24h quoteVolume in USD equivalent or native quotes
# placeholder: use market ticker
url = f'https://www.mexc.com/open/api/v2/market/ticker?symbol={symbol}'
r = requests.get(url, timeout=10)
r.raise_for_status()
data = r.json()
# adapt to response structure — return float
return float(data['data'][0]['quoteVolume'])


def get_klines(symbol: str, interval='1m', limit=200):
url = f'https://www.mexc.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}'
r = requests.get(url, timeout=10)
r.raise_for_status()
return r.json()
