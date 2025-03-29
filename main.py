import pickle

# variables
menueingabe = ""
setupeingabe = ""


# functions

def menu():
    global menueingabe
    menueingabe = input("MENU: (1) Start. (2) Setup. ")

def setup():
    global setupeingabe
    setupeingabe = input("SETUP: Gebe ein Wort ein, dass zur Liste hinzugefügt werden soll. START zum Starten. END um zum Menu zurückzukehren. ").lower()

# main

with open("wortliste.pkl", "rb") as f:
    wortliste = pickle.load(f)

print("Willkommen. ")
while True:
    menu()
    match menueingabe:
        case "1":
            print("Hier solls dann losgehen, aber soweit bin ich noch nicht. ")
            break
        case "2":
            while True:
                setup()
                match setupeingabe:
                    case "end":
                        break
                    case "start":
                        print("Hier soll dann losgehen, aber soweit bin ich noch nicht. ")
                        break
                    case _ if setupeingabe.isalpha() == False:
                        print("FEHLER: bitte nur ein einzelnes Wort eingeben. ")
                        continue
                    case _ if setupeingabe.isalpha() == True:
                        wortliste.append(setupeingabe)
                        print("Passt. " + setupeingabe + " wurde der Liste hinzugefügt. ")
                        for item in wortliste:
                            print("- " + item)
                            continue
                        with open("wortliste.pkl", "wb") as f:
                            pickle.dump(wortliste,f)
                        continue
        case _:
            print("Bitte nur 1 oder 2 eingeben.")
            continue
