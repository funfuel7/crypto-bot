import threading
import time
import traceback
from config import MIN_VOLUME_USD, SCAN_INTERVAL_SECONDS, MIN_LEVERAGE, MAX_LEVERAGE, STARTING_CAPITAL_USDT
from mexc_client import get_futures_tickers, get_24h_volume, get_klines
from bingx_client import BingxClient
from openrouter_client import ask_openrouter
from utils import now_ts


class Scalper:
def __init__(self, telegram_notify):
self.running = False
self.thread = None
self.telegram_notify = telegram_notify
self.bx = BingxClient()


def start(self):
if self.running:
return 'Already running'
self.running = True
self.thread = threading.Thread(target=self.loop, daemon=True)
self.thread.start()
return 'Scalp started'


def stop(self):
self.running = False
return 'Stopping scalp'


def loop(self):
while self.running:
try:
tickers = get_futures_tickers()
# filter by volume
candidates = []
for t in tickers.get('data', []):
try:
sym = t['symbol']
vol = float(t.get('quoteVolume', 0))
if vol >= MIN_VOLUME_USD:
candidates.append(sym)
except Exception:
continue


for sym in candidates:
if not self.running:
break
klines = get_klines(sym, '1m', limit=120)
# ask OpenRouter for a quick evaluation of whether this looks like scalping opportunity
prompt = f"Analyze this 1m kline quick summary for {sym} and tell if there's a scalping opportunity with conservative 5-10x leverage. Return: DECISION: [YES/NO], REASON: one-line, ENTRY:price, SL:price, TP:price, TRAIL:method"
advice
