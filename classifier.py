from pandas import read_csv
from sklearn.tree import DecisionTreeClassifier

attributi = read_csv('status.csv')
X = attributi.drop(columns=['stato'])
y = attributi['stato']

modello = DecisionTreeClassifier()
modello.fit(X.values, y.values)

def domanda():
    sesso = ""
    altezza = 0
    peso = 0
    result1 = True
    result2 = True
    while(sesso != "maschio" and sesso != "femmina"):
        sesso = input("Inserisci il tuo sesso (maschio/femmina): ").lower()
        if(sesso == "maschio"):
         firstParameter = 0
        elif(sesso == "femmina"):
         firstParameter = 1
        else:
         print("Stai sbagliando qualcosa, rileggi attentamente ciò che ti viene chiesto!")

    while (peso < 30 or peso > 150):
        try:
            while (result1):
                peso = (int)(input("Inserisci il tuo peso in kg' (intero da 30 a 150): "))
                if (peso < 30 or peso > 150):
                    print("Il valore inserito non è valido...ritenta")
                else:
                    result1 = False
        except ValueError:
            print("Ti avevo chiesto di inserire un numero...")

    while (altezza < 120 or altezza > 210):
        try:
            while (result2):
                altezza = (int)(input("Inserisci la tua altezza in cm' (intero da 120 a 210): "))
                if (altezza < 120 or altezza > 210):
                    print("Il valore inserito non è valido...ritenta")
                else:
                    result2 = False
        except ValueError:
            print("Ti avevo chiesto di inserire un numero...")
    stato = modello.predict([[firstParameter, peso, altezza]])
    print(stato)