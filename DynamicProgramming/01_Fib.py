
'''
Recursive function
'''
def fibonacci1(n):
    if n <= 2:
        return 1
    return fibonacci1(n-1) + fibonacci1(n-2)

'''
Recursive function  + Memoization
'''
def fibonacci2(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci2(n-1, memo) + fibonacci2(n-2, memo)
    return memo[n]



print(fibonacci2(6))
print(fibonacci2(7))
print(fibonacci2(8))
print(fibonacci2(500))


