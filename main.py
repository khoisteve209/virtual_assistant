from datetime import *
import pyttsx3
import wikipedia
import webbrowser as wb
from sklearn import *

robot_brain = ""
robot_mouth = pyttsx3.init()
voices = robot_mouth.getProperty("voices")
robot_mouth.setProperty("voice", voices[1].id)
while True:
    you = input("You: ")
    you = you.capitalize()
    if you == "Hello" or you == "hello":
        robot_brain = "Hello"
    elif you == "Daniel radcliff":
        robot_brain = "This is a actor who is Harry Potter in the movie Harry Potter"
    elif "Google" in you:
        search = input("Google search box: ")
        wb.get().open(f"https://www.google.com/search?q={search}")
    elif you == "Ok":
        robot_brain = "Ok"
    elif you == "Harry potter":
        robot_brain = "Harry Potter is a series of seven fantasy novels written by British author J. K. Rowling. The novels chronicle the lives of a young wizard, Harry Potter, and his friends Hermione Granger and Ron Weasley, all of whom are students at Hogwarts School of Witchcraft and Wizardry. The main story arc concerns Harry's struggle against Lord Voldemort, a dark wizard who intends to become immortal, overthrow the wizard governing body known as the Ministry of Magic and subjugate all wizards and Muggles (non-magical people)."
    elif "Youtube" in you:
        wb.get().open("https://www.youtube.com/")
    elif you == "Vietnam":
        robot_brain = wikipedia.summary("Vietnam")
    elif "Fortunate son" in you or "Fortunate Son" in you:
        wb.get().open("https://www.youtube.com/watch?v=ec0XKhAHR5I")
    elif "Soviet union" in you or "Soviet Union" in you:
        robot_brain = wikipedia.summary("Soviet Union")
    elif you == "China":
        robot_brain = wikipedia.summary("China")
    elif you == "":
        robot_brain = "Sorry I can't hear you"
    elif you == "Russia":
        robot_brain = wikipedia.summary("Russia")
    elif you == "Today":
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif you == "President of america":
        robot_brain = "Joe Biden"
    elif you == "Time":
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S second")
    elif "Bye" in you or "Quit" in you:
        break
    else:
        wb.get().open(f"https://www.google.com/search?q={you}")
        robot_brain = "SORRY I DON'T KNOW THE ANSWER TO THIS ONE SO I'LL SEARCH IT USING GOOGLE"
    print(f"You {you}")
    print(f"Robot: {robot_brain}")
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
