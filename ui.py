from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR="#375362"
FONT=("Arial",20,"italic")

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz=quiz_brain

        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,background=THEME_COLOR)
        self.score=Label(text=f"Score: {0}",bg=THEME_COLOR,fg="white")
        self.score.grid(row=0,column=1)
        self.canvas=Canvas(width=300,height=250,bg="white")
        self.question_text=self.canvas.create_text(150,125,width=280,text="Some Question Text",fill=THEME_COLOR,font=FONT)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=(30,30))
        true_img=PhotoImage(file="images/true.png")
        self.left=Button(image=true_img,highlightthickness=0,command=self.correct)
        self.left.grid(row=2,column=0)
        false_img=PhotoImage(file="images/false.png")
        self.right=Button(image=false_img,highlightthickness=0,command=self.wrong)
        self.right.grid(row=2,column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You have reached end of the quiz.")
            self.left.configure(state="disabled")
            self.right.configure(state="disabled")

    def correct(self):
        check=self.quiz.check_answer("True")
        self.give_feedback(check)

    def wrong(self):
        check=self.quiz.check_answer("False")
        self.give_feedback(check)

    def give_feedback(self,check):
        if (check):
            self.canvas.config(background="green")
            self.score["text"] = f"Score: {self.quiz.score}"
        else:
            self.canvas.config(background="red")
        self.window.after(1000,func=self.get_next_question)


