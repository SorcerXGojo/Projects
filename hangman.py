import random

words = ['chicken', 'dog', 'cat', 'mouse', 'frog']

hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\")
}

def display_man(wrong_guesses):
    print("************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print("The correct word was:", answer)

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = []
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in answer:
            guessed_letters.append(guess)
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
            if "_" not in hint:
                print("Congratulations! You guessed the word!")
                is_running = False
        else:
            guessed_letters.append(guess)
            wrong_guesses += 1
            print(f"Wrong guess! You have {6 - wrong_guesses} guesses left.")
            if wrong_guesses == 6:
                display_man(wrong_guesses)
                print("Game over! You've been hanged!")
                display_answer(answer)
                is_running = False

if __name__ == "__main__":
    main()