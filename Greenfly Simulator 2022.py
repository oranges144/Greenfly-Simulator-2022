#Variables
juveniles = '0'
adults = '0'
seniles = '0'
birth_rate = '0'
survival_rate = '0'
menu_choice = '0'

#Functions and lists
def leave():
    input("\nPress enter to exit. ")
    quit()

def check_juv(juveniles):
    score = 0
    digits = ['1','2','3','4','5','6','7','8','9','0']
    for letter in juveniles:
        if letter in digits:
            score += 1
    if score == len(juveniles):
        return True
    else:
        return False

def check_adu(adults):
    score = 0
    digits = ['1','2','3','4','5','6','7','8','9','0']
    for letter in adults:
        if letter in digits:
            score += 1
    if score == len(adults):
        return True
    else:
        return False

def check_sen(seniles):
    score = 0
    digits = ['1','2','3','4','5','6','7','8','9','0']
    for letter in seniles:
        if letter in digits:
            score += 1
    if score == len(seniles):
        return True
    else:
        return False

def check_birth(birth_rate):
    if birth_rate >= 1 and birth_rate <= 2:
        return True
    else:
        return False

def check_surv(survival_rate):
    if survival_rate > 0 and survival_rate <= 1:
        return True
    else:
        return False

#Menu
while menu_choice == '0':
    
    print('''\n   _____                      __ _          _____ _                 _       _               ___   ___ ___  ___  
  / ____|                    / _| |        / ____(_)               | |     | |             |__ \ / _ \__ \|__ \ 
 | |  __ _ __ ___  ___ _ __ | |_| |_   _  | (___  _ _ __ ___  _   _| | __ _| |_ ___  _ __     ) | | | | ) |  ) |
 | | |_ | '__/ _ \/ _ \ '_ \|  _| | | | |  \___ \| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|   / /| | | |/ /  / / 
 | |__| | | |  __/  __/ | | | | | | |_| |  ____) | | | | | | | |_| | | (_| | || (_) | |     / /_| |_| / /_ / /_ 
  \_____|_|  \___|\___|_| |_|_| |_|\__, | |_____/|_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|    |____|\___/____|____|
                                    __/ |                                                                       
                                   |___/                                               \n                         
Please pick from one of the following options:

    1. Run Model
    2. Choose Generations to Run
    3. Set Generation 0 Values
    4. Show Generation 0 Values
    5. Exit\n''')

#User inputs menu choice
    menu_choice = input("Enter your choice: ")

#Menu choice 1 - run model
    if menu_choice == '1':
        print("\nIn generation 0, there will be", juveniles, "juveniles,", adults, "adults, and", seniles, "seniles. There will be a starting total of", juveniles + adults + seniles, "greenflies.")
        print("\nThe model will run for", gen_num, "generations.")
        
        while int(gen_num) > 0:
            old_juv = juveniles
            old_adu = adults
            old_sen = seniles 

            seniles = (float(old_sen) * float(survival_rate)) + float(old_adu)
            juveniles = float(old_adu) * float(birth_rate)
            adults = float(old_juv)
            
            print("\nThere are now", round(juveniles), "juveniles,", round(adults), "adults, and", round(seniles), "seniles.\nThat makes a total of", round(juveniles) + round(adults) + round(seniles), "greenflies.")
            
            gen_num = int(gen_num) - 1

            print(gen_num, "generations remain.")

            input("Press enter to proceed. ")
            
        print("\nThe model has finished running.")
        print("The final totals of all ages are", round(juveniles), "juveniles,", round(adults), "adults, and", round(seniles), "seniles.")
        print("This makes the final population total", round(juveniles) + round(adults) + round(seniles), "greenflies.")

        input("\nPress enter to return to the menu. ")

        juveniles = 0
        adults = 0
        seniles = 0
        old_juv = 0
        old_adu = 0
        old_sen = 0
        birth_rate = 0
        survival_rate = 0
        menu_choice = '0'

#Menu choice 2 - pick num of gens
    elif menu_choice == '2':
        gen_num = '0'
        gen_num = input("How many generations would you like to run the model for? ")
        print("\nThe model will run for", gen_num, "generations.\n")
        input("Press enter to go back to the menu.")
        menu_choice = '0'

#Menu choice 3 - set gen 0 values
    elif menu_choice == '3':
        juveniles = input("\nHow many juveniles should there be in generation 0? ")
        check_juv(juveniles)
        while check_juv(juveniles) == False:
            juveniles = input("That isn't a number...\nHow many juveniles should there be in generation 0? ")
            check_juv(juveniles)
        
        adults = input("How many adults should there be in generation 0? ")
        check_adu(adults)
        while check_adu(adults) == False:
            adults = input("That isn't a number...\nHow many adults should there be in generation 0? ")
            check_adu(adults)
            
        seniles = input("How many seniles should there be in generation 0? ")
        check_sen(seniles)
        while check_sen(seniles) == False:
            seniles = input("That isn't a number...\nHow many seniles should there be in generation 0? ")
            check_sen(seniles)

        print("\nThere will be", juveniles, "juveniles,", adults, "adults, and", seniles, "seniles.\n")

        birth_rate = float(input("Please input a birth rate between 1 and 2: "))
        check_birth(birth_rate)
        while check_birth(birth_rate) == False:
            birth_rate = float(input("That isn't a number in the range...\nPlease input a birth rate between 1 and 2: "))
            check_birth(birth_rate)
        
        survival_rate = float(input("Please input a survival rate between 0 and 1: "))
        check_surv(survival_rate)
        while check_surv(survival_rate) == False:
            survival_rate = float(input("That isn't a number in the range...\nPlease input a survival rate between 0 and 1: "))
            check_surv(survival_rate)
        
        print("\nYou selected", birth_rate, "birth rate, and", survival_rate, "survival rate.")

        int(juveniles)
        int(adults)
        int(seniles)

        input("\nPress enter to return to the menu.")
        menu_choice = '0'

#Menu choice 4 - show gen 0 values
    elif menu_choice == '4':
        print("\nIn generation 0, there will be:\n\n", juveniles, "juveniles\n", adults, "adults\n", seniles, "seniles\n A birth rate of", birth_rate, "\n A survival rate of", survival_rate)
        input("\nPress enter to return to the menu. ")
        menu_choice = '0'

#Menu choice 5 - quit
    elif menu_choice == '5':
        leave()

#Menu choice - invalid input
    else:
        print("That isn't an option, try again.")
        input("Press enter to go back to the menu. ")
        menu_choice = '0'
