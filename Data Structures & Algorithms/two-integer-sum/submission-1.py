class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stored = {}
        ans = []
        for index, element in enumerate(nums):
            # print(stored)
            other_num = target - element
            print(other_num)
            if other_num in stored:
                return [stored[other_num], index]
                # return ans
            stored[element] = index

        # return ans
        