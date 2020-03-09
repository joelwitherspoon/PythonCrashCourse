dreamvacations = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    dreamvacation = input("If you could visit one place in the world, where would you go? ")
    
    dreamvacations[name] = dreamvacation
    
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
        
print("\n---Poll Results---")
for name, dreamvacation in dreamvacations.items():
    print(name + " would like to go to " +dreamvacation+".")
    
    