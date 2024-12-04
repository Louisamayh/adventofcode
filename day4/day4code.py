# Load the word search from the input file
with open("inputday4.txt") as file:
    matrix = [list(line.strip()) for line in file]  # Convert each line into a list of characters

def count_xmas(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    target = "XMAS"
    target_len = len(target)
    count = 0

    # Helper function to check bounds and match the target string
    def match(r, c, dr, dc):
        for i in range(target_len):
            nr, nc = r + i * dr, c + i * dc
            if not (0 <= nr < rows and 0 <= nc < cols) or matrix[nr][nc].lower() != target[i].lower():
                return False
        return True

    # Iterate through the matrix
    for r in range(rows):
        for c in range(cols):
            # Check all directions
            # Right (horizontal)
            if match(r, c, 0, 1):  # → Right
                count += 1
            if match(r, c, 0, -1):  # ← Left
                count += 1
            # Down (vertical)
            if match(r, c, 1, 0):  # ↓ Down
                count += 1
            if match(r, c, -1, 0):  # ↑ Up
                count += 1
            # Diagonals
            if match(r, c, 1, 1):  # ↘ Down-Right
                count += 1
            if match(r, c, 1, -1):  # ↙ Down-Left
                count += 1
            if match(r, c, -1, 1):  # ↗ Up-Right
                count += 1
            if match(r, c, -1, -1):  # ↖ Up-Left
                count += 1

    return count

# Count 'XMAS' in the given word search matrix
result = count_xmas(matrix)
print(f"The string 'XMAS' appears {result} times.")
