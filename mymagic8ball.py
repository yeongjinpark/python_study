#my magic ball
import random
#put answers in a tuple
answers=("go for it!",
         "no way, jose",
         "i'm not sure,ask me again",
         "fear od the unknown is whar imprisons us,",
         "it would be medness to do that","only you can save mankind",
         "makes no difference to me,
         "do or don't-whatever.",
         "yes, l think on balance that is the right choice"
         )

print("welcome to mymagicball")

#get the users question
question=input("ask me for advice then press ENTER to shake me.\n")
print("shaking,,,\n" *4)

#use the randint() fuction to select the correct answer
choice=random.randint(0,7)

print(answers[choice])

input("\n\npress the return key to finish")
