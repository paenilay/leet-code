'''
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

Eg 1 
Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.

Eg 2
Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
'''


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if (len(nums) < 2):
            return 0
        else:
            maxDiff = 0
            nums_sorted = sorted(nums)
            print(nums_sorted)
            for i in range (0,len(nums_sorted)-1):
                 if ( nums_sorted[i+1] - nums_sorted[i] ) > maxDiff:
                        maxDiff = nums_sorted[i+1] - nums_sorted[i]
        return maxDiff
