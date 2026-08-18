class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Inputs: Array & integer
# Output: a pair of indices
# Edge cases: empty array, no pair, multiple pairs

# loop through both arrays
# check if the sum of the two indices is equal to the target
# if so, return the indices

        seen = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            seen[nums[i]] = i