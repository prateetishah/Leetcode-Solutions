"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.



Example 1:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.


Constraints:

1 <= nums.length <= 105
-2^31 <= nums[i] <= 2^31 - 1


"""


def firstMissingPositive(self, nums: List[int]) -> int:
    for i in range(len(nums)):
        target = nums[i]
        while 0 < target < len(nums) and target != nums[target - 1]:
            nums[target - 1], nums[i] = nums[i], nums[target - 1]
            target = nums[i]
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    return len(nums) + 1