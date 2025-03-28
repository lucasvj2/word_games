from anagrams.solver import find_words
from anagrams.find_grid import get_grid
from anagrams.find_enter import get_enter
from anagrams.mouse import click_path

def main():
    with open("common/wordlist.txt", "r") as file:
        words = [line.strip().upper() for line in file]
    print("finding grid...")
    grid = get_grid()
    enter = get_enter()
    if grid is None:
        print("❌ Could not detect grid.")
        return
    if enter is None:
        print("❌ Could not detect enter.")
        return
    print("found grid!")
    print("solving...")
    found_words = find_words(grid, words)
    print("solved!")
    points = 0
    for (word, path) in found_words:
        l = len(word)
        if l == 3:
            points += 100
        elif l == 4:
            points += 400
        elif l == 5:
            points += 800
        elif l == 6:
            points += 1400
        elif l == 7:
            points += 1800
        elif l >= 8:
            points += 2200
            
    print(f"✅ Points: {points}")
    
    # if points <= 200000:
    #     return

    for (word, path) in found_words:
        path.append(enter)
        click_path(path)

if __name__ == "__main__":
    main()
