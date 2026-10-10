class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of anagrams

        # grabbing word
        for s in strs:
            # need to grab the letter
            # make array that will hold letter count so each char goes to one section of the
            # array
            count = [0]*26

            # going to the char in the string, s from above
            for c in s:
                # note the ord() will look at the universal unicode database and returns the
                # position of c character note ord("a") is 97 so we do the ord(c)-ord('a') so
                # if you have a the postion is 0 if you have b its ord('b')-ord('a')= index 1.
                # you have an array of 26 values of 0, when you match the index,
                # you increment the count by 1
                # [1,1,0,0,0,0,0,0,0,0,0.....]
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())