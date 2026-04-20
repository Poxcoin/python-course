from os import stat_result
history = []
total_balance = 0  
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
    print(f"История всех сделок:{history}")
    print(f"Общий баланс:{total_balance}USDT")
    
    print("\n---ВАША ИСТОРИЯ СДЕЛОК ---")
    
    for trade in history:
        name = trade["name"]
        res = trade["result"]
        print(f"Монета: {name} | Прибиль: {res} USDT")

    print("\n----------------")
