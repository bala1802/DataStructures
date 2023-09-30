def dailyTemperature(temperatures: list):
    result = [0] * len(temperatures)
    stack = [] #Pair: [temperature, index]

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            _, stackInd = stack.pop()
            result[stackInd] = (i - stackInd)
        stack.append([t, i])
    return result

result = dailyTemperature(temperatures=[73,74,75,71,69,72,76,73])
print(result)