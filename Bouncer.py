#ask for age
age = input("How old are you?: ")
if age:
    age = int(age)
#18-21 wristband
    if age >= 18 and age < 21:
        print("You can enter, but need a wristband!")
    #21+ drink, normal entry
    elif age >= 21:
        print("You are good to enter and can drink!")
    #too young, sorry
    else:
            print("You can't come in, you're too young.")
else:
     print("Please enter an age!")
#Faster way:
# if age:    
#   age = int(age)
#   if age >= 21"
#       print("You can enter and drink.")
#   elif age >= 18:
#       print("You can enter but need a wristband")
#   else:
#       print("You can't come in.")
#else:
#   print("Please enter an age.")