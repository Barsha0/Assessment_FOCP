
#imported mean from statistic module.
from statistics import mean

print("Swallow speed version : 1.0\n")

my_list = []                                           #creating a empty list to store the information given by the user.
reading = input("Enter the next reading: ")            #Asking user for input.
a=reading.lower()                                      #changing the asked input into lower so that lower as well as upeer case can be calculated. 
my_list.append(a)                                      #using append method to add the information to my_list. 
if not a:                                              #checks if list is empty.
    print("NO reading entered. Nothing to read.")       
    exit()                                             #if the above condition is true then it exit from the entire program.
if a:                                                  #using if condition to check weather user have given somthing or not.
    while True:                                        #using while loop and it run until it is false.
        print("Reading saved!")                         
        reading = input("Enter the next reading: ")     
        b=reading.lower()
        my_list.append(b)                               
        if not b:                                      #if we do not enter anything after user ask to. 
            break

print("\n Reading Summery!\n")

length = len(my_list)-1                                 #using the len function to count the length of the my_list.
print(length,"Study Analysed!")       

forEup = []                                             #Creating a list to store the value  after E is removed.    
forBrt = []                                             #Creating a list to store the value  after U is removed.
forMPH = []                                             #Creating a list to add the both typecasted value of U and E.

#
for i in my_list:                   
    if i[0:1].startswith("e"):                          #Use startwith method to check weather it start from e or anything else.
        my_E = i.lstrip("e")                            #Use lstrip method to remove the e.
        forEup.append(my_E)                             #using append method to store in forEup list.
# print(forEup)

  

for k in my_list:
    if k[0:1].startswith("u"):                          #Use startwith method to check weather it start from u or anything else.
        my_U = k.lstrip("u")                            #Use lstrip method to remove the u.
        forBrt.append(my_U)                             #using append method to store in forBrt list.
# print(forBrt)

for j in forEup:                                        #iterating over the forEup list.
    convert = float(j)                                  #typcasting j into float.
    forMPH.append(convert)                              #using append method to add the typecasted value.

for l in forBrt:                                        #iterating over the forBrt list
    convert_1 = float(l)/1.61                           #typecasting l into float.
    forMPH.append(convert_1)                            #using append method to add the typecasted value.
# print(forMPH)  

if forMPH != []:
    my_max = max(forMPH)                                #using the max function to get maximum value.
    my_min = min(forMPH)                                #using the min function to get minimum value.
    my_avg = mean(forMPH)                               #using imported mean function to get the average value.

    print(f"Max speed:     {my_max:.2f}MPH, {my_max*1.161:.2f}KPH")     #using f string and used precision to get upto only 2 values after decimal.
    print(f"Min speed:     {my_min:.2f}MPH, {my_min*1.161:.2f}KPH")     #using f string and used precision to get upto only 2 values after decimal.
    print(f"Average speed: {my_avg:.2f}MPH, {my_avg*1.161:.2f}KPH")     #using f string and used precision to get upto only 2 values after decimal.