def check_guess(g, s):
    '''this function receives two parameters: guess, secret'''
    if g == s:
        print("correct")
    elif g > s:
        print("too high")
    else:
        print("too low")



def is_teen(num):
    if num > 12 and num < 20:
        print("that number is in the teens")
    else:
        print("that number is not in the teens")

# the runnable code begins here
secret = 42
guess = int(input("Guess the number: "))
check_guess(guess, secret)

# TODO
# prompt for another guess, call the function


# calling the 'is_teen' function
print("\n------")
num = 15
is_teen(num)
is_teen(10)
