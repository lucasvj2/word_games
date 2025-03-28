from common.tile import Tile
from typing import List, Tuple, Set
from common.trie import build_trie

def find_words(board: List[Tile], words: List[str]) -> List[Tuple[str, List[Tile]]]:
    def dfs(x: int, node, path: List[Tile], visited: Set[int]):
        word = ''.join(tile.letter for tile in path)
        if node.end_of_word:
            result.append((word, path[:]))
            node.end_of_word = False
            
        for nx in range(len(board)):
            if nx not in visited:
                next_tile = board[nx]
                next_char = next_tile.letter
                if next_char in node.children:
                    dfs(nx, node.children[next_char], path + [next_tile], visited | {nx})
    
    
    
    root = build_trie(words)
    result = []
    
    for i in range(len(board)):
        tile = board[i]
        char = tile.letter
        if char in root.children:
            dfs(i, root.children[char], [tile], {i})
            
    return result