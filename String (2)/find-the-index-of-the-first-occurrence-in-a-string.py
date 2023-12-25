class Solution:
    def kmpSearch(self, text, pattern):
        n, m = len(text), len(pattern)
        if m > n:
            return -1

        if m == n:
            if text == pattern:
                return 0
            else:
                return -1

        lps = self.computeLPSArray(pattern)
        j, i = 0, 0

        while i < n:
            if pattern[j] == text[i]:
                i += 1
                j += 1
            if j == m:
                return i - j
            elif i < n and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1

    def computeLPSArray(self, pattern):
        length = 0
        i = 1
        m = len(pattern)
        lps = [0] * m

        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def strStr(self, haystack: str, needle: str) -> int:
        return self.kmpSearch(haystack, needle)
