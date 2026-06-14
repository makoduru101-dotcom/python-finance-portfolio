#portfolio analyzer
def calculate_pnl(buy_price, current_price, shares):
    pnl = (current_price-buy_price)*shares
    return_pct=(current_price-buy_price/buy_price)*100
    return pnl, return_pct

portfolio= {
    "TSLA":{"buy_price":180.00,"current_price":245.00,"shares":8},
    "AMZN":{"buy_price":140.00,"current_price":195.00,"shares":6},
    "NVDA":{"buy_price":450.00,"current_price":875.00,"shares":4},
    "META":{"buy_price":675.00,"current_price":674.88,"shares":3},
    "APPL":{"buy_price":182.50,"current_price":198.00,"shares":10}
 }
    # קוד שלך

def generate_signal(return_pct):
    if return_pct > 30:
        return "🔥 STRONG BUY"
    elif return_pct >10:
        return "BUY"
    elif return_pct = 0 :
        return "BREAK EVEN"
    elif return_pct < 0 :
        return "LOSS"
        
    # המשך...

def print_position(ticker, pnl, return_pct, signal):
    print("___",ticker,"___")
    print("P&L:",round(pnl,2))
    print("RETURN:%",round(return_pct,4))
    
    # קוד שלך  