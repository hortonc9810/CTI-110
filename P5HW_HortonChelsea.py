# Chelsea Horton
# 5/14/2025
# P5HW: Adventure Game
# Unjumble the Animal: A word guessing game where the player must guess the correct animal from the scrambled letters.

import random

def get_jumbled_word(animal):
    """Returns a jumbled version of the given animal name."""
    letters = list(animal)
    random.shuffle(letters)
    return ''.join(letters)

def play_game():
    print("🐾 Welcome to 'Unjumble the Animal!' 🐾")
    print("Unscramble the letters to guess the animal. Get 3 correct to win!\n")

    animals = [
        "elephant", "giraffe", "kangaroo", "dolphin", "penguin", "tiger", "zebra",
        "lion", "rhino", "cheetah", "hippopotamus", "alligator", "buffalo", "chicken",
        "camel", "donkey", "flamingo", "goat", "iguana", "jaguar", "koala", "lemur",
        "meerkat", "narwhal", "ostrich", "peacock", "quokka", "raccoon", "sloth",
        "toucan", "vulture", "walrus", "yak", "wombat", "otter"
    ]

    correct = 0

    while correct < 3:
        animal = random.choice(animals)
        jumbled = get_jumbled_word(animal)
        print(f"🔤 Jumbled word: {jumbled}")

        guess = input("✏️ Your guess: ").strip().lower()

        if guess == animal:
            print("✅ Correct!\n")
            correct += 1
        else:
            print(f"❌ Wrong! The correct word was '{animal}'.\n")

    print("🎉 Congratulations! You unjumbled 3 animals correctly!")

# Run the game
play_game()