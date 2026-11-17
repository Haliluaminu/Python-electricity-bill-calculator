product = input("product name: ")
price = float(input("price: "))
quantity = int(input("quantity: "))

total = price * quantity

if total >= 100000:
    discount = 0.10  
    print(price, "*", quantity, "=", total)
    print("0.10 discount =", discount * total)
    print("amount after discount:", total - (discount * total))
elif total >= 50000:
    discount = 0.05
    print(price, "*", quantity, "=", total)
    print("0.05 discount =", discount * total)
    print("amount after discount:", total - (discount * total))
else:
    discount = 0
    print(price, "*", quantity, "=", total)
    print("0.00 discount =", discount * total)
    print("amount after discount:", total - (discount * total))