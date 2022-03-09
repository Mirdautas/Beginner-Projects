import time
def name_story():
    p_m_nome_comune1 = input("\n1/13 Nome comune (plurale, maschile): ")
    m_nome_comune1 = input("\n2/13 Stesso nome comune di prima, ma singolare: ")
    numero1 = input("\n3/13 Numero maggiore di 1: ")
    numero2 = input("\n4/13 Numero maggiore di 1: ")
    numero3 = input("\n5/13 Numero maggiore di 1: ")
    p_nome_comune1 = input("\n6/13 Nome comune (plurale): ")
    p_m_aggettivo1 = input("\n7/13 Aggettivo (maschile, plurale): ") 
    m_job1 = input("\n8/13 Mestiere (maschile, plurale): ") 
    nome_comune2 = input("\n9/13 Nome comune (plurale): ") 
    f_nome_comune1 = input("\n10/13 Nome comune (femminile): ")
    nome_proprio = input("\n11/13 Nome proprio: ")
    location = input("\n12/13 Piccolo comune italiano: ")
    magia = input("\n13/13 Magia: ")
    
    print("\nElaborazione...")
    time.sleep(0.5)
    print("\n.")
    time.sleep(0.2)
    print("\n..")
    time.sleep(0.2)
    print("\n...")
    time.sleep(1)
    
    print(f'''\nTutto ebbe inizio con la forgiatura dei grandi {p_m_nome_comune1}. 
{numero1} furono dati agli elfi, gli esseri {p_m_aggettivo1} più saggi e {p_m_aggettivo1} di tutti. 
{numero2} ai re dei nani, grandi {m_job1} e costruttori di {nome_comune2} nelle montagne. 
E {numero3}, {numero3} {p_m_nome_comune1} furono dati alla razza degli uomini
che più di qualunque cosa desiderano il potere. 
Perché in questi anelli erano sigillati la forza e la volontà di governare tutte le razze.
Ma tutti loro furono ingannati, perché venne creato un altro {m_nome_comune1}. 
Nella terra di {location}, tra le fiamme del Monte {magia}, {nome_proprio},
l'Oscuro Signore, forgiò in segreto un {m_nome_comune1} sovrano,
per controllare tutti gli altri e in questo {m_nome_comune1} riversò la sua crudeltà,
la sua malvagità e la sua volontà di dominare
ogni forma di {f_nome_comune1}: un {m_nome_comune1} per domarli tutti.\n''')
if __name__ == '__main__':
    name_story()
