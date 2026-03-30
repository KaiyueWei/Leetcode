class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        d = self.root

        for c in word:
            if c not in d.children:
                d.children[c] = TrieNode()
            d = d.children[c]
        d.terminal = True


    def search(self, word: str) -> bool:
        tmp = self.root
        length = len(word)
        def dfs(node: TrieNode, index: int) -> bool:
            if index == length:
                return node.terminal
                
            c = word[index]
            if c in node.children:
                return dfs(node.children.get(c, None), index + 1)
            if c == '.':
                for key in node.children:
                    if dfs(node.children[key], index + 1):
                        return True
            return False
        return dfs(tmp, 0)






