
def isValid(s):
    
    stack = []
    pairing = {
        "}" : "{",
        "]" : "[",
        ")" : "("
    }

    for eachCharacter in s:
        if eachCharacter in pairing:
            if stack and pairing[eachCharacter] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(eachCharacter)
    
    return True if not stack else False