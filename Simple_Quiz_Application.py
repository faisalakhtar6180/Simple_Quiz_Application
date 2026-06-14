"""
Simple Quiz Application
-----------------------
A command-line quiz program that asks multiple-choice questions,
evaluates answers, tracks scores, and displays detailed feedback.

Run:
    python quiz_app.py
"""

import random


# -----------------------------
# Quiz Questions Database
# -----------------------------
QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "options": {
            "A": "Berlin",
            "B": "Madrid",
            "C": "Paris",
            "D": "Rome"
        },
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": {
            "A": "Venus",
            "B": "Mars",
            "C": "Jupiter",
            "D": "Mercury"
        },
        "answer": "B"
    },
    {
        "question": "Who developed the Python programming language?",
        "options": {
            "A": "Dennis Ritchie",
            "B": "James Gosling",
            "C": "Bjarne Stroustrup",
            "D": "Guido van Rossum"
        },
        "answer": "D"
    },
    {
        "question": "What is the value of 12 × 8?",
        "options": {
            "A": "96",
            "B": "88",
            "C": "108",
            "D": "92"
        },
        "answer": "A"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": {
            "A": "Oxygen",
            "B": "Nitrogen",
            "C": "Carbon Dioxide",
            "D": "Hydrogen"
        },
        "answer": "C"
    },
    {
        "question": "What does CPU stand for?",
        "options": {
            "A": "Central Processing Unit",
            "B": "Computer Processing Utility",
            "C": "Central Program Unit",
            "D": "Control Processing Unit"
        },
        "answer": "A"
    },
    {
        "question": "Which is the largest ocean on Earth?",
        "options": {
            "A": "Indian Ocean",
            "B": "Atlantic Ocean",
            "C": "Arctic Ocean",
            "D": "Pacific Ocean"
        },
        "answer": "D"
    },
    {
        "question": "What is the square root of 144?",
        "options": {
            "A": "10",
            "B": "11",
            "C": "12",
            "D": "14"
        },
        "answer": "C"
    },
    {
        "question": "Which scientist proposed the theory of relativity?",
        "options": {
            "A": "Isaac Newton",
            "B": "Albert Einstein",
            "C": "Galileo Galilei",
            "D": "Nikola Tesla"
        },
        "answer": "B"
    },
    {
        "question": "Which company developed the Windows operating system?",
        "options": {
            "A": "Apple",
            "B": "Google",
            "C": "Microsoft",
            "D": "IBM"
        },
        "answer": "C"
    }
]


def display_question(question_data, question_number):
    """
    Display a quiz question and its answer options.

    Args:
        question_data (dict): Dictionary containing question details.
        question_number (int): Current question number.
    """
    print("\n" + "=" * 50)
    print(f"Question {question_number}:")
    print(question_data["question"])
    print()

    for option, text in question_data["options"].items():
        print(f"{option}. {text}")

    print("=" * 50)


def get_user_answer():
    """
    Get and validate the user's answer.

    Returns:
        str: Valid answer choice (A, B, C, or D).
    """
    valid_answers = {"A", "B", "C", "D"}

    while True:
        answer = input("\nYour answer (A/B/C/D): ").strip().upper()

        if not answer:
            print("Input cannot be empty. Please enter A, B, C, or D.")
            continue

        if answer in valid_answers:
            return answer

        print("Invalid choice. Please enter A, B, C, or D.")


def calculate_score(correct_answers, total_questions):
    """
    Calculate percentage score.

    Args:
        correct_answers (int): Number of correct answers.
        total_questions (int): Total number of questions.

    Returns:
        float: Percentage score.
    """
    return (correct_answers / total_questions) * 100


def get_performance_feedback(percentage):
    """
    Determine performance feedback based on percentage.

    Args:
        percentage (float): Percentage score.

    Returns:
        str: Performance message.
    """
    if percentage >= 90:
        return "Excellent"
    elif percentage >= 70:
        return "Very Good"
    elif percentage >= 50:
        return "Good"
    else:
        return "Needs Improvement"


def show_results(player_name, correct_answers, total_questions):
    """
    Display final quiz results.

    Args:
        player_name (str): Player's name.
        correct_answers (int): Number of correct answers.
        total_questions (int): Total number of questions.
    """
    incorrect_answers = total_questions - correct_answers
    percentage = calculate_score(correct_answers, total_questions)
    feedback = get_performance_feedback(percentage)

    print("\n" + "=" * 50)
    print("QUIZ COMPLETE!")
    print("=" * 50)

    print(f"Player: {player_name}")
    print(f"Correct Answers: {correct_answers}")
    print(f"Incorrect Answers: {incorrect_answers}")
    print(f"Final Score: {correct_answers}/{total_questions}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Performance: {feedback}")

    print("=" * 50)


def play_quiz():
    """
    Run a complete quiz session.
    """
    print("\nWelcome to the Quiz Application!")
    print("Test your knowledge with questions from various topics.\n")

    # Get player name
    while True:
        player_name = input("Enter your name: ").strip()

        if player_name:
            break

        print("Name cannot be empty. Please try again.")

    # Create a shuffled copy of questions
    questions = QUESTIONS.copy()
    random.shuffle(questions)

    score = 0
    total_questions = len(questions)

    # Ask questions
    for index, question in enumerate(questions, start=1):
        display_question(question, index)

        user_answer = get_user_answer()
        correct_answer = question["answer"]

        if user_answer == correct_answer:
            score += 1
            print("\n✅ Correct!")
        else:
            correct_option_text = question["options"][correct_answer]
            print("\n❌ Incorrect!")
            print(
                f"Correct Answer: "
                f"{correct_answer}. {correct_option_text}"
            )

        print(f"Current Score: {score}")

    # Show final results
    show_results(player_name, score, total_questions)


def ask_play_again():
    """
    Ask the user if they want to play again.

    Returns:
        bool: True if user wants to play again, otherwise False.
    """
    while True:
        choice = input(
            "\nWould you like to play again? (Y/N): "
        ).strip().upper()

        if choice == "Y":
            return True

        if choice == "N":
            return False

        print("Please enter Y or N.")


def main():
    """
    Main program entry point.
    """
    try:
        while True:
            play_quiz()

            if not ask_play_again():
                print("\nThank you for playing the Quiz Application!")
                print("Goodbye!")
                break

    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
        print("Exiting gracefully...")

    except Exception as error:
        print(f"\nAn unexpected error occurred: {error}")
        print("The application will now exit.")


if __name__ == "__main__":
    main()