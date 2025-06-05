menu=['porridge', 'croissant', 'sandwich', 'brownie']
stock= {'porridge': int('30'), 'croissant': int('50'), 'sandwich': int('15'), 'brownie': int('40')}  
price= {'porridge': int('5'), 'croissant': int('2'), 'sandwich': int('4'), 'brownie': int('3')}


'''Calculating the value total of the stock using the 'for loop'. 
For each value in stock and(if) each value in price, the total price value will return 
the multiplication of the stock values and price values '''

total_menu={}
for v in stock:
    if v in price:
        total_menu[v] = (stock[v] * price [v])
        
print(total_menu)
