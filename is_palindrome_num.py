#Return true if integer n equals its mathematically computed reverse

def is_palindrome_num(num):
    rev=0
    temp=num
    while(num>0):
        rev=rev*10+(num%10)
        num=num//10
    print(rev)

    if temp==rev:
        print("num is palindrome")
    else:
        print("num is not palindrome")

is_palindrome_num(121)