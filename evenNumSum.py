def evenNumSum():
    num = input('Enter the number')
    count = 0
    for i in range(int(num) + 1):
        if(i % 2 == 0):
            count = count + i
    print(f'\n{count}')




evenNumSum()