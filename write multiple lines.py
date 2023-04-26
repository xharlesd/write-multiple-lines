# Bernido, Charles David P. | BSCPE 1-5
# Object Oriented Programming | Assignment 4 - Problem 3
# Write a method in python to write multiple line of text contents into a text file mylife.txt


def main():
    # Open mylife.txt (write)
    with open("mylife.txt", "w") as input_file:
        
        # Create a loop
        while True:
            # Ask for user input
            user_input = input("\nEnter line: ")

            # write the input to mylife.txt
            input_file.write("Enter line: " + str(user_input))
        
            # ask the user if he/she wants to add more lines
            yes_or_no = input("Are there more lines (y/n)? ")

            # write the input to mylife.txt
            input_file.write("Are there more lines (y/n)? " + str(yes_or_no) + "\n")

            # if yes
            if yes_or_no.lower() == "y":
                continue

            # if no
            elif yes_or_no.lower() == "n":
                print("Thanks for using my program!")
                exit()

            # if the user failed to enter y or n
            else:
                print("ERROR! Invalid input. Please choose either y or n only. ")
                break

main()