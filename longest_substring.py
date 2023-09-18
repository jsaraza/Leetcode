class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_size = 0
        curr_size = 0
        i = 0

        while(i < len(s)):
            if s[i] not in seen:
                seen[s[i]] = i
                curr_size += 1
            else:
                i = seen[s[i]] + 1
                seen.clear()
                seen[s[i]] = i
                if curr_size > max_size:
                    max_size = curr_size
                curr_size = 1
            i += 1
        
        if curr_size > max_size:
            max_size = curr_size

        return max_size

                
