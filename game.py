# Python_QuizGamedef welcome():
  #Prints a welcome message and giving brief instructions about the quiz.

  print("Welcome to the Python Quiz Game!")
  print("Answer all three questions to test your knowledge.")
  print("Enter the letter of the option you believe is correct.")
  print("\nLet's begin!\n")


def ask_question(question, options, answer):
  """
    Asks a question with multiple-choice options and checks the user's answer.

    Args:
        question: The question string.
        options: A list of option strings.
        answer: The index of the correct answer in the options list.

    Returns:
        True if the user's answer is correct, False otherwise.
    """

  print(question)
  for i, option in enumerate(options):
    print(f"{chr(65 + i)}: {option}")
  user_answer = input().upper()

  valid_letters = [chr(i) for i in range(65, 65 + len(options))]

  # validate user input to ensure it's a valid letter (A, B, C, ...)
  if user_answer not in valid_letters:
    print("Invalid input. Please try again.")
    return ask_question(question, options, answer)

  is_correct = user_answer == chr(answer + 65)
  if is_correct:
    print("Correct!\n")
  else:
    print(
        f"Incorrect. The correct answer is {chr(answer + 65)}: {options[answer]}\n"
    )
  return is_correct


def main():
  # quiz data
  questions = ["What is the capital of France?",
               "Which year did the first moon landing occur?",
               "What is the largest mammal on Earth?",]
  options = [["Berlin", "Paris", "London", "Rome"],
      ["1960", "1969", "1977", "1986"],
      ["Elephant", "Blue Whale", "Giraffe", "Rhinoceros"],
  ]
  answers = [1, 2, 1]  # correct answers updated

  #welcome to quiz and score initialization
  welcome()
  score = 0

  #ask each question and keep updating score
  for i, question in enumerate(questions):

    is_correct = ask_question(question, options[i], answers[i])
    if is_correct:
      score += 1

  #final score
  print(f"You scored {score} out of {len(questions)} ")


# Run quiz
if __name__ == "__main__":
  main()
