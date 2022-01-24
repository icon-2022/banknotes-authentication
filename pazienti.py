from pyswip import Prolog

kb = Prolog()
kb.consult("KB.pl")

def listaPazienti():
    query = "prop(X, lista_pazienti, true)"
    lista = list(kb.query(query))
    print("\nLista pazienti: ")
    for elem in lista:
        nPazienti = list(kb.query("prop(" + elem["X"] + ", occupancy, X)."))[0]['X']
        print(elem["X"] + ": " + str(nPazienti))



def nuovoPaziente():
    listaPazienti()
    check = True
    while (check):
        status = input("\nInserisci la tipologia di paziente che vuoi aggiungere\n").lower()
        queryPazienti = "prop(" + str(status) + ",type,paziente)"
        listaDeiPazienti = list(kb.query(queryPazienti))
        if (len(listaDeiPazienti) > 0):
            while(check):
                n = (input("Quanti pazienti di questa tipologia vuoi aggiungere?:\n"))
                if(n.isnumeric()):
                    intN = int(n)
                    query1 = "prop(" + status + " , occupancy, X)"
                    pazientiIniziali = list(kb.query(query1))[0]['X']
                    kb.retract("prop(" + status + " , occupancy," + str(pazientiIniziali) + ")")
                    kb.assertz("prop(" + status + " , occupancy," + str(pazientiIniziali + intN) + ")")
                    print(str(intN) + " pazienti aggiunti. Il numero dello stato\"" + status + "\" è aggiornato!")
                    check = False
                else: print("Inserisci un numero")
        else:
            print("Tipologia di paziente non esistente")