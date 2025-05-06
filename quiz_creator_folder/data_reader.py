# Start
def main():
    pass

if __name__ == "__main__":
    main()

# 2. In the main function:
#    - Check if the file exists in the current directory.
#    - If not, ask the user to provide the full path to the quiz file.
# 3. Load the questions from the provided file using the load_questions() function.
#    - If the file can't be found or is empty, display an error message and stop the program.
#    - If the file is loaded correctly, return a list of questions.
# 4. In the run_quiz() function:
#    - Shuffle the list of  questions to make the quiz random.
#    - For each question in the shuffled list, display the question and choices (A, B, C, D).
#    - Ask the user to input their answer (A, B, C, D, or 'exit' to quit).
#    - Check if the user's answer is correct:
#      - If correct, display " Correct!".
#      - If incorrect, display " Incorrect!" and show the correct answer.
#    - If the user types 'exit', stop the quiz.
#    - If the answer is invalid, prompt the user again.
# 5. After the quiz is finished, print a thank-you message for playing.
# 6. End the program.
