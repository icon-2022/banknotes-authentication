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
Questo documento è una relazione tecnica finale per il progetto che implementa il gioco degli Scacchi del gruppo Thacker.     
<p>Lo scopo di questo progetto è quello di creare un'applicazione, in completa conformità con il regolamento degli scacchi 
FIDE, che possa essere utilizzata da utenti che abbiano una conoscenza almeno dilettantistica di quest'ultimo.   
<p>L'applicazione può ricevere l'input in modalità interattiva, utilizzando la notazione algebrica italiana, oppure in   
modalità batch con una partita registrata in formato PGN <em>(Portable Game Notation)</em>, utilizzando la notazione   
algebrica inglese.   
<p>Supporta partite interattive esclusivamente contro avversari umani.   
<p>Si osserva che l'obiettivo di questo progetto è quello di dimostrare le competenze acquisite durante le lezioni del   
corso di Ingegneria del Software, piuttosto che produrre una soluzione completa e avanzata.    

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
