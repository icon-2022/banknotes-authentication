from pybbn.graph.dag import Bbn
from pybbn.graph.edge import Edge, EdgeType
from pybbn.graph.jointree import EvidenceBuilder
from pybbn.graph.node import BbnNode
from pybbn.graph.variable import Variable
from pybbn.pptc.inferencecontroller import InferenceController

# Costruizione Rete Bayesiana percentuale raggiungimento obiettivi

#l'utente segue una dieta?
segueDieta = BbnNode(Variable(0, 'segue dieta', ['si', 'no']), [0.75, 0.25])

#l'utente la segue in maniera ferrea
serietàDieta = BbnNode(Variable(1, 'serietà dieta', ['alta', 'media', 'bassa']), [0.80, 0.15, 0.05])

#nodo di presentazione principale (1-2)
valorePersonale = BbnNode(Variable(2, 'valore personale', ['ottimo', 'scarso']),
                          [0.90, 0.10, 0.60, 0.40, 0.51, 0.49, 0.6, 0.4, 0.15, 0.85, 0.05, 0.95])
#l'utente è interessato a migliorare la propria condizione fisica
interesseMiglioramento = BbnNode(Variable(3, 'interesse miglioramento', ['si', 'no']), [0.85, 0.15])

#l'utente ha mai fatto sport?
esperienzaSportiva = BbnNode(Variable(4, 'esperienza sportiva', ['si', 'no']), [0.71, 0.29])

#nodo per un primo profilo dell'utente (2-5)
punteggioPersonale = BbnNode(Variable(6, 'punteggio personale', ['ottimo', 'scarso']), [0.99, 0.01, 0.72, 0.28, 0.32,
                                                                                        0.68, 0.02, 0.98])
#All'utente piace praticare sport?
gradimentoSport = BbnNode(Variable(7, 'gradimento sport', ['si', 'no']), [0.93, 0.07])

#L'utente pratica attualmente sport?
praticaSport = BbnNode(Variable(8, 'pratica sport', ['si', 'no']), [0.85, 0.15])

#nodo per la conoscenza dei linguaggi (7-8)
valoreSportivo = BbnNode(Variable(9, 'valore sportivo', ['ottima', 'scarsa']), [0.93, 0.07, 0.83, 0.17,
                                                                                          0.52, 0.48, 0.12, 0.88])

#nodo per il vincolo lavorativo (9-12)
valoreGlobale = BbnNode(Variable(13, 'valore globale', ['ottimo', 'scarso']), [0.95, 0.05, 0.68, 0.32, 0.51,
                                                                                     0.49, 0.06, 0.94])

#previsione finale della % di essere assunti (6-13)
previsioneObiettivi = BbnNode(Variable(14, 'previsione raggiungimento obiettivi', ['si', 'no']), [0.99, 0.01, 0.72, 0.28, 0.3, 0.7,
                                                                                     0.2, 0.8])

bbn = Bbn() \
    .add_node(segueDieta) \
    .add_node(serietàDieta) \
    .add_node(valorePersonale) \
    .add_node(interesseMiglioramento) \
    .add_node(esperienzaSportiva) \
    .add_node(punteggioPersonale) \
    .add_node(gradimentoSport) \
    .add_node(praticaSport) \
    .add_node(valoreSportivo) \
    .add_node(valoreGlobale) \
    .add_node(previsioneObiettivi) \
    .add_edge(Edge(segueDieta, valorePersonale, EdgeType.DIRECTED)) \
    .add_edge(Edge(serietàDieta, valorePersonale, EdgeType.DIRECTED)) \
    .add_edge(Edge(valorePersonale, punteggioPersonale, EdgeType.DIRECTED)) \
    .add_edge(Edge(gradimentoSport, valoreSportivo, EdgeType.DIRECTED)) \
    .add_edge(Edge(praticaSport, valoreSportivo, EdgeType.DIRECTED)) \
    .add_edge(Edge(valoreSportivo, valoreGlobale, EdgeType.DIRECTED)) \
    .add_edge(Edge(valoreGlobale, previsioneObiettivi, EdgeType.DIRECTED)) \
    .add_edge(Edge(punteggioPersonale, previsioneObiettivi, EdgeType.DIRECTED))

# Conversione da bbn ad albero
treeCopy = InferenceController.apply(bbn)

#Setta il valore scelto in base alla risposta data
def insertDefinedValue(tree, nodeName, optionName, value):
    ev = EvidenceBuilder() \
        .with_node(tree.get_bbn_node_by_name(nodeName)) \
        .with_evidence(optionName, value) \
        .build()
    tree.set_observation(ev)

#predizione: domande da fare all'utente
def prediction():
    tree = treeCopy.__copy__()

    while True:
        value = input(
            "Indicare se si segue una dieta:\n"
            "Risposte possibili: (si) (no)\n").lower()
        if value in ["si", "no"]:
            insertDefinedValue(tree, "segue dieta", value, 1.0)
            break

    while True:
        value = input(
            "Indicare il livello di serietà con cui si segue la dieta:\n"
            "Risposte possibili: (alta) (media) (bassa)\n").lower()
        if value in ["alta", "media", "bassa"]:
            insertDefinedValue(tree, "serietà dieta", value, 1.0)
            break

    while True:
        value = input("Ti interessa migliorare la tua condizione fisica?:\n"
                      "Risposte possibili: (si) (no)\n").lower()
        if value in ["si", "no"]:
            insertDefinedValue(tree, "interesse miglioramento", value, 1.0)
            break

    while True:
        value = input("Hai mai praticato sport):\n"
                      "Risposte possibili: (si) (no)\n").lower()
        if value in ["si", "no"]:
            insertDefinedValue(tree, "esperienza sportiva", value, 1.0)
            break

    while True:
        value = input("Ti piace lo sport?:\n"
                      "Risposte possibili: (si) (no)\n").lower()
        if value in ["si", "no"]:
            insertDefinedValue(tree, "gradimento sport", value, 1.0)
            break

    while True:
        value = input("Al momento pratichi sport?:\n"
                      "Risposte possibili: (si) (no)\n").lower()
        if value in ["si", "no"]:
            insertDefinedValue(tree, "pratica sport", value, 1.0)
            break


    print("Analisi delle tue risposte...")
    outputPrediction(tree)


#stampa la probabilità di essere assunti e,in base alla probabilità, stampa un messaggio/consiglio
def outputPrediction(tree):
    for node, posteriors in tree.get_posteriors().items():
        if node == 'previsione raggiungimento obiettivi':
            max, min = posteriors.items()
            print(f'[{node} : {max[1]*100:.0f}%]')
            if max[1] < 0.26:
                print("Probabilità di raggiungimento obiettivi: bassa.")
            elif max[1] < 0.4:
                print("Probabilità di raggiungimento obiettivi: medio-bassa.")
            elif max[1] < 0.5:
                print("Probabilità di raggiungimento obiettivi: media.")
            elif max[1] < 0.7:
                print("Probabilità di raggiungimento obiettivi: medio-alta.")
            else:
                print("Probabilità di raggiungimento obiettivi: alta.")