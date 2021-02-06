
def twoStrings(s1, s2):
    ans = 'NO'
    s1 = set( s1 )
    s2 = set( s2 )
    for s in s1:
        for ss in s2:
            if s == ss:
                ans = 'YES'
                break
    return ans        
    