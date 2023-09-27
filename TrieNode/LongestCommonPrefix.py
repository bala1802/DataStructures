class TrieNode:

    """
    Initializing the TrieNode object
    """

    def __init__(self):
        self.children = {}
        self.numberOfChild = 0
        self.endOfWord = False
    
class Solution:

    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        """
        Adding word to the Trie
        """

        currentNode = self.root

        for eachCharacter in word:
            if eachCharacter not in currentNode.children:
                currentNode.children[eachCharacter] = TrieNode()
                currentNode.numberOfChild += 1
            currentNode = currentNode.children[eachCharacter]
        
        currentNode.endOfWord = True

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        for eachWord in strs:
            self.addWord(word=eachWord)
        
        currentNode = self.root
        result = ""

        while currentNode and currentNode.numberOfChild == 1 and not currentNode.endOfWord:
            
            for eachChildren in currentNode.children:
                result += eachChildren
                currentNode = currentNode.children[eachChildren]
                break
        
        return result

if __name__ == "__main__":
    solution = Solution()
    result = solution.longestCommonPrefix(["tier", "treat", "twist"])
    print(result)