#!/usr/bin/env python

# Remove empty lines from list:
# grep -v -e '^$' adjList.txt
import random

#total_num_lines = sum(1 for line in open('resources/adjList.txt'))


with open('resources/adjList.txt') as adj:
    lines = adj.readlines()
    random_pos1 = random.randint(0, len(lines)-1)
    random_pos2 = random.randint(0, len(lines) - 1)
    print("I AM " +lines[random_pos1].upper())
    print("YOU ARE " +lines[random_pos2].upper())
