s=(input("TYPE ANY WORD"))
def isPalindrome(s):
    return s == s[::-1]
ans=isPalindrome(s)
if ans:
    print(s,"IS A PALINDROME")
else:
    print(s,"IS NOT A PALINDROME")
input()
