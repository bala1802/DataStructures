def maxArea(heights: list) -> int:
    if len(heights) == 0  or len(heights) == 1:
        return 0
    if len(heights) == 2:
        return min(heights[0], heights[1])
    
    result = 0
    leftPointer, rightPointer = 0, len(heights) - 1

    while leftPointer < rightPointer:
        area = (rightPointer - leftPointer) * min(heights[leftPointer], heights[rightPointer])
        result = max(result, area)

        if heights[leftPointer] < heights[rightPointer]:
            leftPointer += 1
        else:
            leftPointer += 1
    return result

print(maxArea(heights = [2,3,4,5,18,17,6]))