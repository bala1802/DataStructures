"""
Author: bala1802@live.com
LeetCode Problem: https://leetcode.com/problems/word-search-ii/

GitHub: https://github.com/bala1802
"""

class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        currentNode = self

        for eachCharacter in word:
            if eachCharacter not in currentNode.children[eachCharacter]:
                currentNode.children[eachCharacter] = TrieNode()
            currentNode = currentNode.children[eachCharacter]
        
        currentNode.isWord = True

class Solution:

    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()

        for eachWord in words:
            root.addWord(word=eachWord)
        
        ROWS, COLUMNS = len(board), len(board[0])
        result, visitedNodes = set(), set()

        def dfs(rowAxis, columnAxis, node, word):
            if ((rowAxis < 0) or (columnAxis < 0) or (rowAxis == ROWS) or (columnAxis == COLUMNS) or 
                ((rowAxis, columnAxis) in visitedNodes) or board[rowAxis][columnAxis] not in node.children):
                return

            visitedNodes.add((rowAxis, columnAxis))
            node = node.children[board[rowAxis][columnAxis]]
            word += board[rowAxis][columnAxis]

            if node.isWord:
                result.add(word)

            dfs(rowAxis=rowAxis-1, columnAxis=columnAxis, node=node, word=word)
            dfs(rowAxis=rowAxis+1, columnAxis=columnAxis, node=node, word=word)
            dfs(rowAxis=rowAxis, columnAxis=columnAxis-1, node=node, word=word)
            dfs(rowAxis=rowAxis, columnAxis=columnAxis+1, node=node, word=word)
        
            visitedNodes.remove((rowAxis, columnAxis))


        for rowAxis in range(ROWS):
            for columnAxis in range(COLUMNS):
                dfs(rowAxis=rowAxis, columnAxis=columnAxis, node=root, word="")

        return result