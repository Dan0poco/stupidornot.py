from tkinter import *

# Initialize player points
player_point = 0

# Function to update the points label
def update_points():
    points.set(f"Player Points: {player_point}")

# Create the main window
window = Tk()
window.title("Stupid or Not")

# Create a StringVar to hold the points text
points = StringVar()
points.set(f"Player Points: {player_point}")

label = Label(window, textvariable=points, font=("Helvetica", 24))
label.pack(pady=20)
label.config(bg='#f00015')
window.config(bg='#ff0015')

print()
print("Welcome to my quiz! This quiz is gonna check if you're stupid or not.")
print()
print("Answer yes/no to every question. If you don't know your answer, write something.")

# 1st question
print("So here's the first question")
answer01 = input("Do you have/had good grades in school? --> ").strip().lower()

if answer01 == "yes":
    player_point += 1
    print("Here's the next question")
elif answer01 == "no":
    player_point -= 1
    print("Here's the next question")
else:
    print("Here's the next question")

update_points()  # Update points after each question

# 2nd question
answer02 = input("Do you feel autistic sometimes? --> ").strip().lower()

if answer02 == "yes":
    player_point += 1
    print("Here's the next question")
elif answer02 == "no":
    player_point -= 1
    print("Here's the next question")
else:
    print("Here's the next question")

update_points()  # Update points after each question

# 3rd question
answer03 = input("Do you think that you're smart? --> ").strip().lower()

if answer03 == "yes":
    player_point -= 1
    print("Here's the next question")
elif answer03 == "no":
    player_point += 1
    print("Here's the next question")
else:
    print("Here's the next question")

update_points()  # Update points after each question

# 4th question
answer04 = input("Do you feel sometimes unmotivated? --> ").strip().lower()

if answer04 == "yes":
    player_point += 1
elif answer04 == "no":
    player_point -= 1
else:
    print()

update_points()  # Update points after each question

if player_point > 2:
    print("The test results are... You're smart!")
elif player_point <= 2:
    print("The test results are... You're not very smart.")
else:
    print("You're neither dumb nor particularly smart.")

print()
print("Your points were ", player_point)
print()

Exitquestion = input("Type 'f' to exit app --> ")

if Exitquestion == "f":
    exit()
else:
    print("ERROR")
    print()

Exitquestion = input("Type 'f' to exit app --> ")

if Exitquestion == "f":
    exit()
else:
    print("ERROR")

window.mainloop()
