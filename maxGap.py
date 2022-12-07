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