#Author: Luke Ittycheria
#Date: 2/15/16
#Program: Make 9, basically a "blackjack" game. Computer keeps adding floats until the user tell it to stop
#The goal is to get the closest number to 9 without going over

#Initialize Variables
score = 0.0
userInput = "y"

#import random function
import random

#makes the next number a random float
nextNumber = random.random()

#Asks user if they would like more points --> then adds points to total score
while userInput == "y" and score < 9.0:
	nextNumber = random.random()*3
	userInput = raw_input("Your score is " + str(score) + " Would you like more points? (y or n): ")
	score = score + nextNumber
	score = round(score,1)
	
#if your score was greater than 9 print this:
if score > 9:
	print("Your score is: " + str(score) + " You lose")

#if score was less than or equal to 9 print this:
else:
	print ("Your score is: " + str(score) + " Not bad")