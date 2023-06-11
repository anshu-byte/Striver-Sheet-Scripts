class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # better approach
        # sliding window
        # use a set to keep track of the characters in the window
        # use two pointers to keep track of the window
        # if the character at the right pointer is in the set, remove the character at the left pointer from the set and increment the left pointer
        # else, add the character at the right pointer to the set and increment the right pointer
        # keep track of the max length of the window
        # return the max length of the window
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # if len(s)==0:
        #     return 0
        # l,r = 0,0
        # maxLen = float('-inf')
        # chars = set()
        # for r in range(len(s)):
        #     if s[r] in chars:
        #         while l<r and s[r] in chars: # duplicates exists conditions
        #             chars.remove(s[l])
        #             l+=1
        #     chars.add(s[r])
        #     maxLen = max(maxLen,r-l+1)
        # return maxLen
    
        # best appraoch
        if len(s)==0:
            return 0
        d = {}
        l,r = 0,0
        maxLen = float('-inf')
        for r in range(len(s)):
            if s[r] not in d:
                d[s[r]] = r
            else:
                if d[s[r]]>=l:
                    l = d[s[r]] + 1
                d[s[r]] = r
            maxLen = max(maxLen,r-l+1)
        return maxLen
sol = Solution()
print(sol.lengthOfLongestSubstring("tmmzuxt"))