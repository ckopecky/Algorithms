#!/usr/bin/python

import sys

'''
so the problem here is that we need to find all the permutations of the possible plays of rock, paper, scissors for each player there is. The more players, three times more plays. This leads to an O(3^n) solution.

n = 1

[["rock"], ["paper"], ["scissors"]] -- we append in its own array, each of the possible plays for 1 player. 

n = 2

[
  ["rock", "rock"], ["rock", "paper"], ["rock", "scissors],
  ["paper", "rock"], ["paper", "paper"], ["paper", "scissors"],
  ["scissors", "rock"], ["scissors", "paper"], ["scissors", "scissors"]
]

-- Here we see that we have triple the amount of permutations. We use the n = 1 array to add each of those items to each index of the mutated array to create a new permutation, until we have exhausted all the plays. 



'''
def rock_paper_scissors(n):

  choices = ["rock", "paper", "scissors"]
  possible_hands = []
  
  #helper func
  def find_results(num_rounds_left, result=[]):
    if num_rounds_left == 0:
      possible_hands.append(result)
      return
    for choice in choices:
      new_result = result + [choice]
      find_results(num_rounds_left - 1, new_result)
    
  find_results(n, [])
  return possible_hands
  
"""
Iterative implementation or rps
"""
# def rock_paper_scissors_iterative(n):
#   output = []
#   possible_plays = ['scissors', 'paper', 'rock']

#   stack = []
#   stack.append([])

#   while len(stack) > 0:
#     hand = stack.pop()

#     if n == 0 or len(hand) == n:
#       output.append(hand)
#     else:
#       for play in possible_plays:
#         stack.append(hand + [play])

#   return output



    



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')