from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            word, level = queue.popleft()

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == word[i]:
                        continue

                    newWord = word[:i] + c + word[i + 1 :]
                    if newWord in wordSet and newWord not in visited:
                        if newWord == endWord:
                            return level + 1
                        queue.append((newWord, level + 1))
                        visited.add(newWord)
        return 0
