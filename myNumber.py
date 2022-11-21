import random
computer_number=random.randint(1,100)

def is_same(target,number):
    if target==number:
        result="win"
    elif target > number:
        result="low"
    else:
        result="high"
    return result

print("Hi\n I chose a number between 1 and 100")

guess = int(input("뭔지 쓰고 엔터키를 누르세요."))

higer_or_lower=is_same(computer_number,guess)

while higer_or_lower != "win":
    if higer_or_lower == "low":
        guess=int(input("Higher than that. Think again"))
    else:
        guess=int(input("Lower than that.Think again"))

    higer_or_lower=is_same(computer_number,guess)

input("Correct!\nGood Job.\n\n\nPress enter to finish")
