#importing string and random module
import string
import random

#creating lists os ascii letters,digits,punctuations,hastag and whitespace
ascii_letter=string.ascii_letters
digits=string.digits
punctuation=string.punctuation
whitespace=string.whitespace

#using hashtag and defined character to use in pasword
characters='#'+string.ascii_letters+string.digits+string.whitespace+string.punctuation

#ganerating password using random choice
def generate_password(length):
    password=''.join(random.choice(characters)for i in range(length))
    return password

def main():
    try:
        length=int(input("Enter Length of the password:"))
        if length<=7:
            print("Password Length should be greather than 8!!! \n PLEASE RETRY \n THANKYOU!")
            return
        else:
            password=generate_password(length)
            print("YOUR PASSWORD IS GENERATED SUCCESSFULLY. \n",password,"\n THANKYOU")
    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")


if __name__ =="__main__":
    main()
