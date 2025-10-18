def checkPalindrome():
    string = input("Enter your name: ")
    reversedString = string[::-1]
    isPalindrome = string == reversedString
    if(isPalindrome):
        print("The string is palindrome")
    else:
        print("The string is not palindrome")

checkPalindrome()