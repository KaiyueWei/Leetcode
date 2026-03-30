class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
    
class Solution:
    def buildTrie(self, words, root):
        if root == None:
            root = TrieNode()
        node = root
        for word in words:
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = word
            node = root
        return root
        
    def findWords(self, board, words):
        rows = len(board)
        cols = len(board[0])
        root = TrieNode()
        root = self.buildTrie(words, root)
        res = []
        def backtrack(r, c, node):
            if node.word:
                res.append(node.word)
                node.word = None
            if (r < 0 or r >= rows) or (c < 0 or c >= cols):
                return
            if board[r][c] not in node.children:
                return 
            cur = board[r][c]
            board[r][c] = "#"

            for r_off, c_off in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                backtrack(r+r_off, c+c_off, node.children[cur])
            board[r][c] = cur

            return 
        for i in range(rows):
            for j in range(cols):
                if board[i][j] in root.children:
                    backtrack(i, j, root)
        return res

            
            


        
        