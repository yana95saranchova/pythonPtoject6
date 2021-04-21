import random
n=0   #число попыток угадать
number_to_guess=random.randint(1,10)

while n<10:
    user_number = int(input("Guess the number:  "))
    n+=1
    if user_number<number_to_guess:
        print("Your number should be bigger")
    if user_number>number_to_guess:
        print("your number should be less")
    if user_number==number_to_guess:
        print('you are right, perfect,this number is {0}'.format(number_to_guess))
        break
