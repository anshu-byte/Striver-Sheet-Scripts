from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        smallest_len = min(len(s) for s in strs)

        result = ""
        char_index = 0
        prefix_found = True

        while prefix_found and char_index < smallest_len:
            current_char = strs[0][char_index]

            for i in range(1, len(strs)):
                if strs[i][char_index] != current_char:
                    prefix_found = False
                    break

            if prefix_found:
                result += current_char

            char_index += 1

        return result
