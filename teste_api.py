import pandas as pd
import yfinance as yf

ticker = "AAPL"

dt_inicial = "2025-01-01"
dt_final = "2025-05-30"

dados = yf.download(ticker, dt_inicial, dt_final)
print(dados)