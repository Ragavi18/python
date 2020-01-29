import time
import random
name = input("What is your name? ")
print ("Hello, " + name, "Time to play hangman!")
print("") 
time.sleep(1)
print ("Start guessing...")
time.sleep(0.5)
words=['umbrella','chocolate','ice-cream',' parris','india','pink'] 
word=random.choice(words)
guesses = ''
if word=='umbrella':
  print ("clue:it protects us from rain")
elif word=='chocolate':
  print("clue:children's favourite")
elif word=='ice-cream':
  print("clue:most of them likes me during summer")
elif word=='parris':
  print("clue:romantic city")
elif word=='india':
  print("clue:our country")
elif word=='pink':
  print("clue:used to symbolize cancer")
turns=10
while turns > 0:         
    failed = 0             
    for char in word:      
        if char in guesses:    
            print(char)    
        else:
            print("_ ",end='')     
            failed += 1    
    if failed == 0:        
        print ("You won")  

        break              

    print()
    guess =input("guess a character:") 
    guesses += guess                    
    if guess not in word:  
        turns -= 1        
        print("Wrong")  
 
        print ("You have", + turns, 'more guesses') 
        if turns == 0:          
            print ("You Lose")
