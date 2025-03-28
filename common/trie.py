class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

def build_trie(words):
    root = TrieNode()
    for word in words:
        node = root
        for char in word.upper():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True
    return root
