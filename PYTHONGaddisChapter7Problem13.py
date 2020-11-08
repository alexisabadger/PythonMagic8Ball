# Exercise 7.13 - Magic 8 Ball

# Write a program that simulates a Magic 8 Ball, which is a 
# fortune-telling toy that displays a random response to a 
# yes or no question. In the student sample programs for this 
# book, you will find a text file named 8_ball_responses. 
# txtPreview the document. The file contains 12 responses, 
# such as "I don't think so", "Yes, of course!", "I'm not sure", 
# and so forth. The program should read the responses from the 
# file into a list. It should prompt the user to ask a question, 
# then display one of the responses, randomly selected from the list. 
# The program should repeat until the user is ready to quit. 

import random

def main():
    # Open a file for reading.
    infile = open(r'#', 'r')

    # Get its contents in a list.
    myList = make_list(infile)

    # Shake the Magic 8 Ball.
    shake(myList)

    # Close the file.
    infile.close()

# This function takes the file object and makes a list.
def make_list(infile):

    # Make an empty list.
    myList = []

    # Read the file object.
    line = infile.readline()

    # Loop through the file object, stipping away newline.
    for line in infile:
        line = line.strip()

        # If there is content in line, append it to the list.
        if line:
            myList.append(line)
    
    # Return the list.
    return myList

# This function shakes the Magic 8 Ball.
def shake(myList):
    print('You found a Magic 8 Ball. Would you like to shake it?')
    ask = 'Y'
    size = len(myList)

    while ask == 'Y':
        ask = input('Enter Y if yes, anything else to exit.')
        fortune = myList[random.randint(0, (size - 1))]
        print('Magic 8 Ball says...', fortune)
        print('Would you like to shake it again?')

# Call the main function.
main()