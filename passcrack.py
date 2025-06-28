# Password-cracker
import os
from random import randint
import time

# Function to crack the password letter by letter
def crack_password(password):
    keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    
    # List to store the guessed password (one character at a time)
    guessed_password = [''] * len(password)
    
    # Loop through each character of the password
    while ''.join(guessed_password) != password:
        # Loop through the password positions and guess each letter
        for i in range(len(password)):
            if guessed_password[i] == '':
                # Guess each character randomly from the possible keys
                guessed_password[i] = keys[randint(0, 35)]

        # Display the current guess progress
        print(''.join(guessed_password))
        print("Attacking... Please wait..........................................")
        
        # Slow down for simulation (you can remove this line for faster performance)
        time.sleep(0.01)
        
        # Clear the screen after each iteration
        os.system("cls")

    return ''.join(guessed_password)

# Main loop for input
while True:
    pas = input("PLEASE ENTER THE PASSWORD TO BE CRACKED: ")

    if pas:
        print(f"Starting password cracking for: {pas}")
        cracked_password = crack_password(pas)
        print(f"The password is: {cracked_password}")
   
