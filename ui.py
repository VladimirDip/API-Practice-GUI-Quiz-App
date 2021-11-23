from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('arial', 20, 'italic')


class QuizInerface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizlett")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='Something text',
            font=FONT, fill=THEME_COLOR
        )
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        self.score_label = Label(text='Score: 0', font=('arial', 10, 'italic'), bg=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0, padx=20, pady=20)

        IMAGE_TRUE = PhotoImage(file='./images/true.png')
        IMAGE_FALSE = PhotoImage(file='./images/false.png')

        self.button_true = Button(image=IMAGE_TRUE, command=self.choise_true, highlightthickness=0)
        self.button_true.grid(column=0, row=2, padx=20, pady=20)

        self.button_false = Button(image=IMAGE_FALSE, command=self.choise_false, highlightthickness=0)
        self.button_false.grid(column=1, row=2, padx=20, pady=20)

        self.get_next_questions()

        self.window.mainloop()

    def choise_true(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def choise_false(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_questions)

    def get_next_questions(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"score: {self.quiz.score}")
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.end_game()

    def end_game(self):
        self.score_label.config(text=f"score: {self.quiz.score}")
        self.canvas.config(bg='white')
        self.canvas.itemconfig(self.text, text="You've completed the quiz\n"
                                               f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
        self.button_true.config(state="disabled")
        self.button_false.config(state="disabled")
