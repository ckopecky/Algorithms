#!/usr/bin/python

import sys

'''
Let's understand the problem:

we need to generate a function that will give us all the possible plays that can be made in a game of rock paper scissors when given some input n, which represents the number of plays per round. 



'''

def rock_paper_scissors(n):
  pass 


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')