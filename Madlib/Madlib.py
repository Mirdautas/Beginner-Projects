from sources import harry_potter,star_wars,lotr,storiandom
import random 
#name_story deve essere la funzione che runna tutto
def componi():
    library = [harry_potter, star_wars, lotr]
    pc_choice = random.choice(library)
    pc_choice.name_story()

def storia_random():
    storiandom.name_story()
    
def uscita():
    print("\nGrazie per aver giocato, ciao!\n")
    quit()

info = '''\n\u001b[42mINFO\u001b[0m:\n\u001b[35;1mStoriandom\u001b[0m è un generatore casuale di storie che lascia decidere al PC come assemblare il racconto!
\u001b[34;1mComponi\u001b[0m ti permette di inserire parole chiave e personalizzare la tua storia!
Digitare \u001b[33;1mexit\u001b[0m nel menù principale per uscire.\n'''

def replay():
    replay = input("Vuoi giocare ancora?\n(Y/n): ") 
    while replay != "Y":
        if replay == "exit" or replay == "n":
            uscita()
        print("\n\u001b[41mERROR\u001b[0m: codice non valido.\n")
        replay = input("Vuoi giocare ancora?\n(Y/n): ")
    if replay == "Y":
        esecuzione()
        
def esecuzione():
    modalità_scelta = input("\n\u001b[35;1m1 - Storiandom\u001b\n\u001b[34;1m2 - Componi\u001b[0m\n\u001b[32;1m3 - INFO\u001b[0m\nScegli numero corrispondente: ")
    while modalità_scelta != "1" and modalità_scelta != "2":
        if modalità_scelta == "3":
            print(info)
            modalità_scelta = input("\n\u001b[35;1m1 - Storiandom\u001b\n\u001b[34;1m2 - Componi\u001b[0m\n\u001b[32;1m3 - INFO\u001b[0m\nScegli numero corrispondente: ")  
        elif modalità_scelta == "exit":
            uscita()
        else:
            print("\n\u001b[41mERROR\u001b[0m: codice non valido.\n")
            modalità_scelta = input("\n\u001b[35;1m1 - Storiandom\u001b\n\u001b[34;1m2 - Componi\u001b[0m\n\u001b[32;1m3 - INFO\u001b[0m\nScegli numero corrispondente: ")
    if modalità_scelta == "1":
        print("\n\u001b[35;1mStoriandom\u001b[0m selezionata:")
        storia_random()   
    if modalità_scelta == "2":
        print("\n\u001b[34;1mComponi\u001b[0m selezionata:")
        componi()   

def init():
    print('''\n\t\t~~~~~~~    Benvenuti nel narrastorie!    ~~~~~~~\n
Istruzioni:
Scegli tra la modalità \u001b[35;1mStoriandom\u001b[0m e \u001b[34;1mComponi\u001b[0m, oppure Info, per avere più informazioni.\n(\u001b[33;1mexit\u001b[0m per uscire)''')
    esecuzione()
    replay()       
init()