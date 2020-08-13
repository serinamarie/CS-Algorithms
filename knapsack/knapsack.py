#!/usr/bin/python

import sys
from collections import namedtuple
import itertools

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
    # Your code here

    pass


def knapsack_brute_force(weight_limit, items):
  max_value = -1
  best_combo = None
  for i in range(1, len(items)+1):
    list_of_combos = list(combinations(items, i))
    for combo in list_of_combos:
      # check weight and value
      value = 0 # of the entire combo
      weight = 0 # of the entire combo
      for item in combo:
        value += item.value
        weight += item.weight
      if weight <= weight_limit: # could fit in knapsack
          if value > max_value:
            max_value = value
            best_combo = combo

  return best_combo

def knapsack_greedy(weight_limit, items):
  for i in items:
    i.efficiency = i.value / i.weight

  # sort by efficiency (value/weight)
  items.sort(keys=lambda x: x.efficiency, reverse=True)

  sack = []
  weight = 0
  
  for i in items:
    weight += i.weight
    if weight > weight_limit:
      return sack
    else:
      sack.append(i)

  return sack





if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')