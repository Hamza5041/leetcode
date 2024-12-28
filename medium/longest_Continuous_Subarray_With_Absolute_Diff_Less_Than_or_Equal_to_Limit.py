from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len(nums) == 1:
            return 1 if nums[0] - nums[0] <= limit else 0
        behind = 0
        ahead = 0
        largestSubArray = 0

        while behind <= ahead < len(nums):
            if abs(nums[ahead] - nums[behind]) <=limit:
                ahead +=1
                largestSubArray = (ahead+1) - (behind+1) if (ahead+1) - (behind+1)  > largestSubArray else largestSubArray
            elif abs(nums[ahead] - nums[behind]) > limit:
                behind += 1
        return largestSubArray


if __name__ == '__main__':
    test = Solution()
    testList = [10,1,2,4,7,2]
    limit = 5
    result = test.longestSubarray(testList, limit)
    assert result == 4, "result was: " + str(result)



