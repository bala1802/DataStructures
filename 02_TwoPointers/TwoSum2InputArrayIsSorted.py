'''
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
'''

import math

def twoSum(numbers: list, target: int) -> list:
    
    leftPointer = 0
    rightPointer = len(numbers) - 1
    
    while(leftPointer < rightPointer):
        if numbers[leftPointer] + numbers[rightPointer] > target:
            rightPointer -= 1
        elif numbers[leftPointer] + numbers[rightPointer] < target:
            leftPointer += 1
        else:
            return [leftPointer+1, rightPointer+1]

        
print(twoSum(numbers = [2,7,11,15], target = 9))
print(twoSum(numbers = [2,3,4], target = 6))
print(twoSum(numbers = [-1,0], target = -1))