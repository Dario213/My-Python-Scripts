a, b = [int(x) for x in input().split()]
if a == 11 and b == 11:
    a = 1
    b = 1
elif b == 11:
    b = 1
elif a == 11:
    a = 1
else:
    a = a
    b = b

suma = a + b

if suma > 21:
    print("0")
else:
    print(suma)
