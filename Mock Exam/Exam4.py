""" Coffee Shop """

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = int(input())

def first(price_per_cup, discount, wanted_cups) :
    """ first promotion price """
    price = price_per_cup
    count = 1

    while count < wanted_cups :
        price +=  price_per_cup - (price_per_cup * (discount / 100))
        count += 1

    return price

def second(price_per_cup, discount, atleast, wanted_cup) :
    """ second promotion price """
    price = 0
    for _ in range(1, wanted_cup + 1) :
        price += price_per_cup

    if price >= atleast :
        price -=  price * (discount / 100)

    return price

first = first(a, b, e)
second = second(a, c, d, e)

if first < second :
    print("1")
    print(f"{first:.2f}")
else :
    print("2")
    print(f"{second:.2f}")
