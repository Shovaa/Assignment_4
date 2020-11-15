
"""Conversion farhrenheit into celsius
    temperature_in_farhrenheit :Which is taken input to measure
    celsius: return answer/result"""
def convert (temperature_in_farhrenheit):
       celsius = (temperature_in_farhrenheit - 32) * 5 / 9
       print ("The given temperature:",celsius)

temperature_in_farhrenheit = float(input("Enter temperature in fahrenheit:"))  
convert(temperature_in_farhrenheit)




#inserting pop and printing list using  function
"""insertion and pop of the element to the list and from the list
     insert function:insert eleemnt in particulat position
     pop function : eliminates elemnet from  the list"""
def insert():
    list.insert(5,"Denmark")
    print(list)

def pop():
    print(list.pop(2))   


list=["Germany", "Nepal","America","Japan","Spain"] 
print(list)
insert()
pop()   




#for printing out specific element of list and for finding the length of the list"
"""listview:function use to view specific element"""
def listview():
    print (list[4], list[0])
    print(len(list))
list= ["Hello", "Shova", "Kuikel", "How you doing !","What's new?"]
listview()




# for converting given time in second and converting that into minutes and seconds.
"""time_conversion: function converts given input in seconds into minutes and sec"""
def time_conversion(time_insec):

    minutes = time_insec // 60
    sec = time_insec % (24 * 3600)
    time_insec %= 60
    seconds = time_insec

    print("minutes:%d" % (minutes))
    print("seconds:%d" % (seconds))

time_insec = float(input("Input time in seconds: "))
time_conversion(time_insec)