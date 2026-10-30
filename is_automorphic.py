#Return true if n*2 ends in the same digits as n using modular place values

def square(num):
    square=num**2
    return square

def is_automorphic(num):
    if num%10==square(num)%10:
        print("is automorhic")
    else:
        print("not automorphic")

num=int(input("enter a number:\n"))
is_automorphic(num)