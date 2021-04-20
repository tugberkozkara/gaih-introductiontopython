#Final Project
#Write a knowledge competition program.
#It should consist of 10 questions in total.
#Each question will have only one answer.
#Adjust the answers of the questions according to case sensitivity.
#Each question should be worth 10 points.
#If User answers 5 or fewer questions, it will be considered unsuccessful.
#If the user answers more than 5 questions correctly, it will considered successful.

print("---Welcome to Non-Millionaire Quiz---\n" +
"You need to answer questions properly, by paying attention to case sensitivity!\n" +
"If you cant give 5 or more correct answers, you won't win anything.\n"+
"And if you can, you still won't win anything. Even a million :)\n")

yay = "Correct answer! You're doing well. You got 10 more points!"
nah = "Nope, totally incorrect! Try to do your best."
sense = "You should be careful about case sensitivity next time!"
points = 0

def contin():
    conti = input("Do you want to continue? (y/n) ")
    while conti != "y" and conti != "n":
        print("Please choose y or n\n")
        conti = input("Do you want to continue? (y/n) ")
    if conti == "y":
        print("\nAlright! Next question then...")
    elif conti == "n":
        print("Huh! What a journey. Thanks for joining...")
        return False
        
def scorecheck():
    if points <= 50:
        print("Your score is " + str(points) + ". Sad but you couldn't make it. Maybe next time :)")
    elif points > 50 and points < 100:
        print("Your score is " + str(points) + ". What a good score!")
    elif points >= 100:
        print("Your score is " + str(points) + ". You're amazing! This is the highest score!!!")

def fin():
    scorecheck()
    exit()

qas = {'Q1 - What is the name of the instructor of the course "Introduction to Python" in Global AI Hub?\n--> ':'Ömer Cengiz',
'Q2 - Who is the first that mentions about Turing Test?\n--> ':'Alan Turing',
'Q3 - What is the name of the humanoid robot that Honda company designed in 2000?\n--> ':'ASIMO',
'Q4 - What is the name of the hub where you can get free education about AI and offers a very useful environment?\n--> ':'Global AI Hub',
'Q5 - What is the name of a teaching model created by combining four important disciplines?\n--> ':'STEM',
'Q6 - Which programming language is created by Bjarne Stroustrup?\n--> ':'C++',
'Q7 - What is the name of the software engineer who leads NASA Apollo program?\n--> ':'Margaret Hamilton',
'Q8 - What is the name of the artificial intelligence supported virtual assistant developed by Amazon?\n--> ':'Alexa',
'Q9 - What is the name of the company that released the gpt-3 in the past months, which was also supported by Elon Musk?\n--> ':'OpenAI',
'Q10 - What is the name of the artificial intelligence system developed by IBM, which defeated Garry Kasparov in chess?\n--> ':'Deep Blue'}

m = 0
for k, v in qas.items():
    m += 1
    answer = input(k)
    if answer == v:
        print(yay)
        points += 10
        if m == len(qas):
            fin()
        print("Your current point is:", points)
        while contin() == False:
            fin()
    elif answer.casefold() == v.casefold():
        print(sense)
        if m == len(qas):
            fin()
        while contin() == False:
            fin()
    else:
        print(nah)
        if m == len(qas):
            fin()
        while contin() == False:
            fin()
