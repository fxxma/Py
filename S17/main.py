from data import question_data
from question_model import Question

q_bank = []
for q in question_data:
    q_text = q["text"]
    q_ans = q["answer"]
    new_q = Question(q_text,q_ans)
    q_bank.append(new_q)
print(q_bank[0].answer)

