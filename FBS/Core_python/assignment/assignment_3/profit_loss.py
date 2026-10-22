selling_price=int(input("enter selling price:-"))
cost_price=int(input("enter cost "))

profit=selling_price-cost_price
loss=cost_price-selling_price

if selling_price>cost_price:
    print('you have profit')

else:
    selling_price<cost_price
    print('you have big loss')