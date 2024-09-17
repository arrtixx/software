#Programmed by Arrtix_x

import random

running = True
while running:
    try:
        fromN = int(input("From: "))
        toN = int(input("To: "))
        
        result = int(random.randint(fromN, toN))
        
        print(f"Random number: {result}")
        
    except ValueError:
        print("Error: Option 'from' or 'to' is not numeric!")
