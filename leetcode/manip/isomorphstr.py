class Solution(object):
    def isIsomorphic(self, s, t):
        map1 = {}  # s → t
        map2 = {}  # t → s
        
        for c1, c2 in zip(s, t):
            # check forward mapping
            if c1 in map1:
                if map1[c1]!=c2:
                    return False
                continue
            if c2 in map2:
                if map2[c2]!=c1:
                    return False
                continue
            map1[c1]=c2
            map2[c2]=c1
            # check reverse mapping
            # add mappings if not present
        
        return True