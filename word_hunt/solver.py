from typing import List, Set, Tuple
from common.tile import Tile
from common.trie import build_trie

def find_words(board: List[List[Tile]], words: List[str]) -> List[Tuple[str, List[Tile]]]:
    def dfs(x: int, y: int, node, path: List[Tile], visited: Set[Tuple[int, int]]):
        word = ''.join(tile.letter for tile in path)
        if node.end_of_word:
            result.append((word, path[:]))
            node.end_of_word = False

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) not in visited:
                    next_tile = board[nx][ny]
                    next_char = next_tile.letter
                    if next_char in node.children:
                        dfs(nx, ny, node.children[next_char], path + [next_tile], visited | {(nx, ny)})

    root = build_trie(words)
    result = []

    for i in range(4):
        for j in range(4):
            tile = board[i][j]
            char = tile.letter
            if char in root.children:
                dfs(i, j, root.children[char], [tile], {(i, j)})

    return result
