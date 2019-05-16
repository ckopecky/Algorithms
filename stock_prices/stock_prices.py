#!/usr/bin/python

import argparse

# Right now this takes into account buying at min at selling at max regardless of time. Did not realize that the list was indicative of time throughout the day. 

def find_max_profit(prices):
  current_min_price = float("inf")
  current_max_price = -float("inf")

  if len(prices) == 0:
    profit = None
    return profit
  
  if len(prices) == 1:
    current_min_price = prices[0]
    current_max_price = prices[0]
    profit = current_max_price - current_min_price
    return profit

  else:
    i = 0
    while i < len(prices):
      if prices[i] < current_min_price:
        current_min_price = prices[i]
      if prices[i] > current_max_price:
        current_max_price = prices[i]
      i = i + 1
    profit = current_max_price - current_min_price
    return profit
    
  



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))