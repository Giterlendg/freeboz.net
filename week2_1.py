# Write program to check if person if of legal drinking age (18 Norway, 21 USA)

# Ask user their name (must have two names)


usa = {"us","the us","usa"}

norway = {"norway","norge","nor"}

legal_usa = 2001
legal_nor = 2004

while True:
    print("Hello Welcome to cheapbooze.net!")
    first_name,last_name = input("May I ask you your first and last name?: ").split()
    nationality = input(f'Nice to have you here {first_name}. From which country are you currently browsing?: ').strip()
    if nationality in norway or usa:
       age = int(input("Thats a glorious country. May we know which year you were born?: "))
    else: print("sorry we only serve customers from the US and Norway atm")

    if nationality == usa and age <= legal_usa or nationality == norway and age <= legal_nor:
        print("Happy shopping!")
    else:
        print ("Sorry you seem to be too young to buy alcohol")
          


#NOTE: Below are just some codes I tried to implement but coudlnt get to work. 

#else: input(''' I didn't get your name properly. Can you please give me your first and last name again?''')

#while True:       
#names = list(input(" Hello, please type your name: ").strip().title()

    
age <= legal_usa 
        
# else:print(input("Sorry I didnt catch that, can you please type your first and last name again?")



# make program return short verdict for the user


          
# if (first_name == True) and (last_name == True):

#Hint: You can use f.ex. len(your_string.split()) to get the length of the string your_string. Can you figure out why?
