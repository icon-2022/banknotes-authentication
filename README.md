# banknotes-authentication

di Nicole Stolbovoi [MAT. 709168] e Luca Zeverino [MAT. 698710]

# Indice  

### 1. [Introduzione](#1)  

### 2. [Metodologia](#2)
 1. [Apprendimento supervisionato](#2.1)  
 2. [Tecniche di ML](#2.2)  
     2.1 [Support Vector Machine](#2.2.1)  
     2.2 [Perceptron](#2.2.2)  
     2.3 [Gaussian Naive Bayes](#2.2.3)  
     2.4 [KNearest Neighbors](#2.2.4)  

### 3. [Modellazione](#3)          
 1. [Importazione delle librerie](#3.1)          
 2. [Caricamento dataset](#3.2)
 3. [Divisione degli attributi](#3.3)             
 4. [Separazione del dataset](#3.4)
 5. [Addestramento sul training set](#3.5)             
 6. [Predizione sul testing set](#3.6)             
 7. [Valutazione delle prestazioni](#3.7)             

### 4. [Conclusioni](#4)

# <span id = "1">1. Introduzione</span>
<p align="justify">Negli Stati Uniti c'è circa una banconota contraffatta ogni 10.000 banconote autentiche. Da quando negli ultimi anni è stato lanciato il servizio di deposito diretto in contanti ai bancomat, le banconote contraffatte sono diventate un problema non solo per i commercianti, ma anche per le banche. Sebbene siano quasi impossibili da identificare ad occhio nudo, l'elaborazione delle immagini è un metodo che può essere utilizzato per individuare le discrepanze nelle banconote contraffatte.</p>
<p align="justify">Dato un set di dati di oltre mille banconote con 4 attributi ciascuno, possiamo utilizzare modelli di apprendimento automatico come la regressione logistica e K-neirest neighbors per addestrare un'IA per classificare le banconote.</p>
<p align="justify">Le immagini sono state tratte da banconote autentiche e contraffatte (n=1372). Ci sono quattro attributi in questo set di dati: varianza dell'immagine trasformata Wavelet (WTI), asimmetria del WTI, curvatura del WTI, entropia dell'immagine. L'ultima colonna è la classificazione della banconota (dove il valore 0 è falso e 1 è autentico). In matematica, una serie wavelet è una rappresentazione di una funzione di integrale quadrato (con valori reali o complessi) per determinate serie ortonormali generate da una wavelet.</p>
<p><a href="#top">Torna all'inizio</a>

# <span id = "2">2. Metodologia</span>
<p align="justify">I modelli sperimentali sono stati configurati utilizzando il metodo <code>holdout</code>. Questo metodo separa il dataset in due sottoinsiemi (rapporto 60:40) chiamati training set e testing set. Il training set viene utilizzato per addestrare il classificatore mentre il testing set viene utilizzato per stimare il tasso di errore del classificatore addestrato.

## <span id = "2.1">2.1. Apprendimento supervisionato</span>
<p align="justify">L'apprendimento supervisionato è una tecnica di apprendimento automatico che mira a istruire un sistema informatico in modo da consentirgli di predire i valori di output di un sistema rispetto ad un input sulla base di una serie di esempi, costituiti da coppie di input e di output, che gli vengono inizialmente forniti. L'obiettivo è quindi predire i valori delle caratteristiche di output dalle caratteristiche di input.

<p align="justify">Una caratteristica è una funzione da esempi in un valore. Il dominio di una caratteristica è l'insieme di valori che può restituire.

<p align="justify">In un task di apprendimento supervisionato, al sistema è dato

  - una serie di funzioni di input
  - una serie di caratteristiche target
  - una serie di esempi di addestramento, in cui vengono forniti i valori per le caratteristiche di input e le                 caratteristiche di output per ciascun esempio, e
  - una serie di esempi di test, in cui vengono forniti solo i valori per le caratteristiche di input.

## <span id = "2.2">2.2. Tecniche di ML</span>

### <span id = "2.2.1">2.2.1 Support Vector Machine</span>
<p align="justify">Le macchine a vettori di supporto (SVM, dall'inglese Support Vector Machines) sono dei modelli di apprendimento supervisionato associati ad algoritmi di apprendimento per la regressione e la classificazione. Dato un insieme di esempi per l'addestramento, ognuno dei quali etichettato con la classe di appartenenza fra le due possibili classi, un algoritmo di addestramento per le SVM costruisce un modello che assegna i nuovi esempi a una delle due classi, ottenendo quindi un classificatore lineare binario non probabilistico. Un modello SVM è una rappresentazione degli esempi come punti nello spazio, mappati in modo tale che gli esempi appartenenti alle due diverse categorie siano chiaramente separati da uno spazio il più possibile ampio. I nuovi esempi sono quindi mappati nello stesso spazio e la predizione della categoria alla quale appartengono viene fatta sulla base del lato nel quale ricade.
 
I vantaggi delle macchine a vettore di supporto sono: 
 - Efficace in spazi ad alta dimensione. 
 - Efficace nei casi in cui il numero di dimensioni è maggiore del numero di campioni. 

Utilizza un sottoinsieme di punti di addestramento nella funzione decisionale (chiamati vettori di supporto), quindi è anche efficiente in termini di memoria.
 
Gli svantaggi delle macchine vettoriali di supporto includono: 
 - Se il numero di funzionalità è molto maggiore del numero di campioni, evitare un adattamento eccessivo nella scelta delle funzioni del kernel e il termine di regolarizzazione è   fondamentale. 

SVC è una classe in grado di eseguire la classificazione binaria e multiclasse su un dataset.
### <span id = "2.2.2">2.2.2 Perceptron</span>
<p align="justify">Il perceptron è un algoritmo per l'apprendimento supervisionato di classificatori binari. Un classificatore binario è una funzione che può decidere se un input, rappresentato da un vettore di numeri, appartiene o meno a una classe specifica. È un tipo di classificatore lineare, ovvero un algoritmo di classificazione che effettua le sue previsioni sulla base di una funzione predittrice lineare che combina un insieme di pesi con il vettore delle caratteristiche.

### <span id = "2.2.3">2.2.3 Gaussian Naive Bayes</span>

### <span id = "2.2.4">2.2.4 KNearest Neighbors</span>
<p align="justify">I K esempi di training che hanno le caratteristiche di input più vicine all'esempio vengono usati per predire il valore per il nuovo esempio. La previsione potrebbe essere la moda, la media o una qualche interpolazione tra la previsione di questi K esempi di training.

Affinché questo metodo funzioni, è necessaria una metrica della distanza che misuri la vicinanza di due esempi. Innanzitutto si definisce una metrica per il dominio di ciascuna caratteristica, in cui i valori delle caratteristiche vengono convertiti in una scala numerica che viene utilizzata per confrontare i valori. La distanza euclidea, la radice quadrata della somma dei quadrati delle differenze dimensionali, potrebbe essere utilizzata come distanza tra due esempi. Una questione importante sono le scale relative di diverse dimensioni; aumentando la scala di una dimensione aumenta l'importanza di quella caratteristica.

I pesi delle caratteristiche possono essere forniti come input. È anche possibile imparare questi pesi. L'agente di apprendimento cercherà di trovare pesi che minimizzino l'errore nella previsione del valore di ciascun elemento del set di addestramento, sulla base di ogni altra istanza nel set di addestramento. Questa è un'istanza di convalida incrociata leave-one-out.

<p align="justify">Quali sono gli svantaggi della classificazione k-neighbor più vicino? Uno è che è abbastanza lento dover attraversare e misurare la distanza tra un punto e ognuno di questi punti vicini. Ma ci sono modi per cercare di aggirarlo. Esistono strutture di dati che possono aiutare a rendere più rapidamente possibile trovare questi vicini. Ci sono anche tecniche che puoi usare per provare a sfoltire alcuni di questi dati, rimuovere alcuni dei punti dati in modo da rimanere solo con i punti dati rilevanti solo per renderlo un po' più semplice.
<p><a href="#top">Torna all'inizio</a>

# <span id = "3">3.Modellazione e analisi</span>

## <span id = "3.1">3.1 Importazione librerie</span>
Il seguente script viene utilizzato per importare i moduli Python:

```
import csv
import random
import sys
import pprint
import time
from tabulate import tabulate
from numpy import *
```

<p align="justify">Sono stati utilizzati gli algoritmi: Support Vector Machines, K Nearest Neighbor (1), Perceptron Learning e Gaussian Naive Bayes, i quattro più comuni per i problemi di classificazione dell'apprendimento automatico:

```
from sklearn import svm
from sklearn.linear_model import Perceptron
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

︙

for x in range(4):

    if x == 0:
        model = Perceptron()
    if x == 1:
        model = svm.SVC()
    if x == 2:
        model = KNeighborsClassifier(n_neighbors=1)
    if x == 3:
        model = GaussianNB()
```

<p align="justify">Si noti che dopo aver importato gli algoritmi, possiamo scegliere quale modello utilizzare. Il resto del codice rimarrà lo stesso.</p>

## <span id = "3.2">3.2 Caricamento dataset</span>  
<p align="justify">Una volta importate le librerie, il passaggio successivo consiste nel caricare il dataset nella nostra applicazione. Quindi apriamo il file con le funzionalità di base del file python e utilizziamo la funzione <code>csv.reader()</code> del modulo csv, che legge il dataset nel formato CSV.</p>

```
# Read data from file
with open("banknotes.csv") as f:
    reader = csv.reader(f)
    next(reader)
```

## <span id = "3.3">3.3 Divisione degli attributi</span>  
<p align="justify">In questo dataset, varianza, inclinazione, curvatura ed entropia sono caratteristiche mentre la colonna della classe contiene l'etichetta. Lo script seguente, insieme alla parte sopra menzionata, divide i dati in evidenze e etichette. Quindi archivia le evidenze e l'etichetta in una elenco <code>data = []</code>.  

```
    data = []
    for row in reader:
        # print(row)
        data.append({
            "evidence": [float(cell) for cell in row[:4]],
            "label": "Authentic" if row[4] == "0" else "Counterfeit"
```

<p align="justify">Il ciclo <code>for</code> è l'indice che vogliamo filtrare dal nostro dataset, nella riga <code>"evidence": [float(cell) for cell in row[:4]]</code> filtriamo dalla colonna 0 alla colonna 3 che contiene l'insieme degli attributi evidenti. Nella riga <code>"label": "Authentic" if row[4] == "0" else "Counterfeit"</code>, abbiamo filtrato solo i record dalla colonna quattro che contiene le etichette (classe). Se l'etichetta è 0, la banconota è autentica e quando l'etichetta è 1, la banconota è contraffatta/falsa.</p>  

## <span id = "3.4">3.4 Separazione del dataset</span>
<p align="justify">Il training set viene utilizzato per addestrare gli algoritmi di apprendimento automatico mentre il testing set viene utilizzato per valutare le prestazioni degli algoritmi di apprendimento automatico.

```
# Separate data into training and testing groups
holdout = int(0.40 * len(data)) # prende 40% del dataset
random.shuffle(data) # mischia dati
testing = data[:holdout]
training = data[holdout:]
```

<p align="justify">Innanzitutto, calcoliamo la lunghezza dell'elenco di dati in <code>holdout = int(0.40 * len(data))</code> e mescoliamo gli elementi dei dati per prestazioni migliori utilizzando la funzione <code>random.shuffle()</code> dal modulo random. Quindi memorizziamo il 40% dei dati nel gruppo testing e il 60% dei dati nel gruppo training.</p>

## <span id = "3.5">3.5 Addestramento sul training set</span>
<p align="justify">Il set di evidenze di training viene archiviato come <code>X_training</code> (input), mentre il set di etichette di training viene archiviato come <code>y_training</code> (output), quindi passato al metodo <code>fit()</code>.

```
    # Train model on training set
    X_training = [row["evidence"] for row in training]
    y_training = [row["label"] for row in training]
    model.fit(X_training, y_training)
```

## <span id = "3.6">3.6 Predizione sul testing set</span>
<p align="justify">Dopo aver addestrato l'algoritmo, abbiamo eseguito previsioni sul set di test. Per fare previsioni, viene utilizzato il metodo <code>predict()</code>. I record da prevedere vengono passati come parametri al metodo <code>predict()</code> come mostrato di seguito:

```
    # Make predictions on the testing set
    X_testing = [row["evidence"] for row in testing]
    y_testing = [row["label"] for row in testing]
    predictions = model.predict(X_testing)
```

## <span id = "3.7">3.7 Valutazione delle prestazioni</span>
Abbiamo valutato le prestazioni del modello attraverso un semplice codice Python:

```
    # Compute how well we performed
    correct = 0
    incorrect = 0
    total = 0
    for actual, predicted in zip(y_testing, predictions):
        total += 1
        if actual == predicted:
            correct += 1
        else:
            incorrect += 1
```

e infine stampiamo l'accuratezza del modello per migliorarne la comprensione:

```
    res[x+1][0] = type(model).__name__
    res[x+1][1] = correct
    res[x+1][2] = incorrect
    res[x+1][3] = f"{100 * correct / total:.2f}"
    res[x+1][4] = f"{time.process_time() - t:.4f}"

print (tabulate(res[1:], headers=res[0]))
```

<p><a href="#top">Torna all'inizio</a>

# <span id = "4">4. Conclusioni</span>
<p align="justify">In questo progetto abbiamo spiegato come abbiamo risolto il problema dell'autenticazione delle banconote utilizzando tecniche di machine learning. Abbiamo confrontato quattro diversi algoritmi in termini di prestazioni e abbiamo concluso che gli algoritmi KNN e SVM sono i migliori algoritmi per l'autenticazione delle banconote con una precisione del 100% e del 99,45%.</p>
<p><a href="#top">Torna all'inizio</a>


```
Model           Correct    Incorrect    Accuracy (%)    Cost (ms)
------------  ---------  -----------  --------------  -----------
Perceptron          542            6           98.91            7
SVC                 546            2           99.64           16
KNeighborsCl        548            0          100              62
GaussianNB          465           83           84.85            6
LogisticRegr        543            5           99.09           24
```
