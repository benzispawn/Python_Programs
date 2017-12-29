import os, random, string

def pass_gen():
    print("Welcome to the Benzi's password generator!!")
    print("How strong you want your password?")
    length = input("Choose a length, 4 to 12: ")

    def pass_number():
       password = ""
       for i in range(int(length)):
           n = str(random.randint(0,9))
           password = password + n
       print(password)

    def pass_low():
        password = ""
        for i in range(int(length)):
            s = string.ascii_lowercase + string.digits
            m = password.join(random.choice(s))
            password = password + m
        print(password)

    def pass_upper():
        password = ""
        for i in range(int(length)):
          x = string.ascii_uppercase + string.ascii_lowercase + string.digits
          y = password.join(random.choice(x))
          password = password + y
        print(password)

    def pass_symbol():
        password = ""
        for i in range(int(length)):
            char = ['!','@','#','$','%','&','*','(',')','[',']','{','}','?',':'\
,';']
            z = string.ascii_uppercase + string.ascii_lowercase + string.digits\
 + random.choice(char)
            c = password.join(random.choice(z))
            password = password + c
        print(password)

    def pass_loop():
        number = input("Do you want only numbers on your password?(yes or no) ")
        if (number == "yes" or number == "y"):
            pass_number()
        else:
            upper = input("Do you wanna mix lowercases with uppercases? With not \
it will only have lowercases with numbers.(yes or no) ")
            if (upper == "no" or upper == "n"):
                pass_low()
            else:
                symbol = input("Do you wanna symbols, like # or * ?(yes or no)")
                if (symbol == "no" or symbol == "n"):
                    pass_upper()
                else:
                    pass_symbol()
    pass_loop()

pass_gen()
