def main():
    user_Input = int(input('What is your number?'))

    fact = factorial(user_Input)
    print(f"Your number: {user_Input}'s factoral is {fact}!")

def factorial(user_Input):
    if user_Input == 0:
        return 1
    else:
        return user_Input * factorial(user_Input -1)
    

if __name__ == "__main__":
    main()