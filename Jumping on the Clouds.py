# -*- coding: utf-8 -*-

def jumpingOnClouds(c):
    steps = 0
    current= 0
    while current < len(c)-1:
        if current + 2 < len(c):
            if c[current+2] == 0:
                current += 2
            else:
                current += 1
        else:
            current += 1
        steps += 1
    return steps