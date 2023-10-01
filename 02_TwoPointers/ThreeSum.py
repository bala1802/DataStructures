def threeSum(numbers: list) -> list:
    result = [] #List of lists
    numbers.sort()

    for i, a in enumerate(numbers):
        
        if i > 0 and a == numbers[i-1]:
            continue

        leftPointer, rightPointer = i+1, len(numbers)-1

        while(leftPointer < rightPointer):
            threeSum = a + numbers[leftPointer] + numbers[rightPointer]
            if threeSum > 0:
                rightPointer -= 1
            elif threeSum < 0:
                leftPointer += 1
            else:
                print("The Three Sum value is : ", threeSum)
                result.append([a, numbers[leftPointer], numbers[rightPointer]])
                leftPointer += 1
                while leftPointer < rightPointer and numbers[leftPointer] == numbers[leftPointer-1]:
                    leftPointer += 1
    
    return result

# print(threeSum(numbers=[-1,0,1,2,-1,-4]))
# print(threeSum(numbers=[0,1,1]))
# print(threeSum(numbers=[0,0,0]))

print(threeSum(numbers=[1,2,-2,-1]))