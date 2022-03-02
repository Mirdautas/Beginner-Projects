from random import randint

def ciao():
    print("\n\t\t\t\t\u001b[45;1mSee ya, adventurer!\u001b[0m\n\n")
    quit()
    
def replay():
    player_choice = input("\nPress ENTER to roll again with the same parameters, R to (R)estart or 'exit' to quit: ")
    while player_choice != "R" and player_choice != "exit" and player_choice != "":
        player_choice = input("\n\u001b[41;1mERROR\u001b[0m: Wrong imput.\nPress Enter to roll again with the same parameters, R to (R)estart or 'exit' to quit: ")
    if player_choice == "R":
        print("\n")
        play()
    elif player_choice == "exit":
        ciao()
    elif player_choice == "":
        print("\n")
        return(0)

dice_list = ["\u001b[35mTetrahedron(4)\u001b[0m","\u001b[36mCube(6)\u001b[0m", "\u001b[32mOctahedron(8)\u001b[0m","\u001b[33mPentagonal(10)\u001b[0m","\u001b[34mDodecahedron(12)\u001b[0m","\u001b[31mIcosahedron(20)\u001b[0m", "\u001b[31;1mD%(100)\u001b[0m"]

def display_dices():
    for index, types in enumerate(dice_list):
        print(f"{index} = {types}")

def valid_dice():
    display_dices()
    dice = input("\nSelect a Dice type: ")
    while dice.isdigit() == False:
        if dice == "exit":
            ciao()
        print("\n\u001b[41;1mERROR\u001b[0m: Invalid dice format.\n")
        display_dices()
        dice = input("\nSelect a Dice type: ") 
    dice_int = int(dice) 
    return(dice_int)

def conversion(dadoscelto):
    if dadoscelto == 0:
        dadoscelto = 4
    elif dadoscelto == 1:
        dadoscelto = 6
    elif dadoscelto == 2:
        dadoscelto = 8
    elif dadoscelto == 3:
        dadoscelto = 10
    elif dadoscelto == 4:
        dadoscelto = 12
    elif dadoscelto == 5:
        dadoscelto = 20
    elif dadoscelto == 6:
        dadoscelto = 100
    return(dadoscelto)

def roll(min_num, max_num):
    dice_roll = randint(min_num,max_num)
    return (dice_roll)

def multiple_dices(): 
    dice_numbers = input("How many dices you want to roll?\nInsert: ")
    while dice_numbers.isdigit() == False:
        if dice_numbers == "exit":
            ciao()
        dice_numbers = input("\n\u001b[41;1mERROR\u001b[0m: Not a number.\nHow many dices you want to roll?\nInsert: ")
    dice_numbers_int = int(dice_numbers)
    return (dice_numbers_int)

def play():
    
    dado = valid_dice()
    while dado > 6:
        print("\n\u001b[41;1mERROR\u001b[0m: Not a dice on the list.\n")
        dado = valid_dice()
    print(f"\n{dice_list[dado]} selected.\n")
    how_many = multiple_dices()
    while how_many == 0:
        print("\nCan't roll zero dices. Pick again.\n")
        how_many = multiple_dices()    
    print(f"\nAight, {how_many} X {dice_list[dado]} selected.\nLet's roll.\n...\n.....")
    faces = conversion(dado)
    multiroll(how_many, faces)
    while replay() == 0:
        print(f"\n{how_many} X {dice_list[dado]} selected.\nLet's roll.\n...\n.....")
        multiroll(how_many, faces)

def multiroll(rollate, facce):
    roll_order =1
    for i in range(rollate, 0, -1):
        print(f"{roll_order}.......>",roll(0, facce))
        roll_order += 1
  
def init():
    print("\n\n\t\t\u001b[45;1mWelcome to Dice Paradise! Pick a Dice and start rolling!\u001b[0m\n")
    play()

init()