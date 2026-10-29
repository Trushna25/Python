# Extract digits using modulo and tally those that satisfy digit % 2 == 0

def count_even_digits(n):
    count=0
    # while(n>0):
    #     last_digit=n%10
    #     if last_digit%2==0:
    #         count+=1
    # print(count)


    for i in n:
        if int(i) % 2 == 0:
            count+=1
    return count

number=int(input("Enter a number:\n"))
print(count_even_digits(1234))