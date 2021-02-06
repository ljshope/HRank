 
def fibonacci(n):
    arr = []
    arr.append(0)
    arr.append(1)
    if n < 2:
        result = arr[n]
    else:
        for i in range(2,n+1):
            arr.append(arr[i-1]+arr[i-2])
        result = arr[n]
    return result        
    
    