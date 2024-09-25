# You are given an array words of size n consisting of non-empty strings.
# We define the score of a string term as the number of strings words[i] such that term is a prefix of words[i].
# For example, if words = ["a", "ab", "abc", "cab"], then the score of "ab" is 2, since "ab" is a prefix of both "ab" and "abc".
# Return an array answer of size n where answer[i] is the sum of scores of every non-empty prefix of words[i].
# Note that a string is considered as a prefix of itself.
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0  # This will store the number of times this prefix appears


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1  # Increment the count for the current prefix

    def get_prefix_score(self, word):
        node = self.root
        score = 0
        for char in word:
            if char in node.children:
                node = node.children[char]
                score += node.count  # Add the count of the current prefix to the score
        return score


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()

        # Step 1: Insert all words into the Trie
        for word in words:
            trie.insert(word)

        # Step 2: Calculate prefix scores for each word
        result = []
        for word in words:
            result.append(trie.get_prefix_score(word))

        return result
