''' Fibonacci pattern '''

#memoization ! starting a cache so that it's remembered what the n-1 and n-2 fib num is.
def Fibonacci(n, cache={}):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        if n in cache:
            return cache[n]
        nth = Fibonacci(n-1) + Fibonacci(n-2)
        cache[n] = nth
        return nth;

# print(Fibonacci(1))
# print(Fibonacci(3))
# print(Fibonacci(40))
# print(Fibonacci(45))
# print(Fibonacci(100))

'''
without cache: time complexity would be O(2 ^ n)
with cache: O(n)
'''

#pointers solution O(n) ... linked list maybe?
def Fibonacci_prev(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    prevprev = 0
    prev = 1
    for i in range(2, n):
        curr = prev + prevprev
        prevprev = prev
        prev = curr
        print(curr)
    return curr
(Fibonacci_prev(3))
(Fibonacci_prev(10))