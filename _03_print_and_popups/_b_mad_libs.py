from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # Put this sentence in a pop-up message box:
    # "If you find yourself having to cross a piranha-infested river, here's how to do it..."
    messagebox.showinfo(message = "If you find yourself having to cross a pirahna-infested river, here's how to do it...")
                        # Get the player to enter an adjective
    adj = simpledialog.askstring(prompt = "Enter adjective.", title = None)
                        # Get the player to enter a type of liquid
    liq = simpledialog.askstring(prompt = "Enter liquid.", title = None)
    # Get the player to enter a body part
    bp = simpledialog.askstring(prompt="Enter body part.", title=None)
    # Get the player to enter a verb
    verb = simpledialog.askstring(prompt = "Enter verb.", title = None)
    # Get the player to enter a place
    pla = simpledialog.askstring(prompt = "Enter place.", title = None)
    # The story below has has been written as a group of Strings joined
    # together by + signs. The story contains place holders, indicated
    # by [** **] which you need to replace with the values entered by the
    # player.
    # Hint: You will need to add more + signs to join the variables to the
    #       other parts of the story.

    story = (
        f"Piranhas are more {adj} during the day, so cross the river at\n"
        f"night. Piranhas are attracted to fresh {liq} and will most\n"
        f"likely take a bite out of your {bp} if you {verb}. Whatever\n"
        f"you do, if you have an open wound, try to find another way to get "
        f"back to the {pla}. Good luck!"
    )

    # Make a pop-up that contains the final story. The \n escape characters add
    # line breaks to the story. If you need to, move them around to make your
    # story look better in the pop-up
    messagebox.showinfo(message = f"Piranhas are more {adj} during the day, so cross the river at\n"
        f"night. Piranhas are attracted to fresh {liq} and will most\n"
        f"likely take a bite out of your {bp} if you {verb}. Whatever\n"
        f"you do, if you have an open wound, try to find another way to get "
        f"back to the {pla}. Good luck!")

    # If you want to write your own Madlib story, just change the story variable
    # and ask the player different questions.

    # Run the window's .mainloop() method

    pass
