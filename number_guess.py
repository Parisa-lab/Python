from random import randint, seed

num = randint(1, 100)
print(num)
guess = int(input("Guess What Number I'm Thinking about? The Number is between 1 and 100. "))
small = 1
big = 100

while True:
    if guess == num:
        print("Hooray You Have Found the Number!")
        break
    elif guess < num:
        small = guess
        print("The Number is Between " + str(small) + " and " + str(big))
    else:
        big = guess
        print("The Number is Between " + str(small) + " and " + str(big))
    guess = int(input("Try Again: "))


