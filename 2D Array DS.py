
def rotLeft(a, d):
     long = a+a
     dd = d%len(a)
     result = []
     for i in range( 0, len(a) ):
         result.append(long[i+d])
     return result    
