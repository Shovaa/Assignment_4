  
# Program to check if a string is palindrome or not
# check if the string is equal to its reverse
"""palindrome:checking the string same after reversing the each letter
 """
def palindrome(my_string):

        my_string = my_string.casefold()
        rev_string = reversed(my_string)
        if list(my_string) == list(rev_string):
           print("The string is a palindrome.")
        else:
           print("The string is not a palindrome.")

my_string = input("Enter the string:")
palindrome(my_string)

#finding prime numbers between 1 and 100 
#finding prime numbers between 1 and 100 
"""prime number:divisible either by 1 or itself
    """
def prime():
        for num in range(1, 100 + 1):
         if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)          
prime()  



#finding the number of occuerence of string and printing them in dictonary key value pairs.
"""counting the occurence of particulat string and formating into key value pair """
def count_char(text):
  for i in range(len(text)):
    if len(text) == 0:
      break;
    ch = text[0]
    if ch == ' ' or ch == '\t':
      continue
    result= ({ch :  text.count(ch)})
    print (dict(result))
    text = text.replace(ch, '').strip()

count_char('pineapple')