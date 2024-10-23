import os
import random

def main():

    print("****WELCOME TO THE QUIZZ GAME****")
    user_input = input("Press ENTER when you are ready to play\n")
    
    if user_input == "":
        game()
    else:
        pass
        
def load_questions():
    with open('questions.txt', 'r', encoding='utf-8') as file:
            
        questions = []

        for line in file: 
            line = line.strip()

            if line.startswith("[") and line.endswith("]"):
                    category = line  # Save the category
                    continue
            
            parts = line.split('|') 
            if len(parts) == 6:
                question = parts[0]
                choices = parts[1:5]
                correct_answer = parts[5]

                questions.append({
                    'category': category,
                    'question': question,
                    'choices': choices,
                    'correct_answer': correct_answer
                })

    return questions
'''
    for q in questions:
        print(f"Category: {q['category']}")
        print(f"Question: {q['question']}")
        print(f"Choices: {q['choices']}")
        print(f"Correct Answer: {q['correct_answer']}")
        print("-" * 40)
   
'''

def get_easy_q(questions):
    return [q for q in questions if q['category'] == "[Easy]"]

def get_med_q(questions):
    return [q for q in questions if q['category'] == "[Medium]"]

def get_hard_q(questions):
    return [q for q in questions if q['category'] == "[Hard]"]

def get_super_hard_q(questions):
    return [q for q in questions if q['category'] == "[Super Hard]"]

def get_random_question(questions, difficulty):
    if difficulty == "easy":
        return random.choice(get_easy_q(questions))
    elif difficulty == "medium":
        return random.choice(get_med_q(questions))
    elif difficulty == "hard":
        return random.choice(get_hard_q(questions))
    elif difficulty == "super hard":
        return random.choice(get_super_hard_q(questions))
    return None

def question_num(n_question):
    positions = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "Last"]

    if n_question < len(positions):
        print(positions[n_question] + " question")
        

def game():

    is_game_over = False
    n_question = 0
    questions = load_questions()
    difficulty = ["easy", "medium", "hard", "super hard"] 
    
    
    while not is_game_over and n_question < 10:

        question_num(n_question)

        # Choose difficulty based on question number
        if n_question < 3:
            question = get_random_question(questions, difficulty[0]) 
        elif n_question >= 3 and n_question < 6:
            question = get_random_question(questions, difficulty[1])  
        elif n_question >= 6 and n_question < 9:
            question = get_random_question(questions, difficulty[2])  
        else:
            question = get_random_question(questions, difficulty[3])  

        if n_question == 10:

            print("This is the final question! All or nothing, take your time...\n")

            if question:
                print(question['question'])
                print("Choices:")
                for idx, choice in enumerate(question['choices'], 1):
                        print(f"{idx}. {choice}")

                user_input = input("Lock in your final answer: ")[0].upper()
                if user_input != question['correct_answer']:
                    print(f"That's incorrect!\nThe correct answer was {question['correct_answer']}. Better luck next time!\n")
                    
                else:
                    print(f"Congratulations! You got it right! The correct answer is {question['correct_answer']}.\n")
                    print("And that's it! You've completed the final question. Well done!")

        else: 
            if question:
                print(question['question'])
                print("Choices:")
                for idx, choice in enumerate(question['choices'], 1):
                        print(f"{idx}. {choice}")

                user_input = input("Lock in your final answer: ")[0].upper()
                if user_input != question['correct_answer']:
                    print(f"That's incorrect!\nThe correct answer was {question['correct_answer']}. Better luck next time!\n")
                    is_game_over = True
                else:
                    print(f"Congratulations! You got it right! The correct answer is {question['correct_answer']}.\n")
            
        n_question += 1

        if n_question == 10:
            is_game_over = True

main()


