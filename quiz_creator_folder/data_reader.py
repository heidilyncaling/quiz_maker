import os
import random

#Start

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
        print("file not found")
        return []

    blocks = content.split("-" * 50)
    questions = []

#return a list of questions.
    for block in blocks: 
        lines = block.strip().splitlines()
        if len(lines) >= 6:
            question_text = lines[0][3:].strip()
            options = {
                "A": lines [1][3:].strip(),
                "B": lines [2][3:].strip(),
                "C": lines [3][3:].strip(),
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

# run_quiz() function
def run_quiz(questions):
    """
    Run the quiz by presenting each questions to the user.

    Args:
        questions(list):  A list of question dictionaries
    """
    random.shuffle(questions)
    score = 0

    for idx, q in enumerate(questions, 1):
        print(f"\nQuestion {idx}: {q['questions']}")
        for key in["A", "B", "C", "D"]:
            print (f"{key}.{q['options'][key]}")
        
        while True:
            user_answer = input("A/B/C/D OR EXIT:").strip().upper()
            if user_answer == "EXIT":
                print("\n Exiting. Thanks four playing!")
                print(f"Your score: {score}/{idk - 1}")
                return
            if user_answer in ["A", "B", "C", "D"]:
                break
            print("invalid input. a,b,c,d or exit only.")

        if user_answer == q["answer"]:
            print("correct")
            score += 1
        else:
            correct_option = q["answer"]
            correct_answer = q["options"][correct_option]
            print (f"wrong. answer: {correct_option}: {correct_answer}")    
            
# After the quiz is finished, print a thank-you message for playing.
    print("\n Thanks four playing!")
    print (f"Your score: {score}/{idx - 1}")

def main():
    default_path = "quiz_data.txt"
    file_path = default_path

    if not os.path.isfile(file_path):
        print("File not found.")
        file_path = input("Enter full path").strip()
        if not os.path.isfile(file_path):
            print("No file found.")
            return
    questions = load_questions(file_path)
    if not questions:
        print("no valid questions")
        return
    run_quiz(questions)

if __name__ == "__main__":
    main()
