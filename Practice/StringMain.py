#name = input ("Enter your full name: ")
#result = len(name) # - counts number of letters.
#result = name.find("s") # finds "s" in what order of a name entered
#result = name.rfind("q")
#name = name.capitalize() #first letter capitalized

#name = name.upper() #capitalized all letters.
#name = name.lower() #lower letters from capitalized

#result = name.isdigit() #returns false if input contains letters - true if numbers
#result = name.isalpha() #returns true only if all input is letters, space returns false

#phone_number = input("Enter Phone number: ")

#result = phone_number.count("-") #count dashes
#result = phone_number.replace("-", " ") #replace dashes with space

username = input("Enter a username: ")


if len(username) > 12:
    print("Your Username Can NOT Be More Than 12 Characters...")
elif not username.find(" ") == -1:
    print("Your Username Can't Contain Spaces")
elif not username.isalpha():
    print("Your Username Can't Contain Numbers")
else:
    print(f"Welcome {username}")
#print (result)