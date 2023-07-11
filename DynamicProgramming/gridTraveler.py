def gridTraveler(m, n, memo={}):
    key = str(m)+ ',' + str(n)
    
    if key in memo:
        return memo[key]
    if m==1 and n==1:
        return 1
    if m==0 or n==0:
        return 0
    
    memo[key] = gridTraveler(m-1, n) + gridTraveler(m, n-1)
    return memo[key]

print(gridTraveler(1,1))
print(gridTraveler(2,3))
print(gridTraveler(5,5))
print(gridTraveler(5,7))
print(gridTraveler(7,7))
print(gridTraveler(10,10))
print(gridTraveler(100,100))