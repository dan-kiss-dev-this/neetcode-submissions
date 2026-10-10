class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # so I need the indices of the 2 numbers that add to target
        # do for loop and find number?
        # isn't a hash map easier here?

        #naive is like a for loop with a while under it
        for index, n in enumerate(numbers):
            pointer = 1
            while(pointer < len(numbers)):
                if n + numbers[pointer] == target:
                    return [index + 1, pointer + 1]
                pointer += 1