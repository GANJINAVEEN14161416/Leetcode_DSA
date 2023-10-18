class Node:
    def __init__(self):
        self.children={}
        self.end=False# /think box by striver
class Trie:

    def __init__(self):
        self.reference=Node()#// getting that reference
        

    def insert(self, word: str) -> None:
        current=self.reference
        for w in word:
            if w not in current.children:
                current.children[w]=Node()
            current=current.children[w]
        current.end=True        

    def search(self, word: str) -> bool:
        current=self.reference
        for w in word:
            if w not in current.children:
                return False
            current=current.children[w]
        return current.end
        

    def startsWith(self, prefix: str) -> bool:
        current=self.reference
        for w in prefix:
            if w not in current.children:
                return False
            current=current.children[w]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)