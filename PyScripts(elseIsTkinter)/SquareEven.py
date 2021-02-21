def squareEven(array = [], lenght = int):
    if array == None:
        return array

    for i in range(lenght):
        if i % 2 == 0:
            array[i] *= array[i]

    return print(array)

a_list = [int(x) for x in input().split()]
size = len(a_list)

squareEven(a_list, size)
