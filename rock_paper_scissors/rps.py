#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  result = []
  options = ['rock', 'paper', 'scissors']

  # initialise played to be empty array if no rounds have been played yet
  def play(turn, played = []):  
    # base case: if turn = 0,
    # we've played all rounds (n rounds)
    # append the value of the played array to results and return from function
    if turn == 0: 
      result.append(played)
      return

    # else we have more turns left (turn not equal to zero)
    else:
      # only three options to choose from, 
      # could also do for option in options and pass the option into the recursive function
      # rather than the option at index i 
      for i in range(3):
        # recur play function again,
        # passing in the no of turns decremented by one and the current played list + the value of option at index i
         play(turn - 1, played + [options[i]])
  # call recursive play function, passing in n
  # if n == 0, wil break out of function, else will play for n rounds
  play(n)
  # return the result
  return result

print(rock_paper_scissors(2))  



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')