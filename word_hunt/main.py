from word_hunt.solver import find_words
from word_hunt.find_grid import get_grid
from word_hunt.mouse import drag_path

def main():
    with open("common/wordlist.txt", "r") as file:
        words = [line.strip().upper() for line in file]
    print("finding grid...")
    grid = get_grid()
    if grid is None:
        print("❌ Could not detect grid.")
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
        drag_path(path)

if __name__ == "__main__":
    main()
