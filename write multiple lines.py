# Bernido, Charles David P. | BSCPE 1-5
# Object Oriented Programming | Assignment 4 - Problem 3
# Write a method in python to write multiple line of text contents into a text file mylife.txt

import time
import pyfiglet
from colorama import Fore, Style

def intro():
    # Use pyfiglet formatting to Assignment # 4"
    print("")
    lab = pyfiglet.figlet_format("MULTIPLE LINES", font = "banner3-d", width = 130, justify = "center")
    print(Style.BRIGHT + Fore.GREEN + lab)

    # format introductory message
    print(Fore.GREEN + "\033[1m-" * 130 + '\033[0m')
    intro = "INSTRUCTION: ENTER ANY WORD/ PHRASE. TYPE 'y' TO CONTINUE, TYPE 'n' TO STOP." 
    intro_centered = intro.center(130)
    print( "\033[1m" + intro_centered) 
    print(Fore.GREEN + "\033[1m-" * 130 + '\033[0m')

    # insert time delay
    time.sleep(1.5)

def main():
    # Open mylife.txt (write)
    with open("mylife.txt", "w") as input_file:
        
        # Create a loop
        while True:
            # Ask for user input
            user_input = input(Fore.GREEN + "\033[1m\n\t\t\tENTER LINE:  \033[0m" + Fore.YELLOW)

            # write the input to mylife.txt
            input_file.write("Enter line: " + str(user_input) + "\n")
        
            # ask the user if he/she wants to add more lines
            yes_or_no = input(Fore.GREEN + "\033[1m\t\t\tAre there more lines (y/n)?  \033[0m" + Fore.YELLOW)

            # write the input to mylife.txt
            input_file.write("Are there more lines (y/n)? " + str(yes_or_no) + "\n")
            
            # if yes
            if yes_or_no.lower().strip() == "y":
                continue

            # if no
            elif yes_or_no.lower().strip() == "n":
                time.sleep(3.5)
                print(Fore.MAGENTA + "\n\t\t\t[Program will be terminated..............................] \n")
                time.sleep(2)
                exit()

            # if the user failed to enter y or n
            else:
                print(Fore.MAGENTA + "\n\t\t\t[ERROR! Invalid input. The program will be terminated....]")
                exit()

# start
intro()
main()