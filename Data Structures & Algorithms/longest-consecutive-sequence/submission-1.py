class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # need consecutive sequence aka element is 1 greater then previous element
        # loop at find starter values

        # set or hashmap

        num_set = set(nums)
        starters = []
        for num in num_set:
            if num-1 not in num_set:
                starters.append(num)

        max_len = 0
       
        # from starter find sequence length
        for starter in starters:

            counter = 1
            keep_counting = True
            next_value = starter

            while keep_counting:
                next_value += 1
                if next_value in num_set:
                    counter += 1
                else:
                    keep_counting = False

            if counter > max_len:
                max_len = counter

        return max_len

