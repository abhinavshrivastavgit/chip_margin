production_cost = input('Enter the production cost:')
selling_price = input('Enter the selling price:')
profit = int(selling_price)- int(production_cost)
if profit > 1000:
    print('Profitable AI unit')
else:
    print('Optimize Supply Chain')