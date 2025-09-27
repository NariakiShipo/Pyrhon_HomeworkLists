poker = {'A': 1, 'K': 0.5, 'Q': 0.5, 'J': 0.5, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

X_Poker = 0
Y_Poker = 0
for i in range(6):
    num = input()
    if i < 3:
        X_Poker += poker[num]
    else:
        Y_Poker += poker[num]
if X_Poker > 10.5:
    X_Poker = 0
if Y_Poker > 10.5:
    Y_Poker = 0
if float(X_Poker).is_integer():
    X_Poker = int(X_Poker)
if float(Y_Poker).is_integer():
    Y_Poker = int(Y_Poker)
print(X_Poker)
print(Y_Poker)
if X_Poker > Y_Poker:
    print('X Win')
elif X_Poker < Y_Poker:
    print('Y Win')
else:
    print('Tie')