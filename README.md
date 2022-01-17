# banknotes-authentication

di Nicole Stolbovoi [MAT. 709168] e Luca Zeverino [MAT. 698710]

# Indice  

### 1. [Introduzione](#1)  
  
### 2. [Metodologia](#2) 
 1. [Apprendimento](#2.1)  
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

## <span id = "2.1">2.1. Apprendimento</span>
<p align="justify">L'apprendimento si riferisce al machine learning che generalmente con l'idea di non dare istruzioni esplicite al computer su come eseguire un compito, ma piuttosto dare al computer l'accesso alle informazioni sotto forma di dati da cui può imparare, e lasciare che il computer provi a capire quali siano gli schemi per cercare di svolgere un compito da solo.

<p align="justify">L'apprendimento automatico è disponibile in diverse forme ed è un campo molto ampio. in questa sezione si definiscono alcuni degli algoritmi alla base di molte delle diverse aree dell'apprendimento automatico. Una delle branche più popolari è l'apprendimento supervisionato, che si riferisce all'attività in cui diamo al computer l'accesso a un dataset, in cui tale dataset è costituito da coppie input-output. L'obiettivo è che il computer (che la nostra intelligenza artificiale) sia in grado di capire le funzioni che associano gli input agli output, prevedendo quest'utlimo. Quindi si forniscono alcuni dati in modo che il computer possa addestrare il suo modello per capire come gli input e gli output sono in relazione tra loro. Infine si vuole che il computer sia in grado di capire la funzione che, dati quegli input, sia in grado di ottenere quegli output.

<p align="justify">Uno dei compiti principali dell'apprendimento supervisionato è noto come classificazione. La classificazione è il problema in cui si vuole mappare l'input in categorie discrete, ed il compito del computer è proprio prevedere quali sono queste categorie. Un esempio è avere informazioni su una banconota e chiedere di prevedere se appartiene alla categoria delle banconote autentiche o appartiene alla categoria delle banconote contraffatte. È quindi necessario classificare l'input e addestrare il computer per essere in grado di eseguire quel calcolo. In questo caso i dati sono strutturati in una tabella con delle etichette, ovvero assiomi che l'umano ha constato.E quello che il computer dovrebbe fare allora è riuscire a capire, dati questi input, quale etichetta dovrebbe essere associata a quella banconota. 
  
## <span id = "2.2">2.2. Tecniche di ML</span> 
### <span id = "2.2.1">2.2.1 Support Vector Machine</span>
### <span id = "2.2.2">2.2.2 Perceptron</span>
<p align="justify">Quello che si vuole fare è provare a usare una tecnica nota come regressione lineare per trovare una sorta di linea che separi le due metà l'una dall'altra. Il risultato, che dobbiamo solo confrontare: è maggiore di 0 o è inferiore a 0 per dire che non appartiene a un lato della linea o all'altro lato della linea.
  



  
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
<p align="justify">Il set di evidenze di training viene archiviato come <code>X_training</code>, mentre il set di etichette di training viene archiviato come <code>y_training</code>, quindi passato al metodo <code>fit()</code>.
  
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
