# return true if integer age>=18,otherwise ruturn false

def is_voting_age(age):
    if age>=18:
        print("eligible for voting")
       
    else:
       print("not eligible for voting")

age =int(input("Enter your age:\n"))
is_voting_age(age)