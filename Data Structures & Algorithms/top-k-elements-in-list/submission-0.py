class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # how did you think of it?
        # you had a brute force to count occurances, your issue was
        #how to loop and find the most common values=lots of extra logic
        # you could do a heap logic but its extra and n log n time

        # different way to think if it is use the count as in index in an array
        # then you keep the number in an array associated with the count

        count = {}
        freq = [ [] for _ in range(len(nums)+1)]

        for n in nums:
            count[n]= count.get(n, 0) + 1

        for n, c in count.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                # note the k is k most frequen elements
                if len(res) == k:
                    return res

