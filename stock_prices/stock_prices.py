#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # initialize index of max element in array to 0
  max_index = 0
  # initialize max profit to 0
  max_profit = 0

# 1:
# get index of maximum value from index 0 - index of last element in array
  for i in range(len(prices)):
    if prices[i] > prices[max_index]:
      max_index = i

#2:
# once we have the index of the maximum element:
# if the index of the max element is 0 (it's the first element of the array)
# the maximum profit will be calculated by getting the next largest number in the array 
# and subtracting the value of the smallest element before it
# eg for array [100, 90, 80, 50, 20, 10]
# max element = 100
# max index = 0
# next largest element from index 1 to the last element in array = 90
# max profit = 90 - 100 = -10
  if max_index == 0: 
    next_biggest_value = max(prices[1:])
    max_profit = next_biggest_value - min(prices[:next_biggest_value])

# otherwise max profit will be calculated by subtracting the smallest element 
# that comes before index of max element from the max element
  else:
    max_profit = prices[max_index] - min(prices[:max_index]) 
  
  # return the max profit
  return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))