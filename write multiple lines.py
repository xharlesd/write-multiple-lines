# Bernido, Charles David P. | BSCPE 1-5
# Object Oriented Programming | Assignment 4 - Problem 2
# Write a method in python to write multiple line of text contents into a text file mylife.txt

# Open mylife.txt (write)
with open("mylife.txt", 'w') as input_file:
    
    # Create a loop
    while True:

        # Ask for user input
        user_input = input =("Enter line: ")

        # write the input to mylife.txt
        input_file.write(str(user_input))
        """"""
    
    # add more lines
    # write the input to mylife.txt
    # if yes
    # continue
    # if no
    # exit