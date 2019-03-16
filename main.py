# Code for CS 303E Project 3, a simple polyalphabetic cipher
def main():

    # loop until user enters negative number
    while True:

        # Handle input
        userInput = input()
        userInput = userInput.strip()
        userInput = userInput.replace(' ', '')
        userInput = userInput.upper()               # Make all uppercase
        values = userInput.split(';')   # Parse input into a list

        # Check for end condition
        if int(values[0]) < 0:
            break

        # Assign list to different variables
        shift = int(values[0])
        secretWord = values[1]
        message = values[2]

        # Convert secretWord to numbers
        wordList = []
        for i in range(len(secretWord)):
            wordList.append(ord(secretWord[i]) - ord('A') + 1)

        extendedWordList = []
        messageList = []
        shiftedList = []
        finalStr = ""
        for i in range(len(message)):
            # Extend secretWord to message length
            extendedWordList.append(wordList[i % len(wordList)])
            # Convert message to numbers using shift size
            messageList.append(ord(message[i]) - ord('A') + 1 + shift)
            # Shift the secret word from the message
            shiftedList.append(extendedWordList[i] + messageList[i])
            # If greater than 26, wrap around
            if shiftedList[i] > 26:
                shiftedList[i] = shiftedList[i] % 26
            # Convert back to letters
            shiftedList[i] = chr(shiftedList[i] + ord('A') - 1)
            # Add shiftedList values to finalStr
            finalStr += shiftedList[i]

        print(finalStr)


main()
