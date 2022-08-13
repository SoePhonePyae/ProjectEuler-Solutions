import math

def lcm_to_a_num(limit):
    if limit == 1:
        return limit
    
    return math.lcm(limit, lcm_to_a_num(limit-1))

print(lcm_to_a_num(20))
