'''
Difficulty : Medium

longest substring without repeating characters
Just reference from https://www.youtube.com/watch?v=sUicrnHwA0s
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subList = {}
        cur_subList_start = 0
        cur_len = 0
        longest = 0

        for i, letter in enumerate(s):
            print(letter)
            #
            if letter in subList and subList[letter] >= cur_subList_start:
                print(cur_subList_start)
                cur_subList_start = subList[letter]
                cur_len = i - subList[letter]
                subList[letter] = i
            else:
                subList[letter] = i 
                print(subList[letter])
                cur_len += 1
                if cur_len > longest:
                    longest = cur_len

        return (longest)

sol = Solution()
sol.lengthOfLongestSubstring("dvdf")
