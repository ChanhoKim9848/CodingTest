def findContentChildren(self, g: List[int], s: List[int]) -> int:
    
    if not len(s):
        return 0
    s.sort()
    g.sort()
    result=0
    i,j=0,0
    
    while i<len(g) and j<len(s):
        
        if g[i]<=s[j]:
            i+=1
            j+=1
            result+=1
        else:
            j+=1
    return result