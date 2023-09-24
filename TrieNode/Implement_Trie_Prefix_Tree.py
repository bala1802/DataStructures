class TrieNode:
    
    def __init__(self):
        self.children = {} #children["a"] = TrieNode()
        self.endOfWord = False #Flag to say whether a this point, the characters form a valid word or not

class Trie:

    def __init__(self):
        """
        Initializing the data structure here
        """

        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie
        """

        currentNode = self.root

        for eachCharacter in word:
            if eachCharacter not in currentNode.children:
                #If none of the immediate children doesn't has the 'eachCharacter' as a letter, create a new Node
                currentNode.children[eachCharacter] = TrieNode()
            #When the eachCharacter is available as a Children, set the next node as the currentNode
            currentNode = currentNode.children[eachCharacter] 
        
        #At the end of the word, set that particular node as End of the word as True
        currentNode.endOfWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the Trie
        """
        
        currentNode = self.root

        for eachCharacter in word:
            #Check whether the character is present in the node
            if eachCharacter not in currentNode.children:
                return False
            #If the eachCharacter is present move to the next node
            currentNode = currentNode.children[eachCharacter]
        
        return currentNode.endOfWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if any word is in the Trie that starts with the given prefix
        """
        
        currentNode = self.root

        for eachCharacter in prefix:
            #Check whether the character is present in the node
            if eachCharacter not in currentNode.children:
                return False
            #If the eachCharacter is present move to the next node
            currentNode = currentNode.children[eachCharacter]
        
        return True
    


