numbers = [10, 4, 8, 12, 7, 15, 19, 25]
k = 4

def topK():
    numbers.sort(reverse=True)
    print(numbers[:k])
    # reversedNumbers = numbers[::-1]
    # print(numbers)
    # print(reversedNumbers)
    # for i in range(len(numbers)):
    #     print(numbers[i])





topK()