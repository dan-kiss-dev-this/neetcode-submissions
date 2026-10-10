class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stored = {}
        ans = []
        for index, element in enumerate(nums):
            other_num = target - element
            if other_num in stored:
                ans = [stored[other_num], index]
                return ans
            stored[element] = index

        return ans
        