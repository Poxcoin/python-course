def format_result(coin_name:str, profit:float) -> str:
    if profit < 0:
        return f"{coin_name}: -{abs(profit)} USDT"
    elif profit > 0:
        return f"{coin_name}: +{abs(profit)} USDT"
    else:
        return f"{coin_name}: {profit} USDT"

def calculate_profit(buy_price:float, sell_price:float, amount:float) -> float:
    return (sell_price - buy_price) * amount

def run_tracker() -> None:
    while True:
        coin_name = input(f"Enter the name of the coin: ")
        if coin_name == "exit":
            break
        buy_price = float(input(f"Enter the buy price of {coin_name}: "))
        sell_price = float(input(f"Enter the sell price of {coin_name}: "))
        amount = float(input(f"Enter the amount of {coin_name} to trade: "))
        profit = calculate_profit(buy_price, sell_price, amount)
        print(format_result(coin_name, profit))
        
if __name__ == "__main__":    
    run_tracker()