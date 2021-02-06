 
def checkMagazine(magazine, note):
    result = 'YES'
    mdict = dict()
    for word in magazine:
        if word in mdict.keys():
            mdict[ word ] +=1
        else:
            mdict[ word ] = 1
    ndict = dict()
    for word in note:
        if word in ndict.keys():
            ndict[ word ] +=1
        else:
            ndict[ word ] = 1
    for key in ndict.keys():
        if key in mdict.keys():
            if ndict[ key ] > mdict[key]:
                result = 'NO'
                break
        else:
            result = 'NO'
            break
    print( result )   
            
