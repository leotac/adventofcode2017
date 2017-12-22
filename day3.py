import math
import numpy as np 

#37  36  35  34  33  32  31
#38  17  16  15  14  13  30
#39  18   5   4   3  12  29
#40  19   6   1   2  11  28
#41  20   7   8   9  10  27
#42  21  22  23  24  25  26 ...

def previous_square(n):
    root = int(math.sqrt(n))
    return root, root**2

def dist(n):
    r, s = previous_square(n)
    next_corner = r*(r+1) + 1
    if n == s:
        return r - 1
    if n == s + 1 or n == next_corner:
        return r
    if n > next_corner:
        previous_corner = next_corner
        next_corner = (r+1)**2
    else:
        previous_corner = s + 1
    print(previous_corner)
    return dist(previous_corner) - min((n-previous_corner), (next_corner-n))


right = np.array([1,0])
up = np.array([0,1])
left = np.array([-1,0])
down = np.array([0,-1])
directions = [right, up, left, down]

def iter_direction(i = 0):
    while True:
        yield directions[i]
        i = (i+1)%4
 
# sum in the 8 adjacent positions
def sum_neighbors(v, t):
    return v.get(tuple(t + right), 0) + v.get(tuple(t + left), 0) + v.get(tuple(t + up), 0) + v.get(tuple(t + down), 0) +\
            v.get(tuple(t + right + up), 0) + v.get(tuple(t + left + up), 0) + v.get(tuple(t + right + down), 0) + v.get(tuple(t + left + down), 0)


# Spiral fibonacci
def first_largest_value(target, max_it = 1000):
    v = dict()
    v[0,0] = 1
    side_len = 1
    cur = np.array([0,0])
    dir_iterator = iter_direction() 
    for _ in range(max_it):
            print("Side length:", side_len)
            for _ in range(2):
                direction = next(dir_iterator)
                print("direction:", direction)
                for i in range(side_len):
                    cur += direction
                    v[tuple(cur)] = sum_neighbors(v, cur)
                    print(cur,v[tuple(cur)])
                    if v[tuple(cur)] > target:
                        return v[tuple(cur)]
            side_len += 1
    return 0
