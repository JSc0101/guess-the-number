import random

guess__taken = 0
min__number = 1
max_number = 20

print("!Hello¡ What your name ?: ")

# nombre de usuario
username = input()

number__ale = random.randint(min__number, max_number)
print(
    f"Welcome {username} I am thinking in a number between {str(min__number)} and  {str(max_number)}"
)

# Bucle del juego
while guess__taken < 6:
    print("take a guess: ")
    guess = input()
    guess = int(guess)

    guess__taken += 1
    if guess < number__ale:
        print("Your guess is too low")
    if guess > number__ale:
        print("Your guess is to high")
    if guess == number__ale:
        break

if guess == number__ale:
    guess__taken = str(guess__taken)
    print(
        f"Good Job {username} you guessed my number in {guess__taken}guesses")

if guess != number__ale:
    number__ale = str(number__ale)
    print(f"No, the number que i was thinking of was {number__ale}")

# M;=4t38cTK:yNd$