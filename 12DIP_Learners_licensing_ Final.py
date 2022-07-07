#12DIP
#Cuda Wong 2022
#LNI
#Learners licensing Final

#Imports
import time
from playsound import playsound
import ast
import random
import emoji
import os

#This is the dictionary that will have the the questions in random order
quiz = {

}

#Varibles
name = ""
age = 0
age_verify = True
age_confirm = ""
name_verify = ""
num_of_Q_verify = True
num_of_Q_confirm = ""
num_of_Q = 0
user_response = ""
quit_verify = ""
test = True
score = 0
x = 0
question_count = 1
Qs_till_end = 0
leaderboard_consent = True
see_leaderboard = ""
consent = ""
percentage = 0

def main(): #Structures the order main code 
    intro()
    start()
    end()
    
def sleep(): #function that allows for the gap (new line gap) between sentences and a time delay
    time.sleep(0.5) #time wait before starting loop
    for i in range(2): #prints twice
        print("") #blank
        time.sleep(0.25) #time between each 'blank'

def dictionary(): #fetches the external text file and makes it into dictionary .py file
    global questions
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "Questions.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    with open(abs_file_path) as q: 
        question_file = q.read() #tells code to read the questions
        questions = ast.literal_eval(question_file) #evaluates questions converts into a dictionary

def shuffle(): #this function shuffles dictionaries
  global quiz, x, num_of_Q
  quiz.clear()  #ensures that the quiz dictionary is clear incase of retry
  while True:
    if x == num_of_Q: #will gather questions until the users requested amount of questions are choosen at random
        break
    else:
      key, value = random.choice(list(questions.items()))  #chooses a question and answer at random
      quiz.update({key: value}) #adds the question and answer to the quiz
      questions.pop(key, value)  #removes the question and answer that are not used in quiz
      x += 1
    
def intro(): #This function starts off the Programme and it ask for users name, age, and number of questions they would like to do
    global age_verify, num_of_Q_verify, name, num_of_Q, age
    print("Learners licensing test") #Title
    sleep()
    while name == "": #Loops when Invalid response is given
        name = input("Please enter your name: ").strip().title() #asking user for thier name
        sleep()
        name_verify = input("{}, is your name correct? (Yes or No) ".format(name)).strip().capitalize() #confims if name is correct
        sleep()
        if name_verify == "No": #Incorrect name
            print("Ok try again")
            sleep()
            name = ""
            
        elif name_verify == "Yes": #Correct name
            print("Hello, {}".format(name))
            sleep()
        
        else: #Invalid Response
            print("Please enter with 'Yes' or 'No'")
            sleep()
            name = ""
            
    while age_verify is True: #Loops when Invalid response is given
        try:
            while True:
                age = int(input("What is your age (number form) ")) #Asking user for thier age
                sleep()
                age_confirm = input("{}, is your age correct {}? (Yes or No) ".format(age, name)).strip().capitalize()
                
                if age_confirm == "Yes": #user says yes
                    sleep()
                    break

                elif age_confirm == "No": #user says no
                    sleep()
                    print("Ok try again {}".format(name))
                    sleep()

                else: #user doesnt enter valid response
                    sleep()
                    print("Please enter with a vaild response 'Yes' or 'No'")
                    sleep()
            
            if age < 16: #Age is under 16
                print("Since you are {}, you cannot take the test yet, however you can still practice".format(age))
                sleep()
                age_verify = False
                
            elif age >= 16:#Age is 16 or over
                print("Since you are {}, you are eligible to take the test".format(age))
                sleep()
                age_verify = False
                
            else: #Invalid Response
                print("Your age is invaild please type your age again")
                sleep()
                
        except ValueError: #If user gets ValueError (Puts down a string or float)
            sleep()
            print("Your age is invaild please type your age again")
            sleep()

    while num_of_Q_verify is True: #Loops when Invalid response is given
        try:
            while True:
                num_of_Q = int(input("How many questions would you like too do (35 questions max) (35 questions is the number of questions you do in the real test) ")) #Asking user for number of questions to answer
                sleep()
                num_of_Q_confirm = input("You are going to answer {} questions. Is this correct? (Yes or No) ".format(num_of_Q)).strip().capitalize() #Confims if the users input of Num_of_Q is correct
                if num_of_Q_confirm == "Yes": #user says yes
                    sleep()
                    break

                elif num_of_Q_confirm == "No": #user says no
                    sleep()
                    print("Ok try again {}".format(name))
                    sleep()
                    num_of_Q_verify = True

                else: #user enters invaild response
                    sleep()
                    print("Please enter with 'Yes' or 'No'")
                    sleep()
                    num_of_Q_verify = True
                
            if num_of_Q in range (1, 36): #User enters number between 1 and 35
                print("Thanks, You are going to answer {} questions".format(num_of_Q))
                sleep()
                num_of_Q_verify = False
            elif num_of_Q > 35: #User enters number over 35
                print("You have put in to many questions, try again")
                sleep()
            elif num_of_Q <= 0: #user enters number under 1
                print("You have put in not enough questions, try again")
                sleep()
            else:
                print("Please enetr a vaild response")
                
        except ValueError: #Users gets ValueError (enters a string or float)
            sleep()
            print("Your number of questions is invaid try again, (enter the number)")
            sleep()

