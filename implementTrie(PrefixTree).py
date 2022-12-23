class TrieNode:
    
    def __init__(self):
        self.children = {};
        self.end = False;

class Trie(object):

    def __init__(self):
        self.root = TrieNode();

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root;
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode();
                node = node.children[char];
            else:
                node = node.children[char];
        node.end = True;

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root;
        n=len(word);
        for char in word:
            if char in node.children:
                node=node.children[char];
                n-= 1;
                if node.end == True and n==0 : return True;      
            else:
                return False;

    
    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root;
        if node.children:      
            for char in prefix:      
                if char in node.children:
                    node=node.children[char];                 
                else:
                    return False;
            return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)