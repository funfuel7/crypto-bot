import ccxt
from config import BINGX_API_KEY, BINGX_API_SECRET, USE_PAPER


# CCXT supports bingx as `bingx` or `bingx` may be available; if not, REST wrappers are needed.


class BingxClient:
def __init__(self):
if USE_PAPER:
self.exchange = None
return
self.exchange = ccxt.bingx({
'apiKey': BINGX_API_KEY,
'secret': BINGX_API_SECRET,
'enableRateLimit': True,
})


def create_order(self, symbol, side, amount_usdt, leverage, price=None, reduce_only=False):
# amount_usdt: notional in USDT; convert to qty according to contract size
if USE_PAPER:
return {'id': 'PAPER-' + symbol, 'status': 'closed', 'filled': amount_usdt}
# example using ccxt create_order — exchanges vary; you *must* adapt parameters to BingX API
params = {
'leverage': leverage,
}
# This is illustrative — adjust to bingx's param names: 'positionSide', 'reduceOnly', etc.
return self.exchange.create_order(symbol, 'market', side, None, price, params)


def fetch_balance(self):
if USE_PAPER:
return {'USDT': {'free': 1000, 'used': 0, 'total': 1000}}
return self.exchange.fetch_balance()


def fetch_positions(self):
if USE_PAPER:
return []
# method depends on exchange; ccxt may implement fetch_positions
return self.exchange.fetch_positions()
