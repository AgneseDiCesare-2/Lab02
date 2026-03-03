import translator as tr

t = tr.Translator()
t.loadDictionary("dictionary.txt")
continua=True

while(continua):

    print(t.printMenu())
    txtIn = (input("scegli un'opzione: ")).strip()

    if not txtIn.isdigit():
        print ("input non valido")

    # Add input control here!

    if int(txtIn) == 1:
        parola = input("Inserisci: <parola_aliena> <traduzione>: "). strip().lower()
        if not parola.isalpha():
            print("Errore: la parola deve contenere solo lettere.")
            continue
        print(t.handleAdd(parola))

    if int(txtIn) == 2:
        query = input("Parola aliena da tradurre: ").strip()
        if not query.isalpha():
            print("Errore: la parola deve contenere solo lettere.")
            continue
        print(t.handleTranslate(query))

    if int(txtIn) == 3:
        pass

    if int(txtIn) == 4:
        #leggi tutto il dizionario
        for corrisp in t.dizionari:
            print(corrisp)

    if int(txtIn) == 5:
        continua=False
