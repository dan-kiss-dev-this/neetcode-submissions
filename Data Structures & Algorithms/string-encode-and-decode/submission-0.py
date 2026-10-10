class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            length = str(len(s))
            res += length + "#" + s
        print(res)
        return res
        
    # sample is 4#same3#fun
    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            # j is the end of the string pointer
            j = i
            while s[j] != "#":
                j += 1
            # per sample str[0:1] returns a slice which has the value of 4. note explicity type conversion to int
            # 
            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            res.append(word)
            i = j + 1 + length
        return res
