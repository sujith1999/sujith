#!/usr/bin/python3
import random
count=0
r=0
while count<=100:
    roll=input("press r to roll the dice")
    if roll=="r":
    	r=random.randint(1,6)
    	count=count+r  
    print("your random number is",r)
    print("you are on ",count)
    if count==8:
    	count=37
    	print("you climbed to",count)
    elif count==11:
         count=2
         print("you r down to",count)
    elif count==13:
    	 count=34
    	 print("up the ladder",count)
    elif count==25:
    	 count=4
    	 print("down the ladder",count)
    elif count==38:
    	 count=9
    	 print("down the ladder",count)
    elif count==40:
    	 count=68
    	 print("up the ladder",count)
    elif count==52:
    	 count=81
    	 print("up the ladder",count)
    elif count==65:
    	 count=46
    	 print("down the ladder",count)
    elif count==76:
    	 count=97
    	 print("up the ladder",count)
    elif count==93:
    	 count=64
    	 print("down the ladder",count)
    elif count>=100:
    	 print("you r the winner")