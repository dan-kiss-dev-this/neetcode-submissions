class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                # mean sum too big so the right pointer shift to left
                r -= 1
            elif curSum < target:
                # mean sum too small so move right pointer up 1 index
                l += 1
            else:
                # we know curSum == target in this condition
                return [l + 1, r + 1]