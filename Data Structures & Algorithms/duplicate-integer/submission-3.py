class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checker = {}
        for index, element in enumerate(nums):
            if element not in checker:
                checker[element] = index
            else:
                return True
        
        return False