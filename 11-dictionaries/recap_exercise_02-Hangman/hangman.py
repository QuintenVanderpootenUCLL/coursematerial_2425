list_of_words = ["Bart", "Robbe", "Vliegtuig", "Koningspinguin", "Boom"]
Correct_word = list_of_words[int(input(f"Kies het woord aan de hand van een nummer tussen 1 en {len(list_of_words)} ")) - 1]
#Hier wordt het woord gekoze


#vanaf hier gaan we spelen
doorgaan = True
verborgen = "_" * len(Correct_word)
gegokte_letters = set()
levens = 5
leven_teken = " \u2764\uFE0F "
def guess(gevonden, Correct_word):
    global verborgen
    global levens
    global gegokte_letters
    global doorgaan
    print(f"Dit zijn jouw gevonden letters {verborgen} \naantal levens:{leven_teken * levens}")
    print(f"Deze letters heb je al gegegokt{gegokte_letters}")
    gok = input("Gok is even een letter ")
    if gok.lower() == "stop":
        doorgaan = False
    gevonden = 0
    for i in range(len(Correct_word)):

        if gok.lower() == Correct_word[i].lower():
            verborgen = verborgen[0:i] + Correct_word[i] + verborgen[i + 1:]
            gevonden += 1
    if gevonden > 0:
        print("Je hebt een goed lettertje gegokt")
    elif gok.lower() in gegokte_letters:
        print("Je hebt deze letter al gegokt")
    else:
        print("Slechte gok die staat er niet in")
        levens -= 1
    gegokte_letters.add(gok.lower())

while verborgen != Correct_word and levens != 0 and doorgaan:
    guess(verborgen, Correct_word)
if not doorgaan:
    print("\nOke we zijn gestopt")
elif levens > 0:
    print(f"\nGefeliciteerd je bent gewonnen het woord was {Correct_word}")
else:
    print("\nJe bent dood!!!!!!!")