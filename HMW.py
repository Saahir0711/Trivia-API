import requests
import random
import html
import time

print("Welcome to Trivia Game! You have 5 questions to answer and 10 seconds per question")
time.sleep(2)
score = 0


response = requests.get("https://opentdb.com/api.php?amount=5")
if response.status_code == 200:
    trivia = response.json()
    trivia = trivia['results']
    question = 0

    for q in trivia:

        question += 1
        print(f"Question {question}:\nType: {q['type']} \nDifficulty: {q['difficulty']} ")
        print(f"Question: {html.unescape(q['question'])}")
        ops = (q['incorrect_answers'] + [q['correct_answer']])
        options = []
        for i in ops:
            options.append(html.unescape(i))
        random.shuffle(options)
        print(f"Options: {options}")


        start_time = time.time()
        uAnswer = input(f"Your Answer (1-{len(options)}): ")
        end_time = time.time()
        if (end_time - start_time) > 10:
            print("You took too long. This answer wont count\n")
            time.sleep(2)

            continue
        while True:
            try:
                int_answer = int(uAnswer)
                break
            except ValueError:
                uAnswer = input("Invalid Answer. PLease enter 1-4: ")
        if options[(int_answer - 1)] == q['correct_answer']:
            print("Correct!\n") 
            score += 1
        else:
            print(f"Incorrect. The correct answer was {q['correct_answer']}\n")
        time.sleep(2)
        
    print(f"Well done, you got {score}/5 questions!")


        
