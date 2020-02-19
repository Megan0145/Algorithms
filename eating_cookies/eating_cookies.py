#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution


# 1 cookie = only 1 way to eat 1 cookie
# 1 = 1

# 2 cookies = 
  # - eat both at once
  # - eat 1 then eat 1
# 2 = 2

# 3 cookies =
  # - eat all 3 at once
  # - eat 1 then eat 2 
  # - eat 2 then eat 1
  # - eat 1 then eat 1 then eat 1
# 3 = 4

# 4 cookies = 
  # - eat all 4 at once
  # - eat 3 then eat 1
  # - eat 1 then eat 3
  # - eat 1 then 1 then 2
  # - eat 1 then 2 then 1
  # - eat 2 then 1 then 1
  # - eat 1 then 1 then 1 then 1
# 4 = 7

# 5 cookies = 
  # - eat all 5 at once
  # - eat 4 then 1
  # - eat 1 then 4
  # - eat 3 then 2
  # - eat 2 then 3
  # - eat 1 then 1 then 3
  # - eat 1 then 3 then 1
  # - eat 3 then 1 then 1
  # - eat 1 then 1 then 1 then 2
  # - eat 1 then 1 then 2 then 1
  # - eat 1 then 2 then 1 then 1
  # - eat 2 then 1 then 1 then 1
  # - eat 1 then 1 then 1 then 1 then 1
# 5 = 13

# 6 cookies = 
  # - eat all 6 at once
  # - eat 5 then 1
  # - eat 1 then 5
  # - eat 2 then 4
  # - eat 4 then 2
  # - eat 3 then 3
  # - eat 4 then 1 then 1
  # - eat 1 then 4 then 1
  # - eat 1 then 1 then 4
  # - eat 1 then 2 then 3
  # - eat 1 then 3 then 2
  # - eat 2 then 1 then 3
  # - eat 2 then 3 then 1
  # - eat 3 then 1 then 2
  # - eat 3 then 2 then 1
  # - eat 2 then 2 then 2
  # - eat 2 then 2 then 1 then 1
  #   .....
  # - eat 1 then 1 then 1 then 1 then 1 then 1
# eventually will give 24 permutations
# 6 = 24

# Therefore:
# 1 = 1
# 2 = 2
# 3 = 4
# 4 = 7
# 5 = 13
# 6 = 24
# ..and so on

# This can be achieved by effectively creating a recursive function that gets the fibionacci number 
# for each val of n (or cookies in this case) but recursively calling the function to get the 
# fib of n - 3 on each call too:

def eating_cookies(n, cache=None): 
  # base cases to return from recursion:
    if n<0: 
        return 0
    elif n==0: 
        return 1
 
  # original fibionacci seq function would be:
  # return eating_cookies(n-1) + eating_cookies(n-2) 
  #but in this case to get the desired value we have to pass in n - 3 too
    else: 
      return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
