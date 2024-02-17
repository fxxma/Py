from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

q_bank = []
for q in question_data:
    q_text = q["text"]
    q_ans = q["answer"]
    new_q = Question(q_text,q_ans)
    q_bank.append(new_q)

quiz = QuizBrain(q_bank)

while quiz.still_has_questions() :
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is{quiz.score}/{len(quiz.question_list)}")
