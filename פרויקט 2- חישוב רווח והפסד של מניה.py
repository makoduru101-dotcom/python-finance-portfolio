# Lesson 1 — Position P&L Calculator
# Project: Mini Trade Tracker

stock_name = "Meta"
ticker = "META"
buy_price = 675.28
current_price = 674.88
shares = 3

pnl = (current_price - buy_price) * shares
return_pct = ((current_price - buy_price) / buy_price) * 100

print("Stock:", stock_name)
print("Ticker:", ticker)
print("Shares:", shares)
print("Buy Price:", buy_price)
print("Current Price:", current_price)
print("P&L:", round (pnl,2))
print("Return %:",round(return_pct,4))
