class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        d = self.trie

        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d['*'] = '*'


    def search_rec(self, node: dict, word: str, index: int, length: int) -> bool:
        if node == None:
            return False
        if index == length:
            if '*' in node:
                return True
            else:
                return False
        c = word[index]
        if c in node:
            print(c)
            return self.search_rec(node.get(c, None), word, index + 1, length)
        if c == '.':
            for key in node:
                if key == '*':
                    continue
                if self.search_rec(node.get(key, None), word, index + 1, length):
                    return True
        return False 



    def search(self, word: str) -> bool:
        d = self.trie

        return self.search_rec(d, word, 0, len(word))


