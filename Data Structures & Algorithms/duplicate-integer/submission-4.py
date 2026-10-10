class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for num in nums:
            if counter.get(num):
                return True
            else:
                counter[num] = 1
        return False