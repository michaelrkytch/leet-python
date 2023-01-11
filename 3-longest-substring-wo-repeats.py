# Two-pointer solution

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        start, end = 0, 0
        best = 0
        cur_chars = set()
        while end < n:  # outer loop increments the end of the window
            next_char = s[end]
            while next_char in cur_chars:  # Advance the start of the window until it only contains unique chars
                cur_chars.discard(s[start])
                start += 1

            # now add in the char at the end of the window
            cur_chars.add(next_char)
            if (end - start + 1) > best:  # we have a new longer substring
                best = end - start + 1

            end += 1

        return best
