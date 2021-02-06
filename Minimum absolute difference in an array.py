 
def minimumAbsoluteDifference(arr):
    sorted_arr = sorted( arr )
    minabs = 2*10e10
    for i in range( len( sorted_arr )-1 ):
        new = abs( sorted_arr[i] - sorted_arr[i+1])
        if new < minabs:
            minabs = new
    return minabs                 
