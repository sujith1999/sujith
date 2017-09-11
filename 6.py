#!/usr/bin/python3
import random

op = ["rock","paper","scissors"]
AI = op[random.randint(0,2)]
user = input("pick either rock,paper or scissors: ")
user = user.lower()
print("you choose",user,"ai chosses",AI)
if user == 'rock' or 'paper' or 'scissors' :
	print ("The computer has drawn ",AI,"whilst you have drawn",user)
if user == 'rock':
	if AI =='rock':
		print ('tie game')
	elif AI == 'PAper':
		print ('AI wins')
	else:
		print ('user wins')
if  user =='paper':
	if AI =='rock':
		print('user wins')
	elif AI =='paper':
		print('tie game')
	else:
		print('AI wins')
if  user =='scissors':
	if AI =='Rock':
		print('AI wins')
	elif AI =='paper':
		print('user wins')
else:
		print('Tie game')
