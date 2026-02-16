import random

def addition_of_two_numbers(num1, num2, answer):
    correct_answer = num1 + num2

    if answer == correct_answer:
        print("Great Job! That is the correct answer!")
    else:
        print(f"That is incorrect. The correct answer is: {correct_answer}")

num1 = random.randint(1,50)
num2 = random.randint(1,50)

print(f"  {num1}")
print(f"+ {num2}")
print("------")

answer = float(input("Please enter in your answer: "))

while True:
    addition_of_two_numbers(num1, num2, answer)
