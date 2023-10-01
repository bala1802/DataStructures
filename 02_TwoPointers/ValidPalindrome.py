def validPalindrome(s: str) -> bool:
    if s == "":
        return True
    
    leftPointer, rightPointer = 0, len(s) - 1
    while(leftPointer < rightPointer):
        
        while (leftPointer < rightPointer and not isAlphaNum(s[leftPointer])):
            leftPointer += 1
        
        while (rightPointer > leftPointer and not isAlphaNum(s[rightPointer])):
            rightPointer -= 1

        if s[leftPointer].lower() != s[rightPointer].lower():
            return False
        
        leftPointer += 1
        rightPointer -= 1
    
    return True

def isAlphaNum(c) -> bool:
    return ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9')

print(validPalindrome(s="A man, a plan, a canal: Panama"))
print(validPalindrome(s="race a car"))
print(validPalindrome(s=" "))