def start(): #This function starts the quiz 
    global quit_verify, question_count, num_of_Q, Qs_till_end, test, name, user_response
    dictionary() #Imports dictionary
    shuffle() #Shuffles questions in dictionary
    Qs_till_end = num_of_Q
    while Qs_till_end > 0: #Loop untill the number of questions user has put down has been answered
        while test is True: #loop untill user wants to quit the quiz
            for question, answers in quiz.items(): #Loops for the key and value in the dictionary 
                print("Question {}".format(question_count)) #Shows question count
                sleep()
                print(question, "\n") #Prints question in the 'questions.text' dictionary
                while True: #loop for if user wants to quit but then decides not too
                    user_response = input("Please enter A, B, C or D on which one you think is correct or enter Q to quit the quiz ").strip().capitalize() #user answers the question
                    if user_response in ["A", "B", "C", "D", "Q"]: #user enters a valid response
                        
                        if user_response == "Q": #user wants to quit (pressed 'Q')
                            sleep()
                            quit_verify = input("You are going to quit the quiz, are you sure you want to quit (Yes or No) ").strip().capitalize() #confims if user wants to quit
                            if quit_verify == "Yes": #user says yes
                                sleep()
                                print("Your score was {} out of {} ({:.2f}%)".format(score, num_of_Q, percentage))
                                sleep()
                                print("Ok goodbye\n{}".format(name))
                                test = False #end loop for quiz
                                quit()
                            elif quit_verify == "No": #User says 'No' and goes back to answering question
                                sleep()
                            elif quit_verify != "Yes" or "No": #user gives invaild response
                                sleep()
                            else:
                                sleep()
                            
                        elif user_response == answers: #user answers correctly
                            sleep()
                            correct()
                            question_count = question_count + 1
                            Qs_till_end = Qs_till_end - 1
                            break
        
                        elif user_response != answers: #user answers incorrectly
                            sleep()
                            incorrect()
                            question_count = question_count + 1
                            Qs_till_end = Qs_till_end - 1
                            break
                                
                        else:
                            sleep()
                            print("Please enter a valid response (A, B, C, D or Q)")
                            sleep()
                            
                    else: #user enters invalid response (Not A, B, C, D or Q)
                        sleep()
                        print("Please enter a valid response (A, B, C, D or Q)")
                        sleep()
                        
                else:
                    break
            else:
                break
        else:
            break


def incorrect(): #function that is used when user gets a question incorrect
    global score, percentage
    percentage = 100 * (score/num_of_Q) #Calcuates percentage
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "Wrong_Buzzer.mp3"
    abs_file_path = os.path.join(script_dir, rel_path)
    playsound(abs_file_path) #plays incorrect sound
    print("Incorrect", emoji.emojize(":cross_mark:")) #Incorrect with cross emoji
    sleep()
    print("Your score is currently {} out of {} ({:.2f}%)".format(score, num_of_Q, percentage)) #shows current score
    sleep()


