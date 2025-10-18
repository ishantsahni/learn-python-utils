def countVowels():
    string = input("Enter the string: ")
    count = 0
    for i in range(len(string)):
        if(string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u'):
            count = count + 1

    print(f'The number of vowels in {string} are {count}')



countVowels()