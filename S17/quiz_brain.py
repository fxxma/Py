class QuizBrain:

    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.question_list = q_list

    def next_question(self) :
        curr_q = self.question_list