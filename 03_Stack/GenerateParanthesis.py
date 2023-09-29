def generateParanthesis_usingStack(n :int) -> list:
    
    #Only add open paranthesis if open < n
    #Only add close paranthesis if closed < open
    #valid if open == closed == n

    stack = []
    result = []

    def backtrack(open: int, close: int, counter: int):
        counter += 1

        if open == close == n:
            result.append("".join(stack))
        
        if open < n:
            # print("Open Stack Before Append at Counter : ", counter, " - ", stack)
            stack.append("(")
            backtrack(open+1, close, counter)
            stack.pop()
        
        if close < open:
            # print("Close Stack Before Append at Counter : ", counter, " - ", stack)
            stack.append(")")
            backtrack(open, close+1, counter)
            stack.pop()

    backtrack(open=0, close=0, counter=0)
    return result

def generateParanthesis(n: int) -> list:
    
    res = []

    def backtrack(open_n:int, closed_n:int, path:str):
        if open_n == closed_n == n:
            res.append(path)
            return
        if open_n < n:
            backtrack(open_n=open_n + 1, closed_n=closed_n, path=path + "(")
        if closed_n < open_n:
            backtrack(open_n=open_n, closed_n=closed_n + 1, path=path + ")")

    backtrack(open_n=0, closed_n=0, path="")
    return res

result = generateParanthesis(n=2)
print("The result is : ", result)