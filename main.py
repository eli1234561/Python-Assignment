from tkinter import *
import random

global question_answer
names_list = []
asked = []
score = 0 

question_answer = {
    1: [
        "What is Mental Health",
        'Mental Health is about my physical health',
        'Some game', 'Something to do with food',
        'A important issue in todays world', 'A fruit',
        'A Sport', 1
    ],
    2: [
        "How does Mental Health affect you?",
        'How you handle stress',
        'How you act',
        'How you feel',
        'Relating to others', 'all of them',
        'all of them', 5
    ],
    3: [
        "Which country has the most Mental Health problems?", 'Brazil', 'China',
        'United States of America', 'Germany', 'Russia', 'China', 2
    ],
    4: [
        "Which country creates the least pollution?", 'New Zealand', 'Finland',
        'France', 'Sweden', 'Australia', 'Sweden', 4
    ],
    5: [
        "How do you look after your Mental Health?", 'Staying Active',
        'Keep in touch',
        'Ask for help',
        'Doing things that make you happy', 'Stay in contact with friends and socialise with them',
        'Sit alone and do not tell anyone',
        3
    ],
    6: [
        "Which one of these causes the most Mental health problems in todays society?",
        'Being Bullied online', 
        'Being bullied at work or school', 
        'Dealing with health problems alone',
        'Family Arguments', 'Stressful life situations', 'Financial Problems', 4
    ],
    7: [
        "How many people seek public help everyday due to bullying caused by Cyber bullying",
        '434343434 people', 
        '38923983 people', 
        '397492379 people', 
        '4444444444444 people',
        '637228 people', 
        '565656 people', 
        1],
    8:[
        "unknown", 'hello1', 'hello2', 'hello3', 'hello4', 'hello5', 'hello1', 1],
    9:[
        "unknown", 'hello1', 'hello2', 'hello3', 'hello4', 'hello5', 'hello1', 1],
    10:[
        "Questions to be done", 
     'hello1', 'hello2', 'hello3', 'hello4', 'hello5', 'hello1', 1]
} 

def randomiser():
    global qnum  #the question number is the key in the dictionary question_answers, we have 10 keys (10 questions)
    qnum = random.randint(1, 10)
    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        randomiser()


class MainScreen:
    def __init__(self, master):
        self.master = master
        master.title("Quiz on Mental Health")

        background_color = "blue"

        self.quiz_frame = Frame(master,bg=background_color,padx=130,pady=100)
        self.quiz_frame.grid()

        self.heading_label = Label(self.quiz_frame,text="Mental Health", font=("Pacifico", "39"),       
                                   bg=background_color,
                                   fg='white',
                                   padx=20,
                                   pady=20)
        self.heading_label.grid(row=1, padx=20, pady=20)

        self.entry_box = Entry(self.quiz_frame)
        self.entry_box.grid(row=2, padx=20, pady=20)

        #start button
        self.start_button = Button(self.quiz_frame,
                                   text="Start",
                                   font=("Pacifico", "16", "bold"),
                                   fg='white',
                                   bg="cyan",
                                   command=self.name_collection)
        self.start_button.grid(row=3, padx=20, pady=20) 
        
        #quit button
        self.Quit_Button = Button(self.quiz_frame,
                                  text="Quit",
                                  font=("Pacifico", "13", "bold"),
                                  fg='black',
                                  bg="cyan")
        self.Quit_Button.grid(row=5, padx=20, pady=20)

    def name_collection(self):
        name = self.entry_box.get()
        names_list.append(name)
        self.quiz_frame.destroy()
        Quiz(root)


