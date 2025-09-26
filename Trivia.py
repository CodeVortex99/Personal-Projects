# Set of Questions
# 10-15 Questions
# Randomly Choosen by the Computer
# Input for number of questions from the User.
# 10 Seconds to Answer Each Question
# 9 Points for Correct Answer
# -5 Points for Incorrect Answer
# -2 Points for Skipping the Question

import random
import time

def Inp_Ques():
    while True:
        try:
            Num_Qs = int(input("Enter the number of questions you want to answer bet 10-15: "))
            if 10 <= Num_Qs <= 15:
                return Num_Qs
            else:
                print("Please enter a number between 10-15")
        except:
            print("Invalid input/syntax, please input a number between 10-15")

Questions = {'What is the capital of Australia?': 'Canberra',
             'What element has the chemical symbol O?': 'Oxygen',
             'Who wrote the play Romeo and Juliet?': 'William Shakespeare',
             'Which planet is known as the Red Planet?': 'Mars',
             'How many Continents are there on Earth?': '7',
             'What is the hardest natural substance on Earth?': 'Diamond',
             'In which year did the Titanic Sink?': '1912',
             'Who painted the Mona Lisa?': 'Leonardo da Vinci',
             'What is the largest mammal in the world?': 'Blue Whale',
             'What is the main language spoken in Brazil?': 'Portuguese',
             'What does HTTP stand for?': 'Hypertext Transfer Protocol',
             'What is the name of the first artificial satellite sent into space?': 'Sputnik 1',
             'Who developed the theory of General Relativity?': 'Albert Einstein',
             'Which part of the cell contains the genetic material?': 'Nucleus',
             'What programming language is knwon for its snake logo and simplicity?': 'Python'}

def Trivia(Number):
    count = 0

    List_Questions = list(Questions.items())
    random.shuffle(List_Questions)

    Selected_Ques = List_Questions[:Number]

    for i, (question, answer) in enumerate(Selected_Ques, 1):
        print(f"\nQuestion {i}: {question}")

        S_Time = time.time()
        User_Ans = input("Enter your answer: ")
        T_Taken = time.time() - S_Time

        if T_Taken > 20 or T_Taken > 25:
            print(f"Time's up! The correct answer is {answer}.", "\n You have added -2 points to your score.")
            count -= 2
        elif User_Ans.upper() == answer.upper():
            print(f"Correct! 9 points achieved.")
            count += 9
        else:
            print(f"Incorrect! Score reduced by 5 points.")
            count -= 5
    
    print(f"You have succesfully completed the quiz and you achieved {count} points out of {Number * 9}.")

if __name__ == "__main__":
    Trivia(Inp_Ques())
