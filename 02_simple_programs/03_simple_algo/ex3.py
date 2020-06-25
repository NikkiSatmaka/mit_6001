# -*- coding: utf-8 -*-
"""
Created on Wed Jun  25 11:44:04 2020

@author: nikkisatmaka
"""

num = 42
low = 0
high = 100
guess = int((high + low) / 2)

print("Please think of a number between 0 and 100!")
while(True):
    print("Is your secret number " + str(guess) + "?")
    print("Enter 'h' to indicate the guess is too high", end=' ')
    print("Enter 'l' to indicate the guess is too low.", end=' ')
    print("Enter 'c' to indicate I guessed correctly.", end=' ')
    ans = input()
    if ans == 'h':
        high = guess
        guess = int((high + low) / 2)
    elif ans == 'l':
        low = guess
        guess = int((high + low) / 2)
    elif ans == 'c':
        print("Game over. Your secret number was: " + str(guess))
        break
    else:
        print("Sorry, I did not understand your input.")
