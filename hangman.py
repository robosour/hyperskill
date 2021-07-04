import random

print("H A N G M A N")
print('Type "play" to play the game, "exit" to quit:')
menu = input()

if menu != "exit" and menu != "play":
    print('Type "play" to play the game, "exit" to quit:')
    
answers = ['python', 'java', 'kotlin', 'javascript']
wrong = []
answer = random.choice(answers)
length = ("-" * (len(answer)))
count = 8
board = list(length)
if menu == "play":
    while count > 0:
        print()
        print("".join(board))
        letter = input("Input a letter: ")
    
        if len(letter) != 1:
            print("You should input a single letter")
            continue
        if not letter.islower():
            print("Please enter a lowercase English letter")
            continue
        if letter in wrong:
            print("You've already guessed this letter")
            continue
        wrong.append(letter)

        if letter in board:
            print("No improvements")
        if letter in answer:

            c = answer.count(letter)
            n = answer.find(letter)
            board[n] = letter
            loop = 1

            while loop < c:
                b = answer.find(letter, n + 1)
                board[b] = letter
                loop += 1
            loop = 1
        else:
            print("That letter doesn't appear in the word")
            count -= 1
        
            if ("".join(board)) == answer:
                print("""You guessed the word!
    You survived!""")
                break

        if ("".join(board)) == answer:
            print("""You guessed the word!
    You survived!""")
            break
    if (("".join(board)) != answer) and count == 0:
        print("You lost!")
