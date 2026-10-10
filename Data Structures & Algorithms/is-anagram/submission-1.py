class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for element in t:
            t_dict[element] = t_dict.get(element, 0) + 1

        for element in s:
            s_dict[element] = s_dict.get(element,0)+1

        for key in s_dict:
            if s_dict[key] != t_dict.get(key,0):
                return False

        return True
        
            

        
