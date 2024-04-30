from rembg import remove
from PIL import Image
import time


print("Welcome to the sports quiz game. We'll ask you a few questions, lets see how many you'll get")

quiz = {
    "Question1":{
        "Question":"Who is the greatest footballer of all time?",
        "Answer": "Lionel Messi"
    },
    "Question2":{
        "Question":"Who is the greatest Quarterback of all time?",
        "Answer": "Tom Brady"
    },
    "Question3":{
        "Question":"Who is the all time leader in points in the NBA?",
        "Answer": "Lebron James"
    },
    "Question4":{
        "Question": "Who is the greatest shooter of all time in Basketball?",
        "Answer": "Steph Curry"
    },
    "Question5":{
        "Question":"Who won the 2023 Rugby World Cup?",
        "Answer": "South Africa"
    },
    "Question6":{
        "Question":"Who is the greatest African Basketball player of all time?",
        "Answer":"Hakeem Olajuwon"
    },
    "Question7":{
        "Question": "Which country won the 2022 Fifa World Cup?",
        "Answer": "Argentina"
    },
    "Question8": {
        "Question": "Who won the 2023-24 NFL defensive player of the year?",
        "Answer": "Myles Garret"
    },
    "Question9": {
        "Question": "Who was the number 1 pick at the 2023 NBA draft?",
        "Answer": "Victor Wembenyama"
    },
    "Question10": {
        "Question": "How many Uefa Champions league titles has Zinedine Zidane won with Real Madrid?",
        "Answer": "3"
    },

}

lives = 3
score = 0
total = 10
attempts = 0
for key , value in quiz.items():
    while lives > 0 and attempts < total:
        print(f'Your current score is {score}')
        print(value['Question'])
        ans = input(': ').lower()
        if ans.lower() == value['Answer'].lower():
            print('You')
            time.sleep(1)
            print('are')
            time.sleep(2)
            print('correct')
            time.sleep(1)
            print(f'Answer : {value['Answer']}')
            score += 1
            attempts += 1
            break

        else:
            print('You')
            time.sleep(1)
            print('are')
            time.sleep(2)
            print('wrong!!!')
            time.sleep(1)
            print(f'Wrong answer\nCorrect answer : {value['Answer']}')
            break

percentage = (score / total) * 100
print(f'Your final score is {"%.2f" % percentage}%')