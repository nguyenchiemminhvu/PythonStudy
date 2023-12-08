import random

print("Guess a number in range [1, 10]")

times = 3
while (times > 0):
    times -= 1
    target = random.randint(1, 10)
    num = input("Enter a number [1, 10]: ")
    if (target == int(num)):
        print("Correct!!")
        break
    else:
        print("The target is: " + str(target))
else: # In Python, the while loop can optionally have an else part
    print("You lose")