def correct(): #function that is used when user gets a question correct
    global score, percentage
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "Correct_Buzzer.mp3"
    abs_file_path = os.path.join(script_dir, rel_path)
    playsound(abs_file_path) #Plays Correct sound
    print("Correct", emoji.emojize(":check_mark_button:")) #Crorrect with a checkmark emoji
    sleep()
    score = score + 1 #Adds 1 point to score
    percentage = 100 * (score/num_of_Q) #Calcuates percentage
    print("1 point has been added to your score") #Tells user that 1 point has been added to score
    sleep()
    print("Your score is currently {} out of {} ({:.2f}%)".format(score, num_of_Q, percentage)) #shows current score
    sleep()
      
def end(): #function that is used for when the user quits or its the end of the quiz and gives out the score
    print("You have finsihed the test")
    sleep()
    print("You got a score of {} out of {} ({:.2f}%)".format(score, num_of_Q, percentage))
    if percentage < 91.43: #user would fail if they did actual test
        sleep()
        print("You would of failed the real test, you need 91.43% to pass (32/35, in real test)")
        sleep()
        print("Better luck next time")
        sleep()
        leaderboard()

    elif percentage >= 91.43: #user would pass if they did actual test
        sleep()
        print ("You would of passed the test, Congratulations (91.43% to pass)")
        sleep()
        leaderboard()
        
    sleep()
    print("Goodbye and goodluck\n{}".format(name)) #Last print statment (end of code)

def leaderboard(): #this function allows the user to chooses to save their score to the leaderboard
    global leaderboard_consent, consent
    while leaderboard_consent is True: #If user gives invaild response will loop back here
        consent = input("Would you like to submit your score to the leaderboard? (Yes or No) ").strip().capitalize() #Ask if user they would like to submit thier score
        if consent == "Yes": #user says 'Yes'
            script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
            rel_path = "leaderboard.txt"
            abs_file_path = os.path.join(script_dir, rel_path)
            save_leaderboard = open(abs_file_path, "a") #opens the leaderboard file
            save_leaderboard.write("Name- {}\nAge- {}\nNumber of questions- {}\nScore- {} out of {}\nPercentage- {:.2f}%\n\n".format(name, age, num_of_Q, score, num_of_Q, percentage)) #adds the to the leaderboard file: name, age, number of questions, score and percentage)
            save_leaderboard.close()  #closes the leaderboard file
            sleep()
            print("Ok done")
            viewleaderboard()
            leaderboard_consent = False #End loop
          
        elif consent == "No": #user says 'No'
            sleep()
            print("Ok Thank you")
            viewleaderboard()
            leaderboard_consent = False #End loop
            
        else: #User gives invalid response (Not 'Yes' or 'No'
            sleep()
            print("Please answer with 'Yes' or 'No'")
            sleep()
            leaderboard_consent = True #Loop back

def viewleaderboard(): #Function that ask user if they would like to see the leaderboard
    global see_leaderboard
    while True: 
        sleep()
        see_leaderboard = input("Would you like to see the leaderboard standings currently? (Yes or No) ").strip().capitalize() #ask user if they would like to see the leaderboard
        if see_leaderboard == "Yes": #User says 'Yes'
            script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
            rel_path = "leaderboard.txt"
            abs_file_path = os.path.join(script_dir, rel_path)
            with open(abs_file_path, "r") as l: #opens the leaderboard file as a read file
                print(l.read()) #Displays the leaderboard file
                break

        elif see_leaderboard == "No": #User says 'No'
            sleep()
            print("Ok Thank you")
            break
            
        else: #user gives invalid repsonse (Not 'Yes' or 'No') and loops back to users input of see_leaderboard
            sleep()
            print("Please answer with 'Yes' or 'No'")


#Run main code
main()
