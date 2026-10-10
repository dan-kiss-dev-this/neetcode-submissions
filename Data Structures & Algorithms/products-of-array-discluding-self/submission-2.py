class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        holder = 1
        for i, element in enumerate(nums):
            for i2, element2 in enumerate(nums):
                if i2 != i:
                    # make the holder value for an index
                    holder *= nums[i2]
            # in parent loop add the holder
            output.append(holder)
            holder = 1
        return output
            
