import random 
r1=random.randint(1,9) 
chances=0
while chances < 5:
    guess=int(input("enter your guess"))
    if guess==r1:
        print("Congratulation!!You Won")
        break
    elif guess<r1:
        print("your guess was too low. guess a higher number!!")
    else:
        print("your guess was too high, guess a lower number!!")  
    chances+=1
if  not chances<5:
    print("You Lost!!")        
