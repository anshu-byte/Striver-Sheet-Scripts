class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        temp = ""
        for c in s:
            if c != " ":
                temp += c
            elif temp != "":
                res.append(temp)
                temp = ""
        if temp != "":
            res.append(temp)
        reversed_words = ""
        for i in range(len(res) - 1, -1, -1):
            reversed_words += res[i]
            if i != 0:
                reversed_words += " "
        return reversed_words
