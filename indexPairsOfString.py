class TrieNode():
    def __init__(self):
        self.children = {};
        self.end = False;

class Trie():
    def __init__(self):
        self.root = TrieNode();

    def insert(self,word):
        node = self.root;
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode();
                node = node.children[char];
            else:
                node = node.children[char];
        node.end = True;

class Solution:
    def indexPairs(self, text, words):
        result = [];
        mytrie = Trie();
       
        for word in words:
            mytrie.insert(word);

        for i in range(len(text)) :
            node = mytrie.root;
            j = i;
            while j < len(text) and text[j] in node.children:
                node = node.children[text[j]];
                if node.end == True:
                    result.append([i,j]);
                j+= 1;
        return result


