from time import sleep

def check_15(checknum):
    return(checknum % 15 == 0)

def check_3(checknum):
    return(checknum % 3 == 0)

def check_5(checknum):
    return(checknum % 5 == 0)

while True:
    num = int(input('Please input your number (type 0000 to end the game):    '))
    counter = 1       # counter starts from 1

    if num == 0000:    # if the user types 0000, process stops
        break

    while num >= counter:   # while the user input number is greater than or equal to count_num,
                              # the while loop will run

        if check_15(counter):
                print('Fizzbuzz')
                sleep(0.1)

        elif check_3(counter):
                print('Fizz')
                sleep(0.1)

        elif check_5(counter):
                print('Buzz')
                sleep(0.1)

        else:
                print(counter)
                sleep(0.1)
        counter += 1
