import random

def printboard(board):
    print("________________")
    print("|", board[0], "|", board[1], "|", board[2], "|", board[3], "|")
    print("________________")
    print("|", board[4], "|", board[5], "|", board[6], "|", board[7], "|")
    print("________________")
    print("|", board[8], "|", board[9], "|", board[10], "|", board[11], "|")
    print("________________")
    print("|", board[12], "|", board[13], "|", board[14], "|", board[15], "|")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

def computer_turn():
    print("Its the computer's turn now! ")
    rough = []
    rough = available.copy()
    rough[:] = (value for value in rough if value != "-")
    comp_choice = random.choice(rough)
    for i in range(len(available)):
        i = comp_choice
        available[i - 1] = "-"
        board[i - 1] = "O"
        printboard(board)
        print("The computer has chosen the number", comp_choice)
        print("The available positions now are:", available)
        for j in range(16):
          if board[0]=="O" and board[1]=="O" and board[2]=="O" and board[3]=="O": 
            print("Uh oh! Computer wins.")
            quit()
            break
          if board[4]=="O" and board[5]=="O" and board[6]=="O" and board[7]=="O": 
            print("Uh oh! Computer wins.")
            quit()
            break
          if board[8]=="O" and board[9]=="O" and board[10]=="O" and board[11]=="O": 
            print("Uh oh! Computer wins.")
            quit()
            break
          if board[12]=="O" and board[13]=="O" and board[14]=="O" and board[15]=="O": 
            print("Uh oh! Computer wins.")
            quit()
            break
          if board[0]=="O" and board[4]=="O" and board[8]=="O" and board[12]=="O": 
            print("Uh oh! Computer wins.")
            quit()
            break
          if board[1]=="O" and board[5]=="O" and board[9]=="O" and board[13]=="O": 
            print("computer wins")
            quit()
            break
          if board[2]=="O" and board[6]=="O" and board[10]=="O" and board[14]=="O": 
            print("Uh oh! Computer wins.")
            quit()
            break
          if board[3]=="O" and board[7]=="O" and board[11]=="O" and board[15]=="O": 
            print("Uh oh! Computer wins.")
            quit()
            break
          if board[0]=="O" and board[5]=="O" and board[10]=="O" and board[15]=="O": 
            print("Uh oh! Computer wins.")
            quit()
            break
          if board[3]=="O" and board[6]=="O" and board[9]=="O" and board[12]=="O": 
            print("Uh oh! Computer wins.")
            quit()
            break
          if board[1]=="O" and board[6]=="O" and board[11]=="O": 
            print("Uh oh! Computer wins.")
            quit()
            break
          if board[2]=="O" and board[5]=="O" and board[8]=="O": 
            print("Uh oh! Computer wins.")
            quit()
            break
          if board[4]=="O" and board[9]=="O" and board[14]=="O": 
            print("Uh oh! Computer wins.")
            quit()
            break
          if board[7]=="O" and board[10]=="O" and board[13]=="O": 
            print("Uh oh! Computer wins.")
            quit()
            break
        break


def user_turn():
    print("Its your turn now! ")
    rough = []
    rough = available.copy()
    rough[:] = (value for value in rough if value != "-")
    user_input = int(input("Enter your choice (1-16): "))
    for i in range(len(available)):
        i = user_input
        available[i - 1] = "-"
        board[i - 1] = "X"
        printboard(board)
        print("The available positions now are:", available)
        for j in range(16):
          if board[0]=="X" and board[1]=="X" and board[2]=="X" and board[3]=="X": 
            print("Congratulations! You win.")
            quit()
            break
          if board[4]=="X" and board[5]=="X" and board[6]=="X" and board[7]=="X": 
            print("Congratulations! You win.")
            quit()
            break
          if board[8]=="X" and board[9]=="X" and board[10]=="X" and board[11]=="X": 
            print("Congratulations! You win.")
            quit()
            break
          if board[12]=="X" and board[13]=="X" and board[14]=="X" and board[15]=="X": 
            print("Congratulations! You win.")
            quit()
            break
          if board[0]=="X" and board[4]=="X" and board[8]=="X" and board[12]=="X": 
            print("Congratulations! You win.")
            quit()
            break
          if board[1]=="X" and board[5]=="X" and board[9]=="X" and board[13]=="X": 
            print("Congratulations! You win.")
            quit()
            break
          if board[2]=="X" and board[6]=="X" and board[10]=="X" and board[14]=="X": 
            print("Congratulations! You win.")
            quit()
            break
          if board[3]=="X" and board[7]=="X" and board[11]=="X" and board[15]=="X": 
            print("Congratulations! You win.")
            quit()
            break
          if board[0]=="X" and board[5]=="X" and board[10]=="X" and board[15]=="X": 
            print("Congratulations! You win.")
            quit()
            break
          if board[3]=="X" and board[6]=="X" and board[9]=="X" and board[12]=="X": 
            print("Congratulations! You win.")
            quit()
            break
          if board[1]=="X" and board[6]=="X" and board[11]=="X": 
            print("Congratulations! You win.")
            quit()
            break
          if board[2]=="X" and board[5]=="X" and board[8]=="X": 
            print("Congratulations! You win.")
            quit()
            break
          if board[4]=="X" and board[9]=="X" and board[14]=="X": 
            print("Congratulations! You win.")
            quit()
            break
          if board[7]=="X" and board[10]=="X" and board[13]=="X": 
            print("Congratulations! You win.")
            quit()
            break
        break

print("Welcome to Tic Tac Toe")
print("You will play as X")
print("The computer will play as O")
print("----------------------------")
first = ["user", "computer"]
available = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
board = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14",
    "15", "16"
]
winner = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16],
          [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16],
          [1, 6, 11, 16], [4, 7, 10, 13], [2, 7, 12], [3, 6, 9], [5, 10, 15],
          [8, 11, 14]]
first_turn = random.choice(first)

if first_turn == "user":
    print("You will go first!")
    print("The available positions are", available)
    user_input = int(input("Enter your choice (1-16): "))
    while True:
        if user_input not in available:
            print("---- Please enter a valid choice ! ----")
            break
        else:
            break
    for i in range(len(available)):
        i = user_input
        available[i - 1] = "-"
        board[i - 1] = "X"
        printboard(board)
        break

else:
    print("The computer will go first!")
    print("The available positions are", available)
    computer_choice = random.choice(available)
    for i in range(len(available)):
        i = computer_choice
        available[i - 1] = "-"
        board[i - 1] = "O"
        printboard(board)
        break

if first_turn == "user":
    for i in range(15):
        computer_turn()
        user_turn()
elif first_turn == "computer":
    for i in range(15):
        user_turn()
        computer_turn()
