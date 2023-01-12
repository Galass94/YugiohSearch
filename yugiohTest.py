import yugioh
import os
from requests import get
import textwrap

def listHits(count, cardList):
    if count >= len(cardList):
        return 0
    else: 
        print(f"{count+1}: {cardList[count]}")
        listHits(count+1, cardList)
def listDetails(index, cardList):
    card = yugioh.get_card(card_name=cardList[index-1])
    cardSets = get(f"https://db.ygoprodeck.com/api/v7/cardinfo.php?name={card.name}".replace(" & ", "&").replace(" ", "%20")).json()["data"][0]["card_sets"]
    print(f""" {card.name}
 -------------------------------------------""")
    print("",textwrap.fill(card.description, 120).replace("\n", "\n ").replace("●", "\n ●"))
    print(""" -------------------------------------------""")
    if "Monster" in card.type:
        print(f""" Type: {card.type}
 -------------------------------------------
 ATK: {card.attack} / DEF: {card.defense}""")
    elif "Spell" in card.type:
        print(f""" Type: {card.type}""")
    print(f""" From {card.cardmarket_price}€ on CardMarket
 From {card.tcgplayer_price}€ on TCGPlayer""")
    count=1
    for set in cardSets:
        print(f" Set {count}: {set['set_name']}: {set['set_rarity']}")
        count+=1
    print()

while True:
    os.system("cls")
    cardSearch = input("Enter a card name you're looking for: ")
    cardList = yugioh.get_cards_by_name(cardSearch).list
    listHits(0, cardList)
    index = int(input("Choose a card from above list and enter the index for more information: "))
    os.system("cls")
    listDetails(index, cardList)
    while True:
        try:
            choice = input("Do you want to search for another card? (Y/N) -> ").lower()
            if choice == 'n':
                break
            elif choice == 'y':
                break
            else:
                raise ValueError
        except ValueError as e:
            print("Please enter only \'y\' or \'n\'")
            os.system("pause")
        if choice == 'n':
            break
    if choice=='n':
        break
