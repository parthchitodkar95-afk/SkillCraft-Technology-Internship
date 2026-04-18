# ============================================
#   SkillCraft Technology - Internship Task 03
#   Sudoku Solver
#   Author: Parth Jivan Chitodkar
# ============================================

def print_board(board):
    print("\n+" + "-"*7 + "+" + "-"*7 + "+" + "-"*7 + "+")
    for i in range(9):
        row = "|"
        for j in range(9):
            if board[i][j] == 0:
                row += "  . "
            else:
                row += f"  {board[i][j]} "
            if (j + 1) % 3 == 0:
                row += "|"
        print(row)
        if (i + 1) % 3 == 0:
            print("+" + "-"*7 + "+" + "-"*7 + "+" + "-"*7 + "+")


def is_valid(board, row, col, num):
    # Check row
    if num in board[row]:
        return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False

    return True


def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True


# ---- Predefined Sudoku Puzzles ----
puzzles = {
    "1": {
        "name": "Easy",
        "board": [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]
    },
    "2": {
        "name": "Medium",
        "board": [
            [0, 0, 0, 2, 6, 0, 7, 0, 1],
            [6, 8, 0, 0, 7, 0, 0, 9, 0],
            [1, 9, 0, 0, 0, 4, 5, 0, 0],
            [8, 2, 0, 1, 0, 0, 0, 4, 0],
            [0, 0, 4, 6, 0, 2, 9, 0, 0],
            [0, 5, 0, 0, 0, 3, 0, 2, 8],
            [0, 0, 9, 3, 0, 0, 0, 7, 4],
            [0, 4, 0, 0, 5, 0, 0, 3, 6],
            [7, 0, 3, 0, 1, 8, 0, 0, 0],
        ]
    },
    "3": {
        "name": "Hard",
        "board": [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 3, 0, 8, 5],
            [0, 0, 1, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 5, 0, 7, 0, 0, 0],
            [0, 0, 4, 0, 0, 0, 1, 0, 0],
            [0, 9, 0, 0, 0, 0, 0, 0, 0],
            [5, 0, 0, 0, 0, 0, 0, 7, 3],
            [0, 0, 2, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 4, 0, 0, 0, 9],
        ]
    }
}


# ---- Main Program ----
print("=" * 45)
print("   SkillCraft Technology - Task 03")
print("           Sudoku Solver")
print("=" * 45)

while True:
    print("\nSelect a Puzzle:")
    print("  1. Easy Puzzle")
    print("  2. Medium Puzzle")
    print("  3. Hard Puzzle")
    print("  4. Exit")
    print("-" * 45)

    choice = input("Enter your choice (1/2/3/4): ").strip()

    if choice == '4':
        print("\nThank you! SkillCraft Technology - Task 03 Complete!")
        break

    if choice not in ['1', '2', '3']:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")
        continue

    puzzle = puzzles[choice]
    board = [row[:] for row in puzzle["board"]]  # copy the board

    print(f"\n{puzzle['name']} Puzzle - Unsolved:")
    print("(0 represents empty cells)")
    print_board(board)

    input("\nPress Enter to solve the puzzle...")

    if solve(board):
        print(f"\n{puzzle['name']} Puzzle - SOLVED!")
        print_board(board)
        print("\nSudoku solved successfully using Backtracking Algorithm!")
    else:
        print("\nNo solution exists for this puzzle!")

    print("\n" + "-" * 45)
    again = input("Solve another puzzle? (Y/N): ").strip().lower()
    if again != 'y':
        print("\nThank you! SkillCraft Technology - Task 03 Complete!")
        break