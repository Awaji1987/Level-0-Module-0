from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    sco = 0
    # ASK A QUESTION AND CHECK THE ANSWER
    nap = simpledialog.askstring(title="FNAF", prompt="How did Napoleon die?")
    #      // 2.  Ask the user a question 
    nap = simpledialog.askstring(title="FNAF", prompt="How did Napoleon die")
    #      // 3.  Use an if statement to check if their answer is correct
    if nap == "radioactive wallpaper"
    #      // 4.  if the user's answer was correct, add one to their score 
    sco = +1
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    sco = -1
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    str()
    # Run the window's .mainloop() method
