import time

def name_story():
    nome_proprio1 = input("\n1/10 Nome proprio: ")
    m_nome_comune1 = input("\n2/10 Nome comune (maschile): ")
    m_aggettivo1 = input("\n3/10 ggettivo (maschile, plurale): ")
    p_m_nome_comune1 = input("\n4/10 Nome comune (plurale, maschile): ")
    nome_proprio2 = input("\n5/10 Nome proprio: ")
    m_aggettivo2 = input("\n6/10 Aggettivo (maschile, singolare): ")
    m_aggettivo3 = input("\n7/10 Aggettivo (maschile, singolare): ")
    nome_proprio3 = input("\n8/10 Nome e Cognome: ")
    f_nome_comune1 = input("\n9/10 Nome comune (femminile): ")
    f_nome_comune2 = input("\n10/10 Nome comune (femminile): ")
     
    print("\nElaborazione...")
    time.sleep(0.5)
    print("\n.")
    time.sleep(0.2)
    print("\n..")
    time.sleep(0.2)
    print("\n...")
    time.sleep(1)
    
    print(f'''\nLe macchinazioni del {nome_proprio1} culminarono con l'Ordine 66, un {m_nome_comune1} segreto 
che ordinava alle truppe {m_aggettivo1} di schierarsi contro i {p_m_nome_comune1}, portando allo sterminio totale dell'Ordine {p_m_nome_comune1}.
Senza più i {p_m_nome_comune1}, {nome_proprio2} soppiantò un millennio di democrazia con un regime {m_aggettivo2}, conosciuto come Impero {m_aggettivo3}.
In più {nome_proprio2} riuscì a far passare {nome_proprio3} - il profetizzato Prescelto,
che era destinato a portare equilibrio nella {f_nome_comune1} distruggendo i Sith - al Lato Oscuro della {f_nome_comune1}
e nominandolo Darth {f_nome_comune2}.\n''')
if __name__ == '__main__':
    name_story()