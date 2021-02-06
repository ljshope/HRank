 
def minimumAbsoluteDifference(arr):
    minabs = 2*10e10
    for i in range( len( arr )-1 ):
        num_1 = arr[i]
        for j in range(i+1, len(arr) ):
            num_2 = arr[j]
            new = abs(num_1-num_2)
            if new < minabs:
                minabs = new
    return minabs    

def minimumAbsoluteDifference2(arr):
    sorted_arr = sorted( arr )
    minabs = 2*10e10
    for i in range( len( sorted_arr )-1 ):
        new = abs( sorted_arr[i] - sorted_arr[i+1])
        if new < minabs:
            minabs = new
    return minabs                 