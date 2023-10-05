class QuizBrain:
    def __init__(self, question_list):
        self.question_number=0
        self.question_list=question_list
        self.score=0

    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number +=1
        a=input(f"Q.{self.question_number} : {current_question.text} (True/False)")
        self.check_answer(a,current_question.answer)

    def still_has_question(self):
        l=len(self.question_list)
        if self.question_number==l:
            return False
        else:
            return True

    def check_answer(self,answer,correct_answer):
        if answer.lower()==correct_answer.lower():
            print("yup you got it right")
            self.score+=1

            print(f"the correct answer was : {correct_answer}")
        else:
            print("try again")
            print(f"the correct answer was : {correct_answer}")
        print(f"so your score now is :{self.score}/{self.question_number}")

