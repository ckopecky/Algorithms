#!/usr/bin/python

import argparse

'''
the list of prices show the variance of price during different times of day. list is sorted by time and not by price. 

so the basic problem is to find the maximum profit you can make by buying first and then selling later in the day. 

what we need to do is to keep track of the min price so far and the max profit so far.

so we need to have some sort of pointer that starts at the beginning of the array and then a second pointer that starts at the second element in the array. 

the first element is automatically the current min price so far and the difference between the second element and the first element is the current max profit so far. 

if we do a while loop whose conditional is that i and j are both less than the length of the array, we can keep the while loop going without having nested loops I think. 

for the first check, we set i to the initial element in array and we set j to the third element in the array since we have already instantiated the the max profit so far is the difference between elemnt 1 and element 0. 

let's check to see if j element - i element is > max profit so far -- if it is update max profit

if not, advance j if there is length left in the array -- if not reset i to i + 1 and reset j to the "new" i + 1.


'''

def find_max_profit(prices):

  i = 0
  j = 1
  max_profit = float('-inf')
  while i < len(prices) and j < len(prices):
    difference = prices[j] - prices[i]
    print(difference)
    if difference > max_profit:
      max_profit = difference
      if j + 1 == len(prices):
        #we start over
        if i + 1 == len(prices):
          break
        else:
          i += 1
          j = i + 1 #new i
      else:
        j += 1
    else:
      if j + 1 == len(prices):
        #we start over
        if i + 1 == len(prices):
          break
        else:
          i += 1
          j = i + 1 #new i
      else:
        j += 1


  return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))