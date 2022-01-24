from pyswip import Prolog

prolog = Prolog()
prolog.consult("KB.pl")

#mostra la lista dei pazienti, il loro numero
def listaPazienti():
    myTrueQuery = "prop(X, lista_pazienti, true)"
    myList = list(prolog.query(myTrueQuery))
    print("\nLista pazienti: ")
    for elem in myList:
        nPazienti = list(prolog.query("prop(" + elem["X"] + ", availability, X)."))[0]['X']
        print("-" + elem["X"] + ": " + "n.ro " + str(nPazienti))
    myFalseQuery = "prop(X, lista_pazienti, false)"
    nEmptySpots= list(prolog.query(myFalseQuery))
    if nEmptySpots:
        print("\nDovrai aggiungere questi tipi di pazienti:\n")
        for elem in nEmptySpots:
            print("- "+ elem["X"])
    print()


#incrementa il numero dei pazienti che andiamo a selezionare
def nuovoPaziente():
    listaPazienti()
    check = True
    while (check):
        status = input("Inserisci la tipologia di paziente\n").lower()
        queryStaff = "prop(" + str(status) + ",type,paziente)"
        listaDeiPazienti = list(prolog.query(queryStaff))
        if (len(listaDeiPazienti) > 0):
            while(check):
                quantity = (input("Inserisci la quantità (numerica):\n"))
                if(quantity.isnumeric()):
                    intQuantity = int(quantity)
                    myQuery = "prop(" + status + " , availability, X)"
                    initialStaff = list(prolog.query(myQuery))[0]['X']
                    prolog.retract("prop(" + status + " , availability," + str(initialStaff) + ")")
                    prolog.assertz("prop(" + status + " , availability," + str(initialStaff + intQuantity) + ")")
                    print(str(intQuantity) + " pazienti aggiunti. Il numero dello stato\"" + status + "\" è aggiornato!")
                    check = False
                else: print("Inserisci un numero")
        else:
            print("Tipologia di paziente non esistente")