#check the list is palindrome or not
givenstr=input("Enter the number")
isPalindrome=True
for i in range(len(givenstr)//2):
    if givenstr[i] != givenstr[len(givenstr)-i-1]:
        isPalindrome=False
if isPalindrome:
    print("is a palindrome")
else:
    print("is not a palindrome")
