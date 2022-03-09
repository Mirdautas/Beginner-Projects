import time
import random
def name_story():

    Time = random.choice(["C'era un volta", "Molti anni or sono c'era", "In un antico Regno viveva", "In una Era ormai persa nel tempo, viveva", "Durante il tempo della magia runica e dei Draghi di Smeraldo, viveva","Nelle lande oltre i Monti del Sogno bruno, vi era"])
    Main_char = random.choice(["un Re", "un parroco di campagna", "un monaco","un cavaliere","Ludovico il Bardo, un uomo","un Barone", "un contadino"])
    Quality1 = random.choice(["altruista","irascibile", "gioviale", "buono", "gentile", "orgoglioso","severo","sempre sorridente", "stravagante"])
    Quality2 = random.choice(["e taciturno.", "e loquace.", "e amante degli scherzi.", "e imbattibile in battaglia.","e stratega senza eguali.","e molto saggio.","e riflessivo.", "e dal difficile temperamento."])
    #"\n"
    Time_event = random.choice(["Un giorno decise","Una mattina decise","Una sera decise", "La prima Domenica di Fiordimaio decise","Appena terminata la guerra, decise","Avendo svolto tutte le faccende incombenti, decise"])
    Activity = random.choice(["di fare una passeggiata", "di partire per un viaggio", "di incamminarsi col suo cane", "di cercare un luogo per un picnic rilassante", "di andare all'osservatorio delle nuvole e stelle", "di andare a riflettere"])
    Activity_place = random.choice(["presso il Monte Susina.","al lago Burbussa.","verso il villaggio Coppolini.", "nella Foresta odorosa dei muschi.", "sui verdi prati dietro casa."])
    #"\nMentre andava, si accorse di "
    Secondary_char = random.choice(["un signore", "un bizzarro personaggio,", "un figuro", "un'ombra di aspetto", "un giovane"])
    Sec_char_aspect = random.choice(["stanco e sudato,", "pallido e curvo,", "proporzionato e muscoloso,","alto ed emaciato,","tarchiato e muscoloso,","alto e molto in carne,","bassino e dalla pancia prominente," ])
    Sec_char_age = random.choice(["intorno alla cinquantina,","di 30 anni o poco più,", "visibilmente avanti con l'età,","apparentemente molto giovane di età,"])
    Sec_char_activity = random.choice(["intento a spaccare la legna.","davanti ad un fuocherello.", "che si dondolava comodamente su un'amaca.","intento a caricare la sua pipa all'ombra di un frassino.", "che coglieva bacche dagli arbusti vicini.", "tutto impegnato a tirar di spada contro nemici immaginari.", "che fischiettava allegramente.", "che chiedeve le elemosina."])
    #" e in lui subito riconobbe "
    Sec_char_past = random.choice(["il suo amico di infanzia perduto!", "il suo storico arcinemico!","il suo storico rivale in amore!", "il compagno di mille disaventure passate!","l'antipatico compagno di classe che sempre lo prendeva in giro!"])
    #".\n" 
    Think_past = random.choice(["Con velata nostalgia,","Commosso,", "Preso dalla sorpresa,", "Dentro di sè,", "Senza nascondere le sue emozioni,", "Sorpreso ed emozionato,", "Incapace di trattenere una lacrima,"])
    #"ripensò, nonostante tutto,"
    Tought = random.choice(["a quanto fosse bella la giovinezza", "a come il passato fosse lontano", "a quanto le cose che accadono da giovani sembrano piccole e irrilevanti oggi", "agli anni passati dal loro ultimo incontro"])
    #"e decise dunque "
    Invitation = random.choice(["di abbracciarlo e invitarlo da lui a cena.", "di regalargli il suo mantello preferito in segno di pace e amicizia.", "di chiedegli di tornare a casa con lui, per presentargli la sua famiglia.", "di sorridergli e salutarlo come un fratello perduto.", "di fermarsi a fare merenda con lui, dividendo panini e frutta.", "di trattenersi per ore con lui a raccontarsi aneddoti simpatici.", "di restare con lui, in silenzio, a guardare il cielo per un po'."])
    
    print("\nElaborazione...")
    time.sleep(0.5)
    print("\n.")
    time.sleep(0.2)
    print("\n..")
    time.sleep(0.2)
    print("\n...")
    time.sleep(1)
    
    print("\n",Time,Main_char,Quality1,Quality2,"\n",Time_event,Activity,Activity_place,"\n","Mentre andava, si accorse di",Secondary_char,Sec_char_aspect,"\n",Sec_char_age,Sec_char_activity,"\n","In lui, senza che fosse passato un solo istante, riconobbe",Sec_char_past,"\n",Think_past,"ripensò, nonostante tutto,",Tought,"\n","e decise dunque",Invitation,"\n")
if __name__ == '__main__':
    name_story()
