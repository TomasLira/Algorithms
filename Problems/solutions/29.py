from typing import List
from collections import deque
# INCOMPLETE
#https://leetcode.com/problems/word-ladder/solutions/346920/python3-breadth-first-search/

# Inneficient solution: comparing all the words with each other in O(n)
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def compare_strings(s1, s2):
            count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    count += 1
            return count == 1

        if endWord not in wordList:
            return 0

        wordList = set(wordList)  
        wordList.add(beginWord)
        graph = {word: [] for word in wordList}

        for word1 in wordList:
            for word2 in wordList:
                if compare_strings(word1, word2):
                    graph[word1].append(word2)
        
        queue = deque([beginWord])
        visited = set([beginWord])
        level = 1 
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return level
                for adj_word in graph[word]:
                    if adj_word not in visited:
                        visited.add(adj_word)
                        queue.append(adj_word)
            level += 1
        return 0