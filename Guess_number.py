from random import randint

def computer_number(min_num,max_num):
    return randint(min_num,max_num)

def ciao():
    print ("Grazie per aver giocato, alla prossima!")
    quit()
    
def tipo_e_range():
    insert_request = (input("Numero: "))
    if insert_request == "exit":
        ciao()
    while insert_request.isdigit() == False:
        insert_request = (input('Non sembra essere un numero. Riprova: '))
    insert_request_int = int(insert_request)
    if insert_request_int < 0 or insert_request_int > 10:
        print("Stai sforando, bello. Riprova:")
        tipo_e_range()
    return(insert_request_int)

win_counter = 0
def count():
    global win_counter
    win_counter += 1

err_counter = 0
def error_count():
    global err_counter
    err_counter += 1
    point_counter()

total_points = 0
def show_total_points():
    global total_points
    total_points += points

points = 100
def point_counter():
    global points
    if points == 0:
        exit
    points -= 10
    
def post_win():
    replay = input(f"Vittoria numero {win_counter}! :D\nVuoi continuare?\n(Y/n):")
    if replay == "exit":
        ciao()
    while replay != "Y" and replay != "n":
        replay = input("Non ho capito, scusa.\nRigiochi?\n(Y/n):")
        if replay == "exit":
            ciao()
    if replay == "Y":
        error_count = 0
        init()
    elif replay == "n":
        ciao()


def play(numero_ai):
    
    ai_pick = numero_ai
    numero_user = (tipo_e_range())
    while numero_user != ai_pick:
        if numero_user > ai_pick:
            print("Hai sparato troppo in alto, campione. Riprova!")
            error_count()
            play(ai_pick)
        if numero_user < ai_pick:
            print("Troppo basso, purtroppo. Riprova!")
            error_count()
            play(ai_pick)
            
    print (f"Hai azzeccato! Il numero era proprio {numero_user}! Hai commesso {err_counter} errori e guadagnato {points} punti!\n")
    show_total_points()
    print (f"Totale punti {total_points}")
    count()
    post_win()

def init():
    low = 0
    high = 10
    numero_pc = (computer_number(low,high))
    print(f'\nSfida la sorte indovinando il numero fortunello! \nScegline uno da {low} a {high}.\nPremere "exit" in qualsiasi momento per uscire.\n')
    play(numero_pc)

init()