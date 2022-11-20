#!/usr/bin/env python3

def print_fibonacci(length):
    res = []
    if (length > 0): res.append(0)
    if (length > 1): res.append(1)
    for i in range(2,length):        
        res.append(res[i-1] + res[i-2])

    print(res)

# def recursion(length):
#     if (length == 0): return 0
#     if (length == 1): return 1

#     return recursion(length-1) + recursion(length - 2)