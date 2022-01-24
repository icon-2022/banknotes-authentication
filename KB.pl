:- dynamic(prop/3).

%-----------------------------------------------------------------------------------------------------------------------
% RULES

% Definizione di classe
prop(X, type, C) :-
    prop(S, subClassOf, C),
    prop(X, type, S).

% Definisce il numero massimo di pazienti all'interno dello studio e quanti posti disponibili ci sono
%prop(pazientiDaAggiungere, availability, N):-
 %   prop(postiTotali, total, D),
  %  D >= N.

% Mostra le tipologie presenti all'interno dell'ambulatorio. Se hai degli spot per pazienti liberi, te li segnala
prop(E, lista_pazienti, true):-
    prop(E, type, paziente),
    prop(E, availability, N),
    N > 0.

prop(E, lista_pazienti, false):-
    prop(E, type, paziente),
    prop(E, availability, N),
    N=:=0.
%----------------------------------------------------------------------------------------------------------------------
% DATA

% PAZIENTI
prop(sottopeso_estremo, type, paziente).
prop(sottopeso, type, paziente).
prop(normopeso, type, paziente).
prop(sovrappeso, type, paziente).
prop(obeso, type, paziente).

% POSTI OCCUPATI ALL'INTERNO DELL'AMBULATORIO
prop(sottopeso_estremo, availability, 7).
prop(sottopeso, availability, 5).
prop(normopeso, availability, 2).
prop(sovrappeso, availability, 6).
prop(obeso, availability, 8).

