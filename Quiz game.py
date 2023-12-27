#Welcome
print("Welcome to the simple quiz game")

#chances
chance = 1
print("You will have", chance ,"Chance to answer correctly. \n Please put the alphabets of the answer \n")

#score
score=0

#question 1

question_1 = print(" 1) Who became the first Chief Minister of Maharashtra in 1960? \n a. Vasantrao Naik \n b. Yashwantrao Chavan \n c. Vasantdada Patil \n d. Sharad Pawar \n")
answer_1 ="b"

for i in range(chance):
    answer = input("Answer : ")
    if (answer.lower() == answer_1):
        print("Correct ! Good Job \n")
        score = score + 1
        break
    else:
        print("Incorrect! \n")
        print("The correct answer is ", answer_1, "\n\n ")




#question 2

question_2 = print(" 2) Which of the following places in Maharashtra is well-known for its sarees? \n a. Jalgaon \n b. Paithan \n c. Sangli \n d. Alibagh \n")
answer_2 ="b"

for i in range(chance):
    answer = input("Answer : ")
    if (answer.lower() == answer_2):
        print("Correct ! Good Job \n")
        score = score + 1
        break
    else:
        print("Incorrect! \n")
        print("The correct answer is ", answer_2, "\n\n ")




#question 3

question_3 = print(" 3) Which is the largest district of Maharashtra in terms of area? \n a. Amaravati \n b. Nagpur \n c. Sangli \n d. Ahmednagar\n")
answer_3 ="d"

for i in range(chance):
    answer = input("Answer : ")
    if (answer.lower() == answer_3):
        print("Correct ! Good Job \n")
        score = score + 1
        break
    else:
        print("Incorrect! \n")
        print("The correct answer is ", answer_3, "\n\n ")




#question 4

question_4 = print(" 4) How many districts does Maharashtra have as of 2023? \n a. 34 \n b. 35 \n c. 36 \n d. 37 \n")
answer_4 ="c"

for i in range(chance):
    answer = input("Answer : ")
    if (answer.lower() == answer_4):
        print("Correct ! Good Job \n")
        score = score + 1
        break
    else:
        print("Incorrect! \n")
        print("The correct answer is ", answer_4, "\n\n ")


# Print the score
while score <=4:
    print("Well done ! Your score was", score)
    break

while score>= 3:
    print("Better luck next time ! Your score was ",score)

#Goodby message
print("Thank you for playing simple quiz game")
