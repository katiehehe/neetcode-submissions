class Node:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.head = Node()

    def addWord(self, word: str) -> None:
        curr = self.head
        for c in word:
            if not curr.children[ord(c) - ord('a')]:
                curr.children[ord(c) - ord('a')] = Node()
            curr = curr.children[ord(c) - ord('a')]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def helper(curr, i):
            if not curr:
                return False
            if i == len(word):
                return curr.endOfWord
            if word[i] == '.':
                return any([helper(curr.children[x], i + 1) for x in range(26)])
            if not curr.children[ord(word[i]) - ord('a')]:
                return False
            return helper(curr.children[ord(word[i]) - ord('a')], i + 1)
        return helper(self.head, 0)