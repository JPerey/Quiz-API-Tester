THEME_COLOR = "#375362"
canvas_text = ("Arial", 20, "italic")
score_text = ("Arial", 10)
from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.quiz_end = False
        self.score = 0
        self.answer = bool
        self.window = Tk()
        self.window.title("Trivia Database Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.true_btn_img = PhotoImage(file="images/true.png")
        self.false_btn_img = PhotoImage(file="images/false.png")

        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.canvas_text = self.canvas.create_text(150, 125, text=" quiz text goes here", fill=THEME_COLOR,
                                                   font=canvas_text, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.true_btn = Button(image=self.true_btn_img, highlightthickness=0, command=self.send_answer_true)
        self.true_btn.grid(column=0, row=2)
        self.false_btn = Button(image=self.false_btn_img, highlightthickness=0, command=self.send_answer_false)
        self.false_btn.grid(column=1, row=2)

        self.score_label = Label(text=f"Score= {self.score}", font=score_text, bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        # self.change_white()
        question_text = self.quiz.next_question()
        self.canvas.itemconfig(self.canvas_text, text=question_text)

    def send_answer_true(self):
        if self.quiz_end:
            pass
        else:
            self.score, self.answer = self.quiz.check_answer("True")
            self.score_label["text"] = f"Score= {self.score}"
            self.give_feedback(self.answer)

    def send_answer_false(self):
        if self.quiz_end:
            pass
        else:
            self.score, self.answer = self.quiz.check_answer("False")
            self.score_label["text"] = f"Score= {self.score}"
            self.give_feedback(self.answer)

    def give_feedback(self, correct_answer):
        if correct_answer:
            print(f"answer: {self.answer}")
            self.canvas.configure(bg="green")
            self.window.after(1000, self.change_white)
            still_questions = self.quiz.still_has_questions()
            if still_questions:
                self.window.after(1000, self.get_next_question)
            else:
                self.quiz_end = True
                self.canvas.itemconfig(self.canvas_text, text="You have reached the end of the quiz!")
        else:
            print(f"answer: {self.answer}")
            self.canvas.configure(bg="red")
            self.window.after(1000, self.change_white)
            still_questions = self.quiz.still_has_questions()
            if still_questions:
                self.window.after(1000, self.get_next_question)
            else:
                self.quiz_end = True
                self.canvas.itemconfig(self.canvas_text, text="You have reached the end of the quiz!")

    def change_white(self):
        self.canvas.configure(bg="white")
