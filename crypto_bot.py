import os
import logging
import ccxt
import pandas as pd
import talib
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --- Configuration ---
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
MIN_VOLUME = 40_000_000  # $40M minimum volume
TIMEFRAME = "15m"  # 15-minute candles
RR_RATIO = 2.2  # Minimum Risk/Reward

# Initialize exchange
mexc = ccxt.mexc({"enableRateLimit": True})

# --- Core Functions ---
def get_high_volume_coins():
    """Fetch coins with > $40M volume"""
    tickers = mexc.fetch_tickers()
    return [
        symbol for symbol in tickers
        if symbol.endswith("/USDT") and tickers[symbol]["quoteVolume"] >= MIN_VOLUME
    ]

def analyze_pair(pair):
    """AI-powered technical analysis"""
    ohlcv = mexc.fetch_ohlcv(pair, TIMEFRAME, limit=100)
    df = pd.DataFrame(ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])
    
    # Indicators
    df["rsi"] = talib.RSI(df["close"], 14)
    df["ema20"] = talib.EMA(df["close"], 20)
    df["macd"], _, _ = talib.MACD(df["close"])
    
    # Signal logic
    latest = df.iloc[-1]
    if latest["close"] > latest["ema20"] and latest["rsi"] < 30:
        return "LONG"
    elif latest["close"] < latest["ema20"] and latest["rsi"] > 70:
        return "SHORT"

def send_signal(context: CallbackContext, signal):
    """Send to Telegram"""
    context.bot.send_message(
        chat_id=CHAT_ID,
        text=f"🚀 {signal['pair']} {signal['direction']}\n"
             f"Entry: {signal['entry']:.4f}\n"
             f"TP: {signal['take_profit']:.4f} | SL: {signal['stop_loss']:.4f}",
        parse_mode="Markdown"
    )

# --- Bot Setup ---
def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    updater.job_queue.run_repeating(
        lambda ctx: scan_markets(ctx), interval=900, first=0
    )
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
