:- dynamic(prop/3).

prop(X, type, C) :- prop(S, subClassOf, C), prop(X, type, S).


prop(E, lista_pazienti, true):- prop(E, type, paziente), prop(E, occupancy, N), N >= 0.


% Pazienti
prop(sottopeso_estremo, type, paziente).
prop(sottopeso, type, paziente).
prop(normopeso, type, paziente).
prop(sovrappeso, type, paziente).
prop(obeso, type, paziente).

% Posti occupati all'interno dell'ambulatorio
prop(sottopeso_estremo, occupancy, 7).
prop(sottopeso, occupancy, 5).
prop(normopeso, occupancy, 2).
prop(sovrappeso, occupancy, 6).
prop(obeso, occupancy, 8).

