#the sotal sum of the list element
"""total: function sum up the total of the element in the list"""
def total(listt,sum):
    for num in range(0, len(list)): 
        sum = sum + listt[num] 
    print("Sum of all elements in given list: ", sum)    

listt=[6,9,7,5,4]
sum=0 
total(listt,sum)

#removing duplicate elements from the list.
"""remove : function removes duplicate element from the list 
   removedset : conversion into set directly removes duplicate as set are unique
   removedlist:conversion set into list"""
def remove():
            removedset = set(list1)
            removedlist = list(removedset)
            print("The duplicate free list :",removedlist)

list1 =[1,1,3,5,7,9,9]
remove()


def remove1():
        removedset1=set(list2)
        removedlist1=list(removedset1)
        print("The duplicate free list:", removedlist1)

list2=[2, 1, 6 ,9, 2, 1, 3, 5]    
remove1()  
 


 




""" Counting the length of the string
     string:takes inout from the user
     stringg:function convert and count the length"""
# printing the length of the string         
def stringg(string,string_count):
       for words in string:
                string_count = string_count + 1
       print ("The count of the string is:", string_count)

string=input("Enter string:")
string_count=0
print(string) 

stringg(string,string_count)  
 