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

    def search(self, word: str) -> bool:
        def dfs(index: int, node: dict) -> bool:
            cur = node
            for i in range(index, len(word)):
                c = word[i]
                if c == '.':
                    # If we hit '.', try all possible child nodes recursively
                    for child_char in cur:
                        if child_char != '*' and dfs(i + 1, cur[child_char]):
                            return True
                    return False # If none of the paths worked
                else:
                    if c not in cur:
                        return False
                    cur = cur[c]
            return '*' in cur

        return dfs(0, self.trie)
