player1 = input("Enter player1 name : ")
player2 = input("Enter player2 name : ")
print("Hi ",player1,",",player2,)
counter = 1
player1_score = 0
player2_score = 0
while True:
    print("Game : ",counter)
    print("Enter your choice\nType R for Rock\nType S for scissor\nType P for paper : ")
    input1 = input("Enter player1's choice : ")
    input2 = input("Enter player2's choice : ")
    if input1 == "Q" or input1 == "q" or input2 == "Q" or input2 == "q":
        break
    elif input1 == "R" or input1 == "r" and input2 == "S" or input2 == "s":
        print(player1,'You win!\n**********************')
        counter+=1
        player1_score+=1
    elif input1 == "S" or input1 == "s" and input2 == "R" or input2 == "r":
        print(player2, 'You win!\n**********************')
        counter += 1
        player2_score+=1
    elif input1 == "S" or input1 == "s" and input2 == "P" or input2 == "p":
        print(player1, 'You win!\n**********************')
        counter += 1
        player1_score+=1
    elif (input1 == "P" or input1 == "p" and input2 == "S" or input2 == "s"):
        print(player2, 'You win!\n**********************')
        counter += 1
        player2_score+=1
    elif (input1 == "P" or input1 == "p" and input2 == "R" or input2 == "r"):
        print(player1, 'You win!\n**********************')
        counter += 1
        player1_score+=1
    elif (input1 == "R" or input1 == "r" and input2 == "P" or input2 == "p"):
        print(player2, 'You win!\n**********************')
        counter += 1
        player2_score+=1
    else:
        print("Enter valid input")
if(player1_score > player2_score):
    print(player1,"wins with maximum score of : ",player1_score)
else:
    print(player2,"wins with maximum score of : ",player2_score)
print("Thanks for playing!")






