import sys
print("""Stop! Who would cross the Bridge of Death 
Must answer me these questions three, 'ere the other side he see.""")

name = input("What is your Name? ")                 #Asking user for input.

if name.lower() == "arthur":                        
    print("My liege! You may pass!")                #if entered name is arthur, they can cross the bridge.
    sys.exit()                                      #system terminate from here.

quest = input("What is your quest? ")               #Asking user for input.
if not 'grail' in quest.lower():                    #those who dont seek grail cannot cross the bridge.
    print("Only those who seek the Grail may pass!")#if he entered input as a grail, displayed this message.
    
color = input("What is your Favourite color? ")     #Asking user for input.
if name[0]==color[0]:                               #name's first leltter should match the color's first letter.
    print("You may pass!")                          #if name 1st letter is same as color's 1st letter he can cross the bridge.
else:
    print("Incorrect! You must now face the Gorge of Eternal Peril.")     #otherwise this part will execute.       