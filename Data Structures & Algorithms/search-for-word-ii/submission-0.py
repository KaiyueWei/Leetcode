class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None   # store full word at terminal

class Solution:
    def buildTrie(self, words):
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = word
        return root

    def findWords(self, board, words):
        rows, cols = len(board), len(board[0])
        root = self.buildTrie(words)
        res = set()

        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return

            nxt = node.children[char]

            if nxt.word:
                res.add(nxt.word)
                nxt.word = None  # de-duplicate

            board[r][c] = '#'
            for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, nxt)
            board[r][c] = char

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)

        return list(res)

        
        