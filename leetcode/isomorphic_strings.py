class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        map_dict = {}
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] in map_dict.keys():
                    if t[i] != map_dict[s[i]]:
                        return False
                else:
                    if t[i] in map_dict.values():
                        return False
                    else:
                        map_dict[s[i]] = t[i]
        
        return True
            
        