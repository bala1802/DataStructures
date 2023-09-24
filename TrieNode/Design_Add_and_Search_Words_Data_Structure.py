class TrieNode:

    def __init__(self):

        """
        Initializing the data structure Trie
        """

        self.children = {} #a: TrieNode
        self.word = False

class WordDictionary:
    
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:

        """
        Adding a word to the tree
        """
        curr = self.root

        for eachCharacter in word:
            if eachCharacter not in curr.children:
                """
                If the "eachCharacter" is not present in the children (`children` is the dictionary),
                    - Initialize an empty TrieNode for that particular character (`eachCharacter`)
                Then, update the initialized TrieNode as the recent current node
                """
                curr.children[eachCharacter] = TrieNode()
            curr = curr.children[eachCharacter]
        #Set the Current word at that particular node as True, will be a flag to say that the word searched is present
        curr.word = True

    def search(self, word: str) -> str:
        
        """
        Search a word - `word`
        """
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                
                eachCharacter = word[i]
                if eachCharacter == ".":
                    for child in curr.children.values():
                        if dfs(j=i+1, root=child):
                            return True
                    return False
                else:
                    if eachCharacter not in curr.children:
                        return False
                    curr = curr.children[eachCharacter]
            return curr.word
        
        return dfs(j=0, root=self.root)

wd = WordDictionary()

wd.addWord("test")
wd.addWord("twist")
wd.addWord("pinch")
print(wd.search(word="pinch"))
print(wd.search(word=".est"))
print(wd.search(word=""))
print(wd.search(word="hear"))
print(wd.search(word="pin"))