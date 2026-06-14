tickers = ["AAPL", "VOO", "META", "MSFT", "GOOGL"]
buy_prices = [182.50, 430.00, 675.28, 310.00, 140.00]
current_prices = [198.00, 512.30, 674.88, 415.50, 175.50]
shares = [10, 5, 3, 8, 12]

# Now write the loop!
for i in range(len(tickers)):
    # Your code here
    pnl=(current_prices[i] -buy_prices[i]) * shares[i]
    return_pct=((current_prices[i]-buy_prices[i])/buy_prices[i])*100
    print("Tickers:",tickers[i])
    print("P&L:",round(pnl,2))
    print("Return:%", round(return_pct,4))
