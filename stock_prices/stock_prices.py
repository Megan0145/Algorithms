#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # initialize index of max element in array to 1
  max_index = 1
  # initialize index of min element in array to 0
  min_value = 0
  # initialize max profit to 0
  max_profit = 0

# 1:
# get index of maximum value from index 1 - index of last element in array

# (if index of maximum value was at index 0, you would have to get the next largest element 
# after index 0 anyway and calculate max profit from there
# eg array = [100, 55, 4, 98, 10, 18, 90, 95, 43]
# max value is 100, at index 0. 
# To get max profit you would have to find the next largest number (which is 98) 
# and subtract next min value from it (98 - 4 = 4)
# Therefore no need to loop over array from index 0, just start at index 1)

  for i in range(1, len(prices)):
    if prices[i] > prices[max_index]:
      max_index = i

# 2  
# get the value of the smallest element in array up to index of max element
  min_value = min(prices[:max_index]) 

# 3
# calculate max_profit by subtracting minimum value from value at max_index
  max_profit = prices[max_index] - min_value 

# 4  
# return the max profit
  return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))