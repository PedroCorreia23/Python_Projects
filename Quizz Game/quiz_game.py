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
        
    easy_questions = [q for q in questions if q['category'] == "[Easy]"]
    return easy_questions

def get_random_easy_question(questions):
    easy_questions = get_easy_q(questions)
    
    # Choose a random question from the list of easy questions
    if easy_questions:
        ez_q =  random.choice(easy_questions)
        return ez_q
    else:
        return None

def game():

    is_game_over = False

    questions = load_questions()

    random_easy_question = get_random_easy_question(questions)

    if random_easy_question:
        print(f"Question: {random_easy_question['question']}")
        for choice in random_easy_question['choices']:
            print(choice)
        print(f"Correct Answer: {random_easy_question['correct_answer']}")
    else:
        print("No easy questions found.")

     


main()


