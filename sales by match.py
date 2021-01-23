# -*- coding: utf-8 -*-

#str = '1 1 3 1 2 1 3 3 3 3' 
#list(map(int, str.rstrip().split())) 


def sockMerchant(n, ar):
    sorted_ar = sorted( ar )
    counter = 1
    result = 0
    for i in range(n-1):
        if sorted_ar[i] == sorted_ar[i+1]:
            counter +=1
        else:
            cc = counter//2
            result += cc
            counter = 1
    cc = counter//2
    result += cc
        
    return result 