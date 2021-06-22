from tkinter import *
import random

global question_answer
names_list = []
asked = []
score = 0 

question_answer = { 
      1: [
        "What is Mental Health?",
        'Its a game',
        'Its a sport', 'A state of well-being',
        'I have no idea', 'Some type of food',
        'A state of well-being', 3
    ],
    2: [
        "How does Mental Health affect you?",
        'Effects how you feel',
        'Effects how you act',
        'Effects how we handle stress',
        'Effects how we make choices', 'all of them',
        'all of them', 5
    ],
    3: [
        "Why is Mental Health important?", 'Its not important', 'Becuase its an important stage in life',
        'Mental health is irrelevant', 'No idea', 'Mental health is important but not important enough for people to care about', 'Becuase its an important stage in life', 2
    ],
    4: [
        "Which ways will result in a poor Mental Health?", 'Trauma', 'Childhood abuse',
        'Loneliness', 'All of them will result in a poor mental health', 'social isolation', 'All of them will result in a poor mental health', 4
    ],
    5: [
        "What are ways to deal with a poor mental health?", 'stay isolated',
        'social isolation',
        'Staying active and Drinking and eating well while also hanging out with friends',
        'Staying quiet and not asking for help', 'Listening to music',
        'Staying active and Drinking and eating well while also hanging out with friends',
        3
    ],
    6: [
        "What ages are most affected by Mental Health?",
        'Babies', 
        'Ages 50 and above', 
        'Teenagers aged from 13 to 17',
        'Young Adults aged 18 to 25', 'Adults aged 29 to 49', 'Young Adults aged 18 to 25', 4
    ],
    7: [
        "How many people call the Health line In Newzealand each year due to depression or Mental Health issues?",
        'Around 6 and half thousand people', 
        '44,000 people', 
        '120,000 people', 
        'no people',
        '100 people', 
        'Around 6 and half thousand people', 
        1],
    8:[
        "What can you do if you need help?", 'Call the NZ Health line 0800 611 116', 'Not ask for help', 'Be lonely', 'Self isolate', 'Listen to sad music', 'Call the NZ Health line 0800 611 116' , 1],
} 


def randomiser():
    global qnum  #the question number we have 10 for 10 keys for dictionary
    qnum = random.randint(1, 9)
    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        randomiser() 
          
class MainScreen:
    def __init__(self, master):
        self.master = master
        master.title("Quiz on Mental Health")

        background_color = "blue" 

        self.quiz_frame = Frame(master,
                                bg=background_color,
                                padx=100,
                                pady=100)
        self.quiz_frame.grid()

        self.heading_label = Label(self.quiz_frame,
                                   text="Mental Health Quiz 2021",
                                   font=("Osaka", "25"),
                                   bg=background_color,
                                   fg='black',
                                   padx=20,
                                   pady=20)
        self.heading_label.grid(row=1, padx=24, pady=24)

        self.entry_box = Entry(self.quiz_frame)
        self.entry_box.grid(row=2, padx=22 ,pady=22)

        #start button
        self.start_button = Button(self.quiz_frame,
                                   text="Start Quiz",
                                   font=("Osaka", "14", "bold"),
                                   fg='black',
                                   bg="white",
                                   command=self.name_collection)
        self.start_button.grid(row=3, padx=25, pady=25)

        self.Quit_Button = Button(self.quiz_frame,
                                  text="Exit",
                                  font=("Osaka", "15", "bold"),
                                  fg='black',
                                  bg="white",
                                  command=self.end_screen)
        self.Quit_Button.grid(row=6, padx=20, pady=20)


    def end_screen(self):
        root.withdraw()
        open_endscreen = End(root)

    def name_collection(self):
        name = self.entry_box.get()
        names_list.append(name)
        self.quiz_frame.destroy()
        Quiz(root) 
  
  
  
