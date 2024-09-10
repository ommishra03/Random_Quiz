import pandas as pd
import random

def load_questions(filenames):
    all_questions = []
    for filename in filenames:
      df = pd.read_csv(filename)
      questions = df[['question', 'answer']].to_dict(orient='records')
      all_questions.extend(questions)
    return all_questions

def ask_questions(questions):
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        answer = input("Your answer: ").strip()
        if answer.lower() == q['answer'].strip().lower():
            score += 1
    return score

def main():
    filenames = [paste the path of quiz data set]
    questions = load_questions(filenames)
    selected_questions = random.sample(questions, 10)
    score = ask_questions(selected_questions)
    print(f"\nYour score: {score}/10")

if __name__ == "__main__":
    main()