class Quiz:
    def __init__(self, master):
        self.master = master
        master.title("Quiz on Mental Health")

        background_color = "black"

        self.quiz_frame = Frame(master,
                                bg=background_color,
                                padx=100,
                                pady=100)
        self.quiz_frame.grid()

        self.question_label = Label(self.quiz_frame,
                                    text=question_answer[qnum][0],
                                    font=("Pacifico", "16"),
                                    fg='black',
                                    bg="cyan")
        self.question_label.grid(row=1, padx=20, pady=20)

        self.var1 = IntVar()

        self.rb1 = Radiobutton(self.quiz_frame,
                               text=question_answer[qnum][1],
                               font=("Helvetica", "12"),
                               bg="cyan",
                               value=1,
                               padx=10,
                               pady=10,
                               variable=self.var1,
                               indicator=0,
                               background="cyan",
                               fg="black")
        self.rb1.grid(row=2, sticky=W)

        self.rb2 = Radiobutton(self.quiz_frame,
                               text=question_answer[qnum][2],
                               font=("Helvetica", "12"),
                               bg="cyan",
                               value=2,
                               padx=10,
                               pady=10,
                               variable=self.var1,
                               indicator=0,
                               background="cyan",
                               fg="black")
        self.rb2.grid(row=3, sticky=W)

        self.rb3 = Radiobutton(self.quiz_frame,
                               text=question_answer[qnum][3],
                               font=("Helvetica", "12"),
                               bg="cyan",
                               value=3,
                               padx=10,
                               pady=10,
                               variable=self.var1,
                               indicator=0,
                               background="cyan",
                               fg="black")
        self.rb3.grid(row=4, sticky=W)

        self.rb4 = Radiobutton(self.quiz_frame,
                               text=question_answer[qnum][4],
                               font=("Helvetica", "12"),
                               bg="cyan",
                               value=4,
                               padx=10,
                               pady=10,
                               variable=self.var1,
                               indicator=0,
                               background="cyan",
                               fg="black")
        self.rb4.grid(row=5, sticky=W)

        self.rb5 = Radiobutton(self.quiz_frame,
                               text=question_answer[qnum][5],
                               font=("Helvetica", "12"),
                               bg="cyan",
                               value=5,
                               padx=10,
                               pady=10,
                               variable=self.var1,
                               indicator=0,
                               background="cyan",
                               fg="black")
        self.rb5.grid(row=6, sticky=W)

        self.confirm_button = Button(self.quiz_frame,
                                     text="Confirm",
                                     font=("Helvetica", "13", "bold"),
                                     bg="cyan",
                                     command=self.test_progress)

        self.confirm_button.grid(row=7, padx=5, pady=5)

        self.end_quiz = Button(self.quiz_frame,
                               text="End Quiz",
                               font=("Helvetica", "13", "bold"),
                               bg="cyan",
                               command=self.end_screen)

        self.score_label = Label(self.quiz_frame,
                                 text="SCORE",
                                 font=("Tw Cen MT", "16"),
                                 bg=background_color)
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
                                 question_answer[qnum][5])
                self.confirm_button.config(text="Confirm")

        else:
            if choice == 0:
                self.confirm_button.config(
                    text=
                    "Try Again, You didn't select an option then submit again")
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
                                        question_answer[qnum][5])
                    self.confirm_button.config(text="Confirm")
                    self.question_setup()

    def end_screen(self):
        root.withdraw()
        open_endscreen = End()
        End(root)


class End:
    def __init__(self):
        background = "black"

        self.end_box = Toplevel(root)
        self.end_box.title("End Box")

        self.end_frame = Frame(self.end_box,
                               width=1000,
                               height=1000,
                               bg=background)

        end_heading = Label(self.end_frame,
                            text='Well Done',
                            font=('Tw Cent Mt', 22, 'bold'),
                            bg=background,
                            pady=15)
        end_heading.grid(row=0)

        exit_button = Button(self.end_frame,
                             text='Exit',
                             width=10,
                             bg='cyan',
                             font=('Tw Cent Mt', 12, 'bold'),
                             command=self.close_end)
        exit_button.grid(row=4, pady=20)

    def endScreen(self):
        root.withdraw()
        name = names[0]
        file = open("leaderboard.txt", "a")
        file.write(str(score))
        file.write(" - ")
        file.write(name + "\n")
        file.close()

        inputFile = open("leaderBoard.txt", 'r')
        lineList = inputFile.readlines()
        lineList.sort()
        top = []
        top10 = (lineList[-10:])
        for line in top10:
            point = line.split(" - ")
            top.append(int(point[0]), point[1])
        file.close()
        top.sort()
        top.reverse()
        return_string = ""
        for i in range(len(top)):
            return_string += "{} - {}\n".format(top[i][0], top[i][1])
        print(return_string)
        open_endscrn = End()
        open_endscrn.listLabel.config(text=return_string)
        self.listLabel = Label(self.end_frame,
                               text="1st Place Available",
                               font=('Tw Cent MT', 18),
                               width=40,
                               bg=background,
                               padx=10,
                               pady=10)
        self.listLabel.grid(column=0, row=2)

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