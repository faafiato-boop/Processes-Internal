"""Fa'a Samoa Program."""
# TF 29/07/2026
# Sprint 1 (MVP)

# Module to shuffle quiz questions
import random

# LAYOUT CONSTANTS
ENGLISH_WIDTH = 15
FAASAMOA_WIDTH = 15

# MENU CONSTANTS
VIEW_VOCABULARY = 1
QUIZ_ME = 2
EXIT = 3

# ERROR CONSTANT
INVALID_INPUT = "Invalid input, please enter a number between 1-3"

# Samoan to English vocaublary dictionary
vocabulary = {
    "Talofa": "Hello",
    "Tofa": "Bye",
    "Fa'amolemole": "Please",
    "Fa'afetai": "Thank you",
    "O a mai oe?": "How are you?"
    }


def display_vocabulary():
    """Print the vocabulary in a formatted way."""
    # print main title for program
    print("\n--- Gagana Samoa Program ---")

    # print headers for table columns
    print(f"{'Samoan':<{FAASAMOA_WIDTH}} | {'English':<{ENGLISH_WIDTH}}")

    # print a dividing line matching total width
    print("-" * (ENGLISH_WIDTH + FAASAMOA_WIDTH + 3))

    for faasamoa_word, english_word in vocabulary.items():
        print(
            f"{faasamoa_word.capitalize():<{FAASAMOA_WIDTH}} | "
            f"{english_word.capitalize():<{ENGLISH_WIDTH}}"
        )


def quiz_user():
    """Quiz the user on words in vocabulary."""
    print("\n--- Gagana Samoa Quiz ---")

    questions = list(vocabulary.items())

    # Shuffle the list of keys
    random.shuffle(questions)

    # Iterate directly through the dictionary
    for faasamoa_word, english_translation in questions:
        user_answer = input(
            f"What is the English translation for '{faasamoa_word}'? "
            ).strip().lower()

        if user_answer == english_translation.lower():
            print("Correct!\n")
        else:
            print(f"Incorrect. The correct answer is: {english_translation}\n")


def main():
    """Run the main program loop and handle menu choices."""
    # Keep the programme running until user inputs 3 for EXIT
    while True:
        # display starting menu to user
        print("\n--- Gagana Samoa Program ---")
        print("1. Vocabulary List")
        print("2. Quiz me")
        print("3. Exit")

        # TRY to catch bad inputs before they crash the program
        try:
            # ask user to select an option (1-3)
            choice = int(input("Enter an option (1-3): "))
        except ValueError:
            print(INVALID_INPUT)

            # This restarts the loop immediately
            continue

        # if user inputs '1' display vocabulary list
        if choice == VIEW_VOCABULARY:

            # call the function
            display_vocabulary()

        # if user inputs '2' quiz the user
        elif choice == QUIZ_ME:

            # call the function
            quiz_user()

        # if user inputs '3' exits program
        elif choice == EXIT:
            print("Tofa Soifua!")

            # stops the while loop and ends the programme
            break


if __name__ == "__main__":
    main()
