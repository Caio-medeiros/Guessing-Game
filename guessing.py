from random import randrange
print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

secret_number = randrange(1, 101)
attempts = 0
points = 1000

print("What level of difficulty do you want?", secret_number)
print("(1) Easy \n(2) Medium \n(3) Hard")
level = int(input("Set the level: "))

if (level == 1):
    attempts = 20
elif (level == 2):
    attempts = 10
elif (level >= 3):
    attempts = 5


for round in range(1, attempts+1):
    print("\n********************************")
    print("attempt {} / {}".format(round, attempts))
    guess_input = input("*Type a number between 1 - 100: ")
    guessed_number = int(guess_input)

    got_it_right = secret_number == guessed_number
    bigger = guessed_number > secret_number
    smaller = guessed_number < secret_number
    bigger_than_100 = guessed_number > 100 or guessed_number < 1

    if (bigger_than_100):
        print("You are way too far of the number! Don't forget to type between 1 - 100")
        continue

    if (got_it_right):
        print("You got it right! \nTotal Points: {}".format(points))
        break
    else:
        if (bigger):
            print("You were close, you guessed a number bigger than the right one.")
        elif (smaller):
            print("You were close, you guessed a number smaller than the right one.")
        lost_points = abs(secret_number - guessed_number)
        points = points - lost_points
