    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 19:04:39 2022

@author: william
"""

def count_swap(x):
    count = 0
    l = x.copy()
    for i in l:
        if len(x) == 0:
            break
        t = 0 #Index of shoe
        thing = x[0] #Sets the shoe checked as the first in the current list
        if thing in x and -1 * thing in x:
            if thing < 0: #Checks if left or right shoe
                while x.index(((-1)*thing)) != x.index(thing) + 1: #While the index the two shoes are not next to each other
                    y = x.index(thing)
                    x[y], x[y + 1] = x[y + 1], x[y]
                    count += 1
                    t += 1 #Move "i" to the right, increments the index, and adds one to the number of moves
                x.pop(t)
                x.pop(t) #Deletes the pair of shoes in case of two pairs of the same shoe size
            else:
                while x.index(-1*thing) != x.index(thing) - 1:
                    y = x.index(thing)
                    x[y], x[y + 1] = x[y + 1], x[y]
                    count += 1
                    t += 1
                x.pop(t)
                x.pop(t - 1)
        elif thing in x and -1 * thing not in x:
            if x.index(thing) == 0:
                x.pop(0)
            else:
                pass
    return count
print(count_swap([3,2,1,-1,-2,-3,4]))
print(count_swap([3,2,1,-1,-2,-3,-1]))
print(count_swap([3,2,1, 4,-2,-3,-1]))
