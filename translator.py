from dataclasses import dataclass

class Translator:
    def __init__(self):
        self.dizionari:list[Translator.Dizionario]=[] #dico che definisco una lista di Dizionario, ora vuota

    @dataclass
    class Dizionario:
        parolaAliena:str
        traduzione:str

        def __str__(self):
            return (f"{self.parolaAliena} {self.traduzione}")

    def printMenu(self):
        return ("1. Aggiungi nuova parola \n"
                "2. Cerca una traduzione \n"
                "3. Cerca con wildcard \n"
                "4. Stampa tutto il dizionario \n"
                "5. Exit  \n")
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        pass

    def loadDictionary(self, filename):
        with open(filename,"r", encoding="utf-8") as f:
            file=f.readlines()
            for riga in file:
                dati = riga.strip().split(" ")  # array di tipo parola aliena, traduzione
                parolaAliena = dati[0]
                traduzione=dati[1]
                nuovo = Translator.Dizionario (parolaAliena, traduzione)
                if nuovo not in self.dizionari:
                    self.dizionari.append(nuovo) #aggiungo la parola
        return self.dizionari

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        entryLower=entry.lower()
        dati = entryLower.strip().split(" ")
        parolaAliena = dati[0]
        traduzione = dati[1]

        nuovo = Translator.Dizionario(parolaAliena, traduzione)
        if nuovo in self.dizionari: #la parola è già presente
            return "cliente/parola già inserita"
        else:
            self.dizionari.append(nuovo)
            return ("parola inserita correttamente")

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        for corrisp in self.dizionari:
            if corrisp.parolaAliena == query.lower():
                return corrisp.traduzione
        return "parola non trovata"

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass