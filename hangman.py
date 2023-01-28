import random


word_bank = ["ali", "hassan", "hossein", "sajjad", "mohammad", "sadegh", "kazem", "reza", "javad",
             "hadi", "mahdi", "fatemeh", "zahra", "zeynab", "masome", "khadije", "maryam", "sakine", "roqayeh"]
correct_word = []
wrong_word = []

user_mistake = 0

x = random.randint(0, len(word_bank)-1)
word = word_bank[x]

while user_mistake < 6:
    for i in range(len(word)):
        if word[i] in correct_word:
            print(word[i], end=" ")
        else:
            print("_", end=" ")

    if len(correct_word) == len(word):
        print("congragulation")
        print(" you win 🎊")

    user_char = input("\n\nplease enter your guess world: ")
    user_char = user_char.lower()
    if len(user_char) == 1:
        if user_char in word:
            correct_word.append(user_char)
            print("✅")
        else:
            wrong_word.append(user_char)
            user_mistake += 1
            print("❌")

    else:
        print("please enter 1 word!")

if user_mistake == 6:
    print("Game Over ☠️")
