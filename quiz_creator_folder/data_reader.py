import os

#Start
#set file path
def main():
    default_path = "quiz_data.txt"
    file_path = default_path

    if not os.path.isfile(file_path):
        print("File not found.")
        file_path = input("Enter full path").strip()
        if not os.path.isfile(file_path):
            print("No file found.")
            return

if __name__ == "__main__":
    main()

# Load the questions from the provided file.
def load_questions(file_path):
    """
    Load quiz question from a text file

    Each quetion block in the file should be separated by a line of 50 hypens. 
    the expected format for each block is:
        Q: Question text
        a) Option a
        b) Option b
        c) Option c
        d) option d
        answer: [a/b/c/d]

    Args:
        file_path(str): Path to the quiz data file.

    Returns:
        list: A list of dictionaries containing questions, answers, and options.
    """
#If the file can't be found or is empty, display an error message and stop the program.
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read().strip()
    except FileNotFoundError:
        print("dile not found")
        return []

    blocks = content.split("-" * 50)
    questions = []

#return a list of questions.
    for block in blocks: 
        lines = block.strip().splitline()
        if len(lines) >= 6:
            question_text = lines[0][3:].strip()
            options = {
                "A": lines [1][3:].strip()
                "B": lines [2][3:].strip()
                "C": lines [3][3:].strip()
                "D": lines [4][3:].strip()
            }
            answer_line = lines [5].split(":")
            if len(answer_line) == 2:
                answer = answer_line[1].strip().upper()
                questions.append ({
                    "questions": question_text,
                    "options": options,
                    "answer": answer
                })
    return questions

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
