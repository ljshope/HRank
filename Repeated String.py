

def repeatedString(s, n):
    counter = 0
    for str in s:
        if str == 'a':
            counter += 1
    number = counter*(n//len(s))
    r = 0
    i = 0
    for str in s:
        i += 1
        if str == 'a' and i <= n%len(s):
            r += 1 
        print( str, r, i)
    return int(number//1 + r)        
        