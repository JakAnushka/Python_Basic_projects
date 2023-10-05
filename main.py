from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank=[]
for i in range(0, len(question_data)):
    Ques=question_data[i]["text"]
    Ans=question_data[i]["answer"]
    bank=Question(Ques,Ans)
    question_bank.append(bank)


QB=QuizBrain(question_bank)

while QB.still_has_question() is True:
    QB.next_question()

else:
    print("YOU'VE Complete this game :)")
    print("your full score :")
    print(f"{QB.score}/{QB.question_number}")




