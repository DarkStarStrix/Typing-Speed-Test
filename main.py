# make a graphical user interface to test the users typing speed

from tkinter import *
from tkinter import messagebox
import random
import time

import start as start

# create the window
window = Tk()
window.title("Typing Speed Test")
window.geometry("500x500")
window.config(bg="black")

# create the variables
user_input = StringVar()
words = ['programming', 'coding', 'python', 'java', 'javascript', 'html', 'css', 'php', 'c++', 'c#', 'ruby', 'swift',
         'kotlin', 'sql', 'mysql', 'database', 'django', 'flask', 'react', 'angular', 'vue', 'nodejs', 'express',
         'mongodb', 'nosql', 'firebase', 'git', 'github', 'bitbucket', 'heroku', 'aws', 'azure', 'linux', 'ubuntu',
         'windows', 'macos', 'raspberry pi', 'arduino', 'raspbian', 'raspberry pi os', 'raspberry pi os lite',
         'raspberry pi os full', 'raspberry pi os desktop', 'raspberry pi os desktop with recommended software',
         'raspberry pi os desktop with recommended software',
         'raspberry', ]
random.shuffle(words)
word = words[0]
count = 0

word_label = Label(window, text=word, font=("Arial", 30), bg="black", fg="white")
start_button = Button(window, text="Start", font=("Arial", 20), bg="black", fg="white", command=start)
time_label = Label(window, text="Time: 0 seconds", font=("Arial", 20), bg="black", fg="white")


def start():
    global word
    word_label.config(text=word)
    start_button.config(state=DISABLED)
    start_time = time.time()
    while True:
        if user_input.get() == word:
            end_time = time.time()
            total_time = end_time - start_time
            time_label.config(text=f"Time: {total_time} seconds")
            messagebox.showinfo("Success", "You typed the word correctly!")
            break
        else:
            messagebox.showerror("Error", "You typed the word incorrectly!")
            break


def reset():
    global word, count
    count += 1
    word = words[count]
    word_label.config(text=word)
    user_input.set("")
    start_button.config(state=NORMAL)
    time_label.config(text="Time: 0 seconds")


# create the widgets
user_input_entry = Entry(window, textvariable=user_input, font=("Arial", 20), bg="black", fg="white")
reset_button = Button(window, text="Reset", font=("Arial", 20), bg="black", fg="white", command=reset)

# place the widgets
word_label.place(x=150, y=100)
user_input_entry.place(x=150, y=200)
start_button.place(x=150, y=300)
time_label.place(x=150, y=400)
reset_button.place(x=250, y=300)

# run the window
window.mainloop()

# explain the code
# import the modules
# create the window
# create the variables
# create the widgets
# place the widgets
# run the window
