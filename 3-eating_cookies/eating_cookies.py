#!/usr/bin/python

import sys

'''
The problem here is basically to find how many different combinations of ways that Cookie Monster can eat n number of cookies. 

example:

if we have 3 cookies, Cookie Monster can eat 1 cookie three times, eat 1 cookie and then 2 cookies, 2 cookies then 1 cookie or eat all 3 cookies at once. That gives 4 possible ways.

0, 1, 2, 3, 4, 5
1  1  2  4  8  15

1 1 2 3 5 8 13 21 

1 1 2 4 7 13 24

pattern is prev 3 added together to get nth permutation. 

'''

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache={0: 1, 1: 1, 2: 2}):

  if n == 0 or n == 1 or n == 2:
    return cache[n]
  
  else:
    if n not in cache:
      cache[n] = eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
    return cache[n]
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')