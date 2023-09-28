def solution(s:list):
    stack = []
    for eachElement in s:
        if eachElement == '+':
            stack.append(stack.pop() + stack.pop())
        elif eachElement == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif eachElement == '*':
            stack.append(stack.pop() * stack.pop())
        elif eachElement == '/':
            a, b = stack.pop(), stack.pop()
            print("b is : ", b)
            print("a is : ", a)
            stack.append(int(b/a))
        else:
            stack.append(int(eachElement))
    
    print("End result : ", stack[0])

# solution(s=["2","1","+","3","*"])
# solution(s=["4","13","5","/","+"])
solution(s=["10","6","9","3","+","-11","*","/","*","17","+","5","+"])