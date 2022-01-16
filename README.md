# banknotes-authentication
    
# Indice  

### 1. [Introduzione](#1)  
  
### 2. [Modello di dominio](#2)  
 1. [XXX](#2.1)  
     1.1 [XXX](#2.1.1)  

### 3. [Requisiti specifici](#3)          
 1. [Requisiti funzionali](#3.1)          
 2. [Requisiti non funzionali](#3.2)             

### 4. [Manuale utente](#4)
 1. [XXX](#4.1)  
    1.1 [XXX](#4.1.1)      
              
# <span id = "1">1. Introduzione</span> 
<p style='text-align: justify;'> 
<p>Negli Stati Uniti c'è circa una banconota contraffatta ogni 10.000 banconote autentiche. Da quando negli ultimi anni è stato lanciato il servizio di deposito diretto in contanti ai bancomat, le banconote contraffatte sono diventate un problema non solo per i commercianti, ma anche per le banche. Sebbene siano quasi impossibili da identificare ad occhio nudo, l'elaborazione delle immagini è un metodo che può essere utilizzato per individuare le discrepanze nelle banconote contraffatte.</p>
<p>Dato un set di dati di oltre mille banconote con 4 attributi ciascuno, possiamo utilizzare modelli di apprendimento automatico come la regressione logistica e K-neirest neighbors per addestrare un'IA per classificare le banconote.</p>
<p>Le immagini sono state tratte da banconote autentiche e contraffatte (n=1372). Ci sono quattro attributi in questo set di dati: varianza dell'immagine trasformata Wavelet (WTI), asimmetria del WTI, curvatura del WTI, entropia dell'immagine. L'ultima colonna è la classificazione della banconota (dove il valore 0 è falso e 1 è autentico). In matematica, una serie wavelet è una rappresentazione di una funzione di integrale quadrato (con valori reali o complessi) per determinate serie ortonormali generate da una wavelet. Queste wavelet di valori vengono definite utilizzando varianza e asimmetria vengono trasformate in valori di immagine. Qui il file csv di input è composto da 1372 istanze diviso in 4 valori come V1, V2, V3 e V4. Eccoci qui utilizzando solo i valori V1 e V2. I valori sono classificati in due classi 1 e 2.</p>
</p>
<a href="#top">Torna all'inizio</a> 

# <span id = "2">2. Modello di dominio</span> 
     
## <span id = "2.1">2.1. XXX</span> 

### <span id = "2.1.1">2.1.1 XXX</span>

<p><a href="#top">Torna all'inizio</a>

# <span id = "3">3. Requisiti specifici</span> 
Questa sezione specifica tutti i requisiti per il software di gioco degli scacchi. I requisiti si riferiscono a 
funzionalità e vincoli.     
  
## <span id = "3.1">3.1 Requisiti funzionali</span> 
I FUR *(Functional User Requirement)* descrivono le funzionalità del software in termini di:
 - servizi che il software stesso deve fornire;
 - risposte che l’utente aspetta dal software in determinate condizioni;
 - risultati che il software deve produrre in risposta a specifici input.
 
Questa applicazione fornisce le seguenti funzionalità:  

| Requisito | Descrizione |
|--|--|
| Mostrare l'elenco dei comandi | Al comando <code>help</code> l'applicazione deve mostrare una lista di comandi, uno <br>per riga. |
| Iniziare una nuova partita | Al comando <code>play</code> l'applicazione si deve predisporre a ricevere comandi <br>tra cui la prima mossa del bianco ed è in grado di ricevere altri comandi <br>di gioco (es. <code>show</code>). |
| Mostrare la scacchiera | Al comando <code>board</code>, l'applicazione deve mostrare i pezzi in formato <br>Unicode e la loro posizione sulla scacchiera. |
| Muovere un Pedone | L'applicazione deve accettare mosse in [notazione algebrica abbreviata in<br>italiano](https://it.wikipedia.org/wiki/Notazione_algebrica), rispetta le regole degli scacchi, il Pedone può catturare pezzi, <br>può catturare in en passant, se si tenta una mossa non valida è mostrato il <br>messaggio <code>mossa non valida</code> e l'applicazione rimane in attesa di una mossa <br>valida. |
| Muovere un Cavallo | L'applicazione deve accettare mosse in [notazione algebrica abbreviata in<br>italiano](https://it.wikipedia.org/wiki/Notazione_algebrica), rispetta le regole degli scacchi, il Cavallo può catturare pezzi, se si <br>tenta una mossa non valida è mostrato il messaggio <code>mossa non valida</code> e <br>l'applicazione rimane in attesa di una mossa valida. |
| Muovere un Alfiere | L'applicazione deve accettare mosse in [notazione algebrica abbreviata in<br>italiano](https://it.wikipedia.org/wiki/Notazione_algebrica), rispetta le regole degli scacchi, l'Alfiere può catturare pezzi, se si <br>tenta una mossa non valida è mostrato il messaggio <code>mossa non valida</code> e <br>l'applicazione rimane in attesa di una mossa valida. |
| Muovere una Torre | L'applicazione deve accettare mosse in [notazione algebrica abbreviata in<br>italiano](https://it.wikipedia.org/wiki/Notazione_algebrica), rispetta le regole degli scacchi, la Torre può catturare pezzi, se si <br>tenta una mossa non valida è mostrato il messaggio <code>mossa non valida</code> e <br>l'applicazione rimane in attesa di una mossa valida. |
| Muovere la Donna | L'applicazione deve accettare mosse in [notazione algebrica abbreviata in<br>italiano](https://it.wikipedia.org/wiki/Notazione_algebrica), rispetta le regole degli scacchi, la Donna può catturare pezzi, se si <br>tenta una mossa non valida è mostrato il messaggio <code>mossa non valida</code> e <br>l'applicazione rimane in attesa di una mossa valida. |
| Muovere il Re | L'applicazione deve accettare mosse in [notazione algebrica abbreviata in<br>italiano](https://it.wikipedia.org/wiki/Notazione_algebrica), rispetta le regole degli scacchi, il Re può catturare pezzi, se si <br>tenta una mossa non valida è mostrato il messaggio <code>mossa non valida</code> e <br>l'applicazione rimane in attesa di una mossa valida. |
| Arroccare corto | L'applicazione deve accettare mosse in [notazione algebrica abbreviata in<br>italiano](https://it.wikipedia.org/wiki/Notazione_algebrica), rispetta le regole degli scacchi, il giocatore non ha ancora mosso né <br>il Re né la Torre coinvolti nell'arrocco, non ci devono essere pezzi (amici o <br>avversari) fra il Re e la Torre utilizzata, né la casa di partenza del Re, né la <br>casa che esso deve attraversare e né quella di arrivo devono essere <br> minacciate da un pezzo avversario, se si tenta una mossa non valida è <br>mostrato il messaggio <code>mossa non valida</code> e l'applicazione rimane in attesa <br>di una mossa valida. |
| Arroccare lungo | L'applicazione deve accettare mosse in [notazione algebrica abbreviata in<br>italiano](https://it.wikipedia.org/wiki/Notazione_algebrica), rispetta le regole degli scacchi, il giocatore non ha ancora mosso né <br>il Re né la Torre coinvolti nell'arrocco, non ci devono essere pezzi (amici o <br>avversari) fra il Re e la Torre utilizzata, né la casa di partenza del Re, né la <br>casa che esso deve attraversare e né quella di arrivo devono essere <br> minacciate da un pezzo avversario, se si tenta una mossa non valida è <br>mostrato il messaggio <code>mossa non valida</code> e l'applicazione rimane in attesa <br>di una mossa valida. |
| Mostrare le mosse giocate | Al comando <code>moves</code> l'applicazione deve mostrare la storia delle mosse con <br>[notazione algebrica abbreviata in italiano](https://it.wikipedia.org/wiki/Notazione_algebrica). |
| Mostrare le catture | Al comando <code>captures</code> l'applicazione deve mostra la lista delle catture del <br> giocatore Bianco e del Nero con caratteri Unicode. |
| Mostrare le mosse giocate | Al comando <code>moves</code> l'applicazione deve mostrare la storia delle mosse con <br>[notazione algebrica abbreviata in italiano](https://it.wikipedia.org/wiki/Notazione_algebrica). |
| Chiudere il gioco | Al comando <code>quit</code> l'applicazione si deve chiude e compare il prompt del <br>sistema operativo. |

## <span id = "3.2">3.2 Requisiti non funzionali</span>  
I NFR *(Non Functional Requirement)* descrivono le caratteristiche di qualità del prodotto software da sviluppare, i 
requisiti di sistema/ambiente, le tecnologie e gli standard di cui il software deve tenere conto.

<table>
<thead>
  <tr>
    <th>Requisito</th>
    <th>Sottorequisito</th>
    <th>Descrizione</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="3">Usabilità</td>
    <td>Apprendibilità</td>
    <td>Il software prevede che l'utente conosca le regole generali del gioco degli Scacchi e la notazione algebrica abbreviata italiana.</td>
  </tr>
  <tr>
    <td>Protezione dall’errore utente</td>
    <td>Il livello di protezione dagli errori dell'utente consiste nella rigorosa analisi dell'input con opportune notifiche di comandi o mosse errate.</td>
  </tr>
  <tr>
    <td>Estetica dell’interfaccia utente</td>
    <td>Il software implementata una TUI <em>(Text-based user interfaces)</em> rappresentando le case della scacchiera attraverso ANSI escape code e i pezzi attraverso caratteri Unicode. La gradevolezza dell’uso dell’interfaccia utente è garantita da uno profondo studio dei colori su diverse tipologie di terminale aventi diversi temi.</td>
  </tr>
  <tr>
    <td rowspan="3">Manutenibilità</td>
    <td>Modularità</td>
    <td>Il sotware è creato utilizzando le best practices del linguaggio OO Java ed è suddiviso in package e classi in modo che le modifiche abbiano un minimo impatto sulle altre componenti.</td>
  </tr>
  <tr>
    <td>Riusabilità</td>
    <td>Il software è progettato in modo da poter essere utilizzato per l'implementazione di altri giochi simili (es. Dama) apportando lievi modifiche.</td>
  </tr>
  <tr>
    <td>Testabilità</td>
    <td>Il software è testato attraverso il framework JUnit, tutto documentato attraverso Coveralls e il toolkit JaCoCo, che garantiscono la totale copertura. Alcune classi sono provviste del proprio <code>main</code> per poter essere eseguite e testate autonomamente (es. ParserPGN.java ricevendo in input una partita in formato PGN)</td>
  </tr>
  <tr>
    <td rowspan="4">Portabilità</td>
    <td>Adattabilità</td>
    <td>La larghezza dello schermo prevede un minimo di 80 caratteri.</td>
  </tr>
  <tr>
    <td>Installabilità</td>
    <td> L'unico software da installare per far funzionare l'applicazione è Docker che consente di creare ed eseguire container su Linux, Windows e macOS.</td>
  </tr>
</tbody>
</table>  
<a href="#top">Torna all'inizio</a>

# <span id = "4">4. Manuale utente</span> 

<a href="#top">Torna all'inizio</a> 
