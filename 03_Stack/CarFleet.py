def carFleet(position: list, speed: list, target):
    pair = list(zip(position, speed))

    stack = []
    for eachPosition, eachSpeed in sorted(pair)[::-1]:
        stack.append((target - eachPosition) / eachSpeed)

        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    
    return len(stack)

# print(carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))
# print(carFleet(target = 10, position = [3], speed = [3]))
# print(carFleet(target = 100, position = [0,2,4], speed = [4,2,1]))

print(carFleet(position=[6,8], speed=[3,2], target=10))