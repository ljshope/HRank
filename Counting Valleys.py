# -*- coding: utf-8 -*-
 
def countingValleys(steps, path):
    level = 0
    valleys = 0
    start = 0
    for step in path:
        if step == 'U':
            level += 1
        else:
            level += -1
        if level < 0 and start == 0:
            start = 1
            valleys +=1
        if level == 0:
            start = 0
        print( start, level, valleys )
    return valleys
            
