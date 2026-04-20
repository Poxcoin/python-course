from rich.console import Console
from rich.table import Table

history = []
total_balance = 0  
console = Console()
while True:
    coin_name = input("Введите имя монети: ")

    if coin_name == "exit":
        break

    buy_price = float(input("write price: "))
    sell_price = float(input("write sell price: "))
    amount = float(input("how much buy: "))

    profit = (sell_price - buy_price) * amount

    print(f"я слежу за монетой{coin_name}")
    print(f"Buy price {buy_price}")

    if profit > 0:
        print(f"china: {profit}")
    elif profit < 0:
        print(f"fck: {profit}")
    else:
        print(f"zero")
    
    trade_info = {"name": coin_name, "result": profit}
    
    history.append(trade_info)
    total_balance = total_balance + profit
    
    table = Table(title="Trade History")
    table.add_column("Coin")
    table.add_column("Profit")
    for trade in history:
        name = trade["name"]
        profit = trade ["result"]
        table.add_row(name, f"{profit}USDT")
        
    console.print(table)
    console.print(f"Total balance: {total_balance} USDT", style="bold blue")

    print("\n----------------")
