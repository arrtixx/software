#Programmed by Arrtix_x
#Designed for Windows

import random
import os

running = True
while running:
    try:
        count = int(input("Length: "))
        file = input("Output file: ")
        readonly = input("Make readonly? (y/n): ")

        data = [random.randint(0, 255) for _ in range(count)]

        with open(file, mode="wb") as fileOut:
            fileOut.write(bytes(data))

        if readonly == "y" or readonly == "Y":
            os.system(f"attrib +r {str(file)}")
        
        print(f"File {file} was successfuly created.")
        
    except ValueError:
        print("Error: 'length' is not numeric!")
