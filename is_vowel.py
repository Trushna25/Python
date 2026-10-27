# Return True if character ch matches any vowel in upper or lower case format

def is_vowel(a):
    for i in a:
        if i in "aeiouAEIOU":
            print("vowel is present")
            break
    else:
        print("vowel is not present")

str1 = input("Enter a string:\n") 
is_vowel(str1)