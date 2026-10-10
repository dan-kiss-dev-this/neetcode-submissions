class Solution:

    def encode(self, strs: List[str]) -> str:
        coded = ""
        for s in strs:
            length_string = str(len(s))
            coded += length_string + "$" + s
        return coded

    def decode(self, s: str) -> List[str]:
        i_front = 0
        decode_array = []

        while i_front < len(s):
            # need to find a back pointer called j
            j_back = i_front
            while s[j_back] != "$":
                j_back += 1
            # here we exit while loop and know j_back = $ so now we grab the length
            # we can slice of grab the item in list
            # will use slice to prace better way

            # 2$hi3$you

            # need to explicity convert type as we are in string need int
            numberOfChars = int(s[i_front:j_back])

            decode_array.append(s[j_back + 1:j_back + 1 + numberOfChars])

            i_front = j_back + 1 + numberOfChars

        return decode_array
            
