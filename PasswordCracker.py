from random import *
guess=""
password=input("Enter your password")
letters=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","0","1","2","3","4","5","6","7","8","9"]
while(guess !=password):
    guess=""
    for letter in password:
        guessletter=letters[randint(0,35)]
        guess=str(guessletter) + str(guess)
    print(guess)
print("Password cracked!")

