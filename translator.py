from dataclasses import dataclass

class Translator:
    def __init__(self):
        self.dizionari:list[Translator.Dizionario]=[] #dico che definisco una lista di Dizionario, ora vuota

    @dataclass
    class Dizionario:
        parolaAliena:str
        traduzione: list[str]  #la traduzione è una lista di stringhe

        def __str__(self):
            return (f"{self.parolaAliena} {self.traduzione}")

    def printMenu(self):
        return ("1. Aggiungi nuova parola \n"
                "2. Cerca una traduzione \n"
                "3. Cerca con wildcard \n"
                "4. Stampa tutto il dizionario \n"
                "5. Exit  \n")

    def loadDictionary(self, filename):
        with open(filename,"r", encoding="utf-8") as f:
            file=f.readlines()
            for riga in file:
                dati = riga.strip().split(" ")  # array di tipo parola aliena, traduzione
                parolaAliena = dati[0]
                traduzione=dati[1:] #E' UNA LISTA
                nuovo = Translator.Dizionario (parolaAliena, traduzione)
                if nuovo not in self.dizionari:
                    self.dizionari.append(nuovo) #aggiungo la parola
        return self.dizionari

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        entryLower=entry.lower()
        dati = entryLower.strip().split(" ")
        parolaAliena = dati[0]
        nuova_traduzione=dati[1:]

        # cerca se la parola esiste già
        for voce in self.dizionari:
            if voce.parolaAliena == parolaAliena:
                for t in nuova_traduzione: # aggiungi traduzioni nuove evitando duplicati
                    if t not in voce.traduzione:
                        voce.traduzione.append(t)
                return "traduzione aggiornata correttamente"

        # se non esiste, crea nuova voce
        self.dizionari.append(Translator.Dizionario(parolaAliena, nuova_traduzione))
        return "parola inserita correttamente"

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        for corrisp in self.dizionari:
            if corrisp.parolaAliena == query.lower():
                return corrisp.traduzione
        return "parola non trovata"

    def handleWildCard(self,query):

        # vincoli richiesti: al massimo un '?'
        if query.count("?") > 1:
            return "Errore: è ammesso un solo '?' nella ricerca."

        if "?" not in query:
            return self.handleTranslate(query)  #se non ci sono ?

        qpos = query.index("?")
        matches = []

        for voce in self.dizionari:
            parola = voce.parolaAliena.lower()

            if len(parola) != len(query):
                continue

            # confronto carattere per carattere tranne la posizione del '?'
            ok = True
            for i, ch in enumerate(query):
                if i == qpos:
                    continue
                if parola[i] != ch:
                    ok = False
                    break

            if ok:
                matches.append(voce)

        if not matches:
            return "Nessuna parola trovata."

        if len(matches) == 1:
            # se una sola parola soddisfa, ritorno le traduzioni
            return matches[0].traduzione

        # caso ambiguo: più parole soddisfano (es. ALI?NO -> ALIENO e ALINNO)
        return {
            "messaggio": "Ricerca ambigua: più parole soddisfano il pattern.",
            "candidati": [(v.parolaAliena, v.traduzione) for v in matches],
        }