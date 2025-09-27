import math

def discount(count, rules, price):
    for threshold, rate in rules:
        if count > threshold:
            return math.ceil(price * rate)
    return price

def book_price(x, y, z, price) -> int:
    price[0] = discount(x, [(30, 0.8), (20, 0.85), (10, 0.9)] , price[0])
    price[1] = discount(y, [(30, 0.8), (20, 0.85), (10, 0.95)], price[1])
    price[2] = discount(z, [(30, 0.7), (20, 0.8), (10, 0.85)], price[2])

    total = price[0] * x + price[1] * y + price[2] * z
    return int(total)

price = [380,1200,180]
x = int(input())
y = int(input())
z = int(input())

if 0 < x < 100 and 0 < y < 100 and 0 < z < 100:
    total =book_price(x,y,z,price)
    print(total)