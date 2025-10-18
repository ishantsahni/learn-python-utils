string = 'my name is ishant sahni'

def reverseString():
    reverseString = ''
    for i in range(len(string) - 1, -1, -1):
        reverseString = reverseString + string[i]
    print(reverseString)



reverseString()