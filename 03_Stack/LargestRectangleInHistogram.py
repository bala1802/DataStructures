def largestRectangleArea(heights: list):
    maxArea = 0
    stack = [] #Pair of Index and Height

    for eachIndex, eachHeight in enumerate(heights):
        start = eachIndex

        while stack and stack[-1][1] > eachHeight:
            stackIndex, stackHeight = stack.pop()
            maxArea = max(maxArea, stackHeight * (eachIndex - stackIndex))
            start = stackIndex
        
        stack.append([start, eachHeight])
    
    for eachStackIndex, eachStackHeight in stack:
        maxArea = max(maxArea, eachStackHeight * (len(heights) - eachStackIndex))

    return maxArea

#print(largestRectangleArea(heights = [2,1,5,6,2,3]))
#print(largestRectangleArea(heights = [2,4]))

print(largestRectangleArea(heights=[5, 3, 5, 3, 5, 3, 5, 3]))