class Quiz:
    def __init__(self, master):
        self.master = master
        master.title("Quiz on Mental Health")

        background_color = "blue"

        self.quiz_frame = Frame(master,
                                bg=background_color,
                                padx=100,
                                pady=100)
        self.quiz_frame.grid()

        self.question_label = Label(self.quiz_frame,
                                    text=question_answer[qnum][0],
                                    font=("Osaka", "18"),
                                    fg='black',
                                    bg="white")
        self.question_label.grid(row=1, padx=20, pady=20)

        self.var1 = IntVar()

        self.rb1 = Radiobutton(self.quiz_frame,
                               text=question_answer[qnum][1],
                               font=("Osaka", "14"),
                               bg="blue",
                               value=1,
                               padx=10,
                               pady=10,
                               variable=self.var1,
                               indicator=0,
                               background="white",
                               fg="black")
        self.rb1.grid(row=2, sticky=W)

        self.rb2 = Radiobutton(self.quiz_frame,
                               text=question_answer[qnum][2],
                               font=("Osaka", "14"),
                               bg="blue",
                               value=2,
                               padx=10,
                               pady=10,
                               variable=self.var1,
                               indicator=0,
                               background="white",
                               fg="black")
        self.rb2.grid(row=3, sticky=W)

        self.rb3 = Radiobutton(self.quiz_frame,
                               text=question_answer[qnum][3],
                               font=("Osaka", "13"),
                               bg="blue",
                               value=3,
                               padx=10,
                               pady=10,
                               variable=self.var1,
                               indicator=0,
                               background="white",
                               fg="black")
        self.rb3.grid(row=4, sticky=W)

        self.rb4 = Radiobutton(self.quiz_frame,
                               text=question_answer[qnum][4],
                               font=("Osaka", "13"),
                               bg="white",
                               value=4,
                               padx=10,
                               pady=10,
                               variable=self.var1,
                               indicator=0,
                               background="white",
                               fg="black")
        self.rb4.grid(row=5, sticky=W)

        self.rb5 = Radiobutton(self.quiz_frame,
                               text=question_answer[qnum][5],
                               font=("Osaka", "13"),
                               bg="white",
                               value=5,
                               padx=10,
                               pady=10,
                               variable=self.var1,
                               indicator=0,
                               background="white",
                               fg="black")
        self.rb5.grid(row=6, sticky=W)

        self.confirm_button = Button(self.quiz_frame,
                                     text="Confirm",
                                     font=("Osaka", "13", "bold"),
                                     bg="white",
                                     command=self.test_progress)

        self.confirm_button.grid(row=7, padx=5, pady=5)

        self.end_quiz = Button(self.quiz_frame,
                               text="End Quiz",
                               font=("Osaka", "13", "bold"),
                               bg="white",
                               command=self.end_screen)
        self.end_quiz.grid(row=9, padx=10, pady=10)

        self.score_label = Label(self.quiz_frame,
                                 text="SCORE",
                                 font=("Osaka", "16"),
                                 bg=background_color,
                                 fg="black")
        self.score_label.grid(row=8, padx=10, pady=1)

    def question_setup(self):
        randomiser()
        self.var1.set(0)
        self.question_label.config(text=question_answer[qnum][0])
        self.rb1.config(text=question_answer[qnum][1])
        self.rb2.config(text=question_answer[qnum][2])
        self.rb3.config(text=question_answer[qnum][3])
        self.rb4.config(text=question_answer[qnum][4])
        self.rb5.config(text=question_answer[qnum][5])

    def test_progress(self):
        global score
        scr_label = self.score_label
        choice = self.var1.get()
        if len(asked) > 9:
            if choice == question_answer[qnum][6]:
                score += 1
                scr_label.config(text=score)
                self.confirm_button.config(text="Confirm")

            else:
                score += 0
                scr_label.config(text="The correct answer was: " +
                                 question_answer[qnum][6])
                self.confirm_button.config(text="Confirm")

        else:
            if choice == 0:
                self.confirm_button.config(
                    text=
                    "Try Again Please!, An Option was not selected!")
                choice = self.var1.get()
            else:
                if choice == question_answer[qnum][6]:
                    score += 1
                    scr_label.config(text=score)
                    self.confirm_button.config(text="Confirm")
                else:
                    print(choice)
                    score += 0
                    scr_label.configure(text="The correct answer was: " +
                                        question_answer[qnum][6])
                    self.confirm_button.config(text="Confirm")
                    self.question_setup()

    def end_screen(self):
        root.withdraw()
        open_endscreen = End(root)

class End:
    def __init__(self,master):
        background = "black"


        self.end_box = Toplevel(root)
        self.end_box.title("The Exit Box")

        self.end_frame = Frame(self.end_box,
                               width=1000,
                               height=1000,
                               bg=background,
                               )
        self.end_frame.grid()

        self.end_heading = Label(self.end_frame,
                            text='Good Job',
                            font=('Osaka', 22, 'bold'),
                            bg=background,
                            pady=15)
        self.end_heading.grid(row=0)

        self.exit_button = Button(self.end_frame,
                             text='Exit',
                             width=10,
                             bg='white',
                             font=('Osaka', 15, 'bold'),
                             command=self.close_end)
        self.exit_button.grid(row=4, pady=20)

    def close_end(self):
        self.end_box.destroy()
        root.withdraw()


randomiser()
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz on Mental Health")
    quiz_instance = MainScreen(root)
    root.mainloop()

root = Tk()
root.title("Quiz on Mental Health")
mainscreen = MainScreen(root)
root.mainloop()