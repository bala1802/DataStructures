def howSum(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    
    for number in numbers:
        remainder = targetSum - number
        remainderResult = howSum(remainder, numbers)
        # print(remainderResult, " for ", number)
        if remainderResult!= None:
            return remainderResult + [number]
    return None

print(howSum(targetSum=8,numbers=[2,3,5]))
# print(howSum(targetSum=7,numbers=[2,4]))