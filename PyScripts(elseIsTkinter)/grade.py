T = int(input())
i = 0
while i < T:
    math, alg = [int(x) for x in input().split()]

    if alg > 50 and math > 70:
        print("Pass")
    else:
        print("Fail")

    i += 1
