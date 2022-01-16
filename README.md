# banknotes-authentication

di Nicole Stolbovoi [MAT. 709168] e Luca Zeverino [MAT. ]

# Indice  

### 1. [Introduzione](#1)  
  
### 2. [Metodologia](#2)  
 1. [XXX](#2.1)  
     1.1 [XXX](#2.1.1)  

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
     
## <span id = "2.1">2.1. XXX</span> 

### <span id = "2.1.1">2.1.1 XXX</span>
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
 
<p>Sono stati utilizzati gli algoritmi: Support Vector Machines, K Nearest Neighbor (1), Perceptron Learning e Gaussian Naive Bayes, i quattro più comuni per i problemi di classificazione dell'apprendimento automatico.
  
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
## <span id = "3.2">3.2 Caricamento dataset</span>  
## <span id = "3.3">3.3 Divisione degli attributi</span>  
## <span id = "3.4">3.4 Separazione del dataset</span>
## <span id = "3.5">3.5 Addestramento sul training set</span>
## <span id = "3.6">3.6 Predizione sul testing set</span>
## <span id = "3.7">3.7 Valutazione delle prestazioni</span>
<p><a href="#top">Torna all'inizio</a>

# <span id = "4">4. Conclusioni</span> 
<p><a href="#top">Torna all'inizio</a>
