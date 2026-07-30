"""Fa'a Samoa Program."""
# TF 29/07/2026
# Sprint 1 (MVP)

# LAYOUT CONSTANTS
ENGLISH_WIDTH = 20
FAASAMOA_WIDTH = 20

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
    print(f"{'English':<{ENGLISH_WIDTH}} | {'Samoan':<{FAASAMOA_WIDTH}}")

    # print a dividing line matching total width
    print("-" * (ENGLISH_WIDTH + FAASAMOA_WIDTH + 3))

    for english_word, faasamoa_word in vocabulary.items():
        print(
            f"{faasamoa_word.capitalize():<{FAASAMOA_WIDTH}} | {english_word.capitalize():<{ENGLISH_WIDTH}}"
        )


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

        # if user inputs '3' exits program
        elif choice == EXIT:
            print("Tofa Soifua!")

            # stops the while loop and ends the programme
            break


if __name__ == "__main__":
    main()
            

        
    
    


        


    

    


