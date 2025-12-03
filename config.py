import os
from dotenv import load_dotenv


load_dotenv()


TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
ALLOWED_CHAT_ID = int(os.getenv('ALLOWED_CHAT_ID', '0'))
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
BINGX_API_KEY = os.getenv('BINGX_API_KEY')
BINGX_API_SECRET = os.getenv('BINGX_API_SECRET')
BINGX_API_PASSPHRASE = os.getenv('BINGX_API_PASSPHRASE')
STARTING_CAPITAL_USDT = float(os.getenv('STARTING_CAPITAL_USDT', '1000'))
MIN_VOLUME_USD = int(os.getenv('MIN_VOLUME_USD', '50000000'))
SCAN_INTERVAL_SECONDS = int(os.getenv('SCAN_INTERVAL_SECONDS', '8'))
MIN_LEVERAGE = int(os.getenv('MIN_LEVERAGE', '5'))
MAX_LEVERAGE = int(os.getenv('MAX_LEVERAGE', '10'))
USE_PAPER = os.getenv('USE_PAPER', 'true').lower() == 'true'
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')


# quick safety checks
if TELEGRAM_TOKEN is None:
raise RuntimeError('TELEGRAM_TOKEN is required')
if ALLOWED_CHAT_ID == 0:
raise RuntimeError('ALLOWED_CHAT_ID must be set to your Telegram user id')
