from hangman_display import *

def main():
    word = "example"
    len_word = len(word)
    splited_word = list(word)
    positions = []
    attempts = 0
    correct_guesses = 0

    print(f"The word as {len_word} letters.")
    print("_ " * len_word)
    print()
    #print(splited_word)

    
    
    while correct_guesses < len_word and attempts < 7:
        guess = input("Guess a letter: ")
        found = False 

        for i, letter in enumerate(word):
            if guess == letter:
                print(f"Found '{guess}' at position {i}")
                positions.append(i)  
                correct_guesses += 1
                found = True
        
        if not found:
            print("Letter not in the word u dumb bitch")
            display_hangman(attempts)
            attempts += 1 

        for i, letter in enumerate(word):
            if i in positions:
                print(letter, end=" ")
            else:  
                print("_", end=" ") 
        print()
    
    #final result
    if correct_guesses == len_word:
        print("Congratulations! You've found the correct word!")
    else:
        print("Game over! Better luck next time.")

def display_hangman(stage):
    if stage < 0 or stage >= len(hangman_stages):
        stage = 0  
    print(hangman_stages[stage])

main()
