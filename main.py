import pickle

# variables
menueingabe = ""
setupeingabe = ""
wortliste = []
# functions

def menu():
    global menueingabe
    menueingabe = input("MENU: START or SETUP. ").lower()

def setup():
    global setupeingabe
    setupeingabe = input("SETUP: Gebe ein Wort ein, dass zur Liste hinzugefügt werden soll. \n" \
    "... LIST um Wortliste anzuzeigen. START zum Starten. END um zum Menu zurückzukehren. ").lower()

# def start():

# main
try:
    with open("wortliste.pkl", "rb") as f:
        wortliste = pickle.load(f)
except:
    print(" ")

print("Willkommen. ")
while True:
    menu()
    match menueingabe:
        case "start":
            print("Hier solls dann losgehen, aber soweit bin ich noch nicht. ")
            break
        case "setup":
            while True:
                setup()
                match setupeingabe:
                    case "end":
                        with open("wortliste.pkl", "wb") as f:
                            pickle.dump(wortliste, f)
                            f.close
                        break
                    case "start":
                        print("Hier soll dann losgehen, aber soweit bin ich noch nicht. ")
                        break
                    case "list":
                        for item in wortliste:
                            print("- " + item)
                            continue
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
                            pickle.dump(wortliste, f)
                        continue
        case _:
            print("FEHLER: Bitte nur START oder SETUP eingeben.")
            continue
