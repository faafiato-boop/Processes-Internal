"""Gagana Samoa Program."""
# TF 29/07/2026
# Sprint 1, 2, 3

import random

# LAYOUT CONSTANTS
ENGLISH_WIDTH = 15
FAASAMOA_WIDTH = 15

# MENU CONSTANTS
VIEW_VOCABULARY = 1
QUIZ_ME = 2
EXIT = 3

# ERROR MESSAGES
INVALID_INPUT = "Invalid input, please enter a valid option number."

# Samoan to English vocabulary dictionary
VOCABULARY_CATEGORIES = {
    "Common Phrases": {
        "Talofa": "Hello",
        "Tofa": "Bye",
        "Fa'amolemole": "Please",
        "Fa'afetai": "Thank you",
        "O a mai oe?": "How are you?",
        "Manuia fa'afetai": "I am good, thank you",
        "Aea oe?": "How about you?",
        "Tulou": "Excuse me"
    },
    "Numbers": {
        "Tasi": "One",
        "Lua": "Two",
        "Tolu": "Three",
        "Fa": "Four",
        "Lima": "Five",
        "Ono": "Six",
        "Fitu": "Seven",
        "Valu": "Eight",
        "Iva": "Nine",
        "Sefulu": "Ten"
    },
    "Colours": {
        "Lanu mumu": "Red",
        "Lanu moli": "Orange",
        "Lanu samasama": "Yellow",
        "Lanu meamata": "Green",
        "Lanu moana": "Blue",
        "Lanu viole": "Purple",
        "Lanu piniki": "Pink",
        "Lanu luli": "Black",
        "Lanu pa'epa'e": "White"
    },
    "Family": {
        "Aiga": "Family",
        "Tāmā": "Father",
        "Tinā": "Mother",
        "Uso": "Sister/Brother",
        "Kasegi": "Cousin",
        "Tamaititi": "Child"
    }
}


def select_category(allow_all=False):
    """Prompt the user to pick a category, with an optional 'All' choice."""
    categories = list(VOCABULARY_CATEGORIES.keys())

    # Header message string for category selection menu
    print("\n<-<>--<>--<>-<>-<>--<>--<>->")
    print("--- Select a Category ---")

    # Set highest valid option number depending on whether "All" is included
    for i in range(len(categories)):
        print(f"{i + 1}. {categories[i]}")

    # If 'allow_all' is True, add an extra menu option for "All Categories"
    if allow_all:
        all_option_num = len(categories) + 1

        # Option text string for selecting all categories
        print(f"{all_option_num}. All Categories")

    # Combine all category dictionaries into one dictionary
    max_choice = len(categories) + 1 if allow_all else len(categories)

    # Loop continuously until the user enters a valid choice number
    while True:
        # Attempt to convert user input to integer choice
        try:
            # Prompt string asking user for their menu choice
            choice = int(input(f"Enter option (1-{max_choice}): "))

            # check if user selected a single category
            if 1 <= choice <= len(categories):
                selected_name = categories[choice - 1]

                # Return category name and dictionary
                return selected_name, VOCABULARY_CATEGORIES[selected_name]

            # Check if user selected "All Categories"
            if allow_all and choice == max_choice:

                # Combine all category dictionaries into one single dictionary
                combined_words = {}

                # Loop through all categories to merge vocabulary lists
                for category_dict in VOCABULARY_CATEGORIES.values():
                    combined_words.update(category_dict)

                # Return label string for all categories combined
                return "All Categories", combined_words

            print(INVALID_INPUT)

        # Catches user non-integer input
        except ValueError:
            print(INVALID_INPUT)


def display_vocabulary():
    """Print vocabulary table for the user's selected category."""
    # Get selected category and get words
    category_name, selected_words = select_category(allow_all=False)

    # print selected category name header string
    print("\n<><><><><><><><><><><><><><><><>")
    print(f"--- Category: {category_name} ---")

    # print headers for table column strings
    print(f"{'Samoan':<{FAASAMOA_WIDTH}} | {'English':<{ENGLISH_WIDTH}}")

    # print a dividing line string matching total width
    print("-" * (ENGLISH_WIDTH + FAASAMOA_WIDTH + 3))

    # Print each Samoan and English word pair in formatted columns
    for faasamoa_word, english_word in selected_words.items():
        # Formatted row string displaying vocabulary pairs
        print(
            f"{faasamoa_word.capitalize():<{FAASAMOA_WIDTH}} | "
            f"{english_word.capitalize():<{ENGLISH_WIDTH}}"
        )


def quiz_user():
    """Quiz the user on words from selected or all categories."""
    category_name, selected_words = select_category(allow_all=True)

    max_available = len(selected_words)

    # Ask how many questions the user wants to answer
    while True:
        # Attempt to convert the user's input into an integer
        try:
            # Prompt string asking user for total number of questions
            num_questions = int(input(
                f"How many questions would you like? "
                f"(Enter a number between 1 and {max_available}): "
            ))

            # Check if number is within valid range
            if 1 <= num_questions <= max_available:
                # Exit loop if input is within valid range
                break

            # Error message string for number out of range
            print(f"Invalid choice. Please enter a number between "
                  f"1 and {max_available}.")

        # catches cases where user input is not a whole number
        except ValueError:
            # Error message string for non-integer input
            print(f"Invalid choice. Please enter a number between "
                  f"1 and {max_available}.")

    # Quiz header text string showing chosen category
    print(f"\n--- Gagana Samoa Quiz ({category_name}) ---")

    # Convert dictionary of words into a list of pairs
    questions = list(selected_words.items())

    # Shuffle the list of keys
    random.shuffle(questions)
    questions = questions[:num_questions]

    # Sets starting score to 0
    score = 0

    # Store total number of questions to ask
    total_questions = len(questions)

    # Iterate directly through the dictionary
    for q_num, (faasamoa_word, english_translation) in enumerate(questions, 1):

        # Prompt string asking user for English translation of Samoan word
        user_answer = input(
            f"{q_num}) What is the English translation for '{faasamoa_word}'? "
        ).strip().lower()

        # Check if answer is correct (case insensitive)
        if user_answer == english_translation.lower():
            # Display custom message for a correct answer
            print("Sa'o! ✅\n")
            score += 1

        # displays feedback for incorrect answer
        else:
            # Incorrect answer feedback message string showing correct word
            print(f"Sese ❌. The sa'o answer is: {english_translation}\n")

    # Final quiz score summary with score displayed
    print(f"Quiz Complete! Well done your final score was: "
          f"{score}/{total_questions}\n")


def main():
    """Run the main program loop and handle menu choices."""
    # Keep the programme running until user inputs 3 for EXIT
    while True:
        # display starting menu decoration and header strings to user
        print("\n<><<>><<>><<>><<>><<>><<>><")
        print("-- Gagana Samoa Program ---")
        print("1. Vocabulary List")
        print("2. Quiz me")
        print("3. Exit")

        # Try to catch bad inputs before they crash my program
        try:
            # ask user to select an option string (1-3)
            choice = int(input("Enter an option (1-3): "))

        # Handles and displays message for non-integer input
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

            # Goodbye message string in Samoan
            print("<><<>>-- Tofa Soifua! --<<>><>")

            # stops the while loop and ends the programme
            break


if __name__ == "__main__":
    main()
