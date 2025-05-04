# 1. Import the tools we need (like os and random)

# 2. Make a function to open and read the quiz_data.txt file
#    - Check if the file is really there
#    - Read everything inside
#    - Cut the text into parts, one for each question
#    - For each part:
#        - Get the question
#        - Get choices A to D
#        - Get the correct anSswer
#        - Put all that into a dictionary (like a mini-box for each question)
#    - Add each box to a list
#    - Give back the list when done

# 3. Make a function to run the quiz
#    - Mix up the questions so they come in random order
#    - For each question:
#        - Show the question and choices
#        - Ask the user to type A, B, C, D, or "exit"
#            - If they type "exit", stop the quiz early
#            - If they type A/B/C/D:
#                - Check if they got it right
#                - Say "Correct!" or show the right answer
#            - If they type something wrong, ask again

# 4. Make the main() function
#    - Get the list of questions from the file
#    - If no questions are found, show an error and stop
#    - Otherwise, say "Welcome!" and start the quiz
#    - After the quiz, say "Thanks for playing!"

# 5. Run the main() function if this file is being run directly
