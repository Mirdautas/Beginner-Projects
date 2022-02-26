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
    
def post_win():
    replay = input(f"Vittoria numero {win_counter}! :D\nVuoi continuare?\n(Y/n):")
    if replay == "exit":
        ciao()
    while replay != "Y" and replay != "n":
        replay = input("Non ho capito, scusa.\nRigiochi?\n(Y/n):")
        if replay == "exit":
            ciao()
    if replay == "Y":
        play()
    elif replay == "n":
        ciao()


def play():
    
    low = 0
    high = 10
    
    numero_pc = computer_number(low,high)
    numero_user = (tipo_e_range())

    while numero_user != numero_pc:
        if numero_user > numero_pc:
            print("Hai sparato troppo in alto, campione. Riprova!")
            play()
        if numero_user < numero_pc:
            print("Troppo basso, purtroppo. Riprova!")
            play()
            
    print (f"Hai azzeccato! Il numero era proprio {numero_user}!")
    count()
    post_win()

low = 0
high = 10
print(f'Sfida la sorte indovinando il numero fortunello! \nScegline uno da {low} a {high}.\nPremere "exit" in qualsiasi momento per uscire.\n')
play()