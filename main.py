import os, time, telebot, yfinance as yf

TOKEN = os.environ.get("TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")

bot = telebot.TeleBot(TOKEN)

def get_price(symbol):
    try:
        t = yf.Ticker(symbol)
        d = t.history(period="1d", interval="1h")
        return round(float(d['Close'].iloc[-1]), 2)
    except:
        return "N/A"

while True:
    try:
        btc = get_price("BTC-USD")
        msg = f"📊 SIBIKE SIGNALS - HOURLY UPDATE\n\n💹 BTCUSD: ${btc}\n\n⏰ Time: Hourly\n🔥 Trade with discipline. No FOMO."
        bot.send_message(CHANNEL_ID, msg)
        print("Sent!")
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(3600)
