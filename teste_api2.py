from yahooquery import Ticker

ticker = Ticker('AAPL')

# Histórico de preços
hist = ticker.history(start='2025-01-01', end='2025-05-30')

print(hist.tail())
