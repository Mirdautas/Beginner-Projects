import time
def name_story():
    f_nome_comune1 = input("\n1/10 Nome comune (femminile): ")
    magia = input("\n2/10 Magia: ")
    f_nome_comune2 = input("\n3/10 Nome comune (femminile): ")
    verbo1 = input("\n4/10 Verbo: ")
    f_nome_comune3 = input("\n5/10 Nome comune (femminile): ")
    p_m_nome_comune1 = input("\n6/10 Nome comune (plurale, maschile): ")
    nome_comune1 = input("\n7/10 Nome comune: ")
    p_m_nome_comune2 = input("\n8/10 Nome comune (plurale, maschile): ")
    m_nome_comune1 = input("\n9/10 Nome comune (maschile): ")
    nome_proprio = input("\n10/10 Nome proprio: ") 
    print("\nElaborazione...")
    time.sleep(0.5)
    print("\n.")
    time.sleep(0.2)
    print("\n..")
    time.sleep(0.2)
    print("\n...")
    time.sleep(1)
    
    print(f'''\nHarry decise in un lampo. Prima che Piton potesse fare anche solo un
passo verso di lui, alzò la {f_nome_comune1}.
«{magia}» gridò. Ma la sua non fu la sola {f_nome_comune2} a {verbo1}. Si udì un
lampo che fece tremare la {f_nome_comune3} sui {p_m_nome_comune1}; Piton fu sollevato da terra e 
sbatté contro il muro, poi scivolò a terra, con un rivolo di {nome_comune1} che gli
scorreva tra i {p_m_nome_comune2}. Era svenuto.
Harry si guardò intorno. Ron e Hermione avevano cercato di disarmare
Piton esattamente nello stesso istante.
La {f_nome_comune1} di Piton disegnò un alto arco a mezz'aria e atterrò sul {m_nome_comune1}, vicino a {nome_proprio}.\n''')
if __name__ == '__main__':
    name_story()
