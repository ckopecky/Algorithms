#!/usr/bin/python

import argparse

def find_max_profit(prices):
  if(len(prices) == 1):
    return 0

  current_max_profit = prices[1] - prices[0]
  current_min_price = prices[0]
  
  '''

  we have a list of stock prices throughout the day -- we can only buy before we sell. And we can't buy and sell in same transaction. We only sell once a day

  Our max profit to start will be the second item - the first item. Then what we need to do is compare the difference of each index in the array and that first item and keep track of the min price and the max profit (difference between ith item and the first item)


  '''
  
  return current_max_profit



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))