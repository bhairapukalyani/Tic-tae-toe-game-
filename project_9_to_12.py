#9 Tic Tae Toe
import random
board = [' '] * 9
def display():
    print("\nCurrent Board:")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]} ")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
w = lambda p: any(all(board[i] == p for i in line) for line in [
    [0,1,2], [3,4,5], [6,7,8],
    [0,3,6], [1,4,7], [2,5,8],
    [0,4,8], [2,4,6]
])
for turn in range(5):
    display()
    move = int(input("Enter your move (0-8): "))
    if board[move] != ' ':
        print("That spot is taken! Try again.")
        continue
    board[move] = 'X'
    if w('X'):
        display()
        print("🎉 You win!")
        break
    if ' ' not in board:
        display()
        print("It's a tie!")
        break
    computer_choice = random.choice([i for i in range(9) if board[i] == ' '])
    board[computer_choice] = 'O'
    if w('O'):
        display()
        print("💻 Computer wins!")
        break
else:
    display()
    print("It's a tie!")
