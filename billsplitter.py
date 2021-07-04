# write your code here
import random

name = []
names = {}
print("Enter the number of friends joining (including you):")

num_friends = int(input())
if num_friends <= 0:
    print("No one is joining for the party")
else:
    print(" Enter the name of every friend (including you), each on a new line:")
    for i in range(num_friends):
        name.append(input())
    names = dict.fromkeys(name, 0)
    print("Final Bill:")
    bill = float(input())
    split = round((bill / num_friends), 2)
    for i in names:
        names[i] = split
    
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    choice = input()
    if choice != "Yes":
        print("No one is going to be lucky")
        print(names)
    else:
        winner = random.choice(name)
        n = num_friends - 1
        split = round((bill / n), 2)
        for i in names:
            if i == winner:
                names[i] = 0
            else :
                names[i] = split
 
        print(winner, "is the lucky one!")
        print(names)




 
