class QuizBrain:

    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self) :
        curr_q = self.question_list[self.question_number]
        self.question_number += 1
        res = input(f"Q.{self.question_number} : {curr_q.text} (True / False)")
        self.check_answer(res,curr_q.answer)
    
    def still_has_questions(self) :
        if self.question_number < len(self.question_list) :
            return True
        else :
            return False
    
    def check_answer(self, user, ans) :
        if user.lower() == ans.lower() :
            print("You got it right!")
            self.score += 1 
        else :
            print("You got it wrong")
        print(f"The correct answer was : {ans}.")
        print(f"Your current score is : {self.score}/{self.question_number}.")
        print("\n")
        
