from random import randint

options_list = ["\u001b[31mGerry Marmitta\u001b[0m","\u001b[33mWide Tomino\u001b[0m","\u001b[36mI Satanic R\u001b[0m","\u001b[32mmodello relazionale Giacirtazzi\u001b[0m","\u001b[35mDottor Amoretti\u001b[0m","\u001b[34mDuce nero\u001b[0m","\u001b[37mCaptain Alpaca\u001b[0m"]

def ft_exit():
    print("\nThank you for playing. Bye! :D\n")
    quit()
    
def replay():
    rematch = input("\nDo you want to play another round? (Y/n): ")
    while rematch != "Y" and rematch != "n":
        if rematch == "exit":
            ft_exit()
        rematch = input("\nI didn't understand. Replay? (Y/n): ")
    if rematch == "Y":
        match()
    if rematch == "n":
        ft_exit()

win_counter = 0
def w_count():
    global win_counter
    win_counter += 1 

loss_counter = 0
def l_count():
    global loss_counter
    loss_counter += 1

tie_counter = 0
def t_count():
    global tie_counter
    tie_counter += 1

def show_results(win,loss,tie):
    print("RESULTS")
    print(f"\nVictory Count:................. {win}")
    print(f"Loss Count:.................... {loss}")
    print(f"Tie Count:..................... {tie}")

def computer_choice(content):
    computer_chose = randint(0, len(content)-1)
    return computer_chose

def user_interface(options):
    for index, value in enumerate(options):
        print(f"{index} = {value}")
        
def user_weapon():
    print("\n")
    user_interface(options_list)
    user_input = (input("\nPick your weapon.\nChoose a number: "))
    while user_input.isdigit() == False:
        if user_input == "exit":
            ft_exit()
        user_input = input(f"\n{user_input}?\nNot a weapon. Retry!\nChoose a number: ")
    user_input_int = int(user_input)
    if user_input_int < 0 or user_input_int > len(options_list)-1:
        print(f"\n{user_input_int} does not match any weapon on the list.\n")
        return
    return(user_input_int)

def match():
    ai_pick = computer_choice(options_list)
    user_pick = user_weapon()
    if user_pick == None:
        match()
    
    print(f"\nYour opponent chosed {options_list[ai_pick]} to contrast your {options_list[user_pick]}\n\n...\n\nAnd\n\n...\n")
        
    if user_pick == ai_pick:
        print(f"\nThe battle between your {options_list[user_pick]} and opponent's own {options_list[ai_pick]} is legendary, but they both end up killing each other.\n         TIE!\n")
        t_count()
        show_results(win_counter,loss_counter,tie_counter)
        replay()
   
    if user_pick == 0:
        if ai_pick > 0 and ai_pick < 4:
            print(f"Your {options_list[user_pick]} won over opponent's {options_list[ai_pick]}.\n          VICTORY!\n")
            w_count()
            show_results(win_counter,loss_counter,tie_counter)
        else:
            print(f"Your {options_list[user_pick]} got SMASHED by opponent's {options_list[ai_pick]}.\n          DEFEAT!\n")
            l_count()
        show_results(win_counter,loss_counter,tie_counter)
        replay()
   
    if user_pick == 1:
        if ai_pick > 1 and ai_pick < 5:
            print(f"Your {options_list[user_pick]} won over opponent's {options_list[ai_pick]}.\n          VICTORY!\n")
            w_count()
        else:
            print(f"Your {options_list[user_pick]} got SMASHED by opponent's {options_list[ai_pick]}.\n          DEFEAT!\n")
            l_count()
        show_results(win_counter,loss_counter,tie_counter)
        replay()
    if user_pick == 2:
        if ai_pick > 2 and ai_pick < 6:
            print(f"Your {options_list[user_pick]} won over opponent's {options_list[ai_pick]}.\n          VICTORY!\n")
            w_count()
        else:
            print(f"Your {options_list[user_pick]} got SMASHED by opponent's {options_list[ai_pick]}.\n          DEFEAT!\n")
            l_count()
        show_results(win_counter,loss_counter,tie_counter)
        replay()    
            
    if user_pick == 3:
        if ai_pick > 3 and ai_pick < 7:
            print(f"Your {options_list[user_pick]} won over opponent's {options_list[ai_pick]}.\n          VICTORY!\n")
            w_count()
        else:
            print(f"Your {options_list[user_pick]} got SMASHED by opponent's {options_list[ai_pick]}.\n          DEFEAT!\n")
            l_count()
        show_results(win_counter,loss_counter,tie_counter)
        replay()
        
    if user_pick == 4:
        if ai_pick > 4 and ai_pick < 7 or ai_pick == 0:
            print(f"Your {options_list[user_pick]} won over opponent's {options_list[ai_pick]}.\n          VICTORY!\n")
            w_count()
        else:
            print(f"Your {options_list[user_pick]} got SMASHED by opponent's {options_list[ai_pick]}.\n          DEFEAT!\n")
            l_count()
        show_results(win_counter,loss_counter,tie_counter)
        replay()               
    
    if user_pick == 5:
        if ai_pick == 6 or ai_pick < 2:
            print(f"Your {options_list[user_pick]} won over opponent's {options_list[ai_pick]}.\n          VICTORY!\n")
            w_count()
        else:
            print(f"Your {options_list[user_pick]} got SMASHED by opponent's {options_list[ai_pick]}.\n          DEFEAT!\n")
            l_count()
        show_results(win_counter,loss_counter,tie_counter)
        replay()

    if user_pick == 6:
        if ai_pick < 3:
            print(f"Your {options_list[user_pick]} won over opponent's {options_list[ai_pick]}.\n          VICTORY!\n")
            w_count()
        else:
            print(f"Your {options_list[user_pick]} got SMASHED by opponent's {options_list[ai_pick]}.\n          DEFEAT!\n")
            l_count()
        show_results(win_counter,loss_counter,tie_counter)
        replay()    
    

  
print("\n\n             WELCOME TO THE ARENA\n")
match()
