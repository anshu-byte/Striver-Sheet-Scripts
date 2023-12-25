class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def count_chars(string):
            char_count = {}
            for char in string:
                char_count[char] = char_count.get(char, 0) + 1
            return char_count

        count_s = count_chars(s)
        count_t = count_chars(t)

        return count_s == count_t
