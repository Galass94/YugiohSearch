import yugioh
import os
from requests import get
import textwrap


def list_hits(count, card_list):
    if count >= len(card_list):
        return 0
    else:
        print(f"{count + 1}: {card_list[count]}")
        list_hits(count + 1, card_list)


def list_details(index, card_list):
    card = yugioh.get_card(card_name=card_list[index - 1])
    card_sets = get(f"https://db.ygoprodeck.com/api/v7/cardinfo.php?name={card.name}".replace(" & ", "&").replace(" ",
                                                                                                                  "%20")).json()[
        "data"][0]["card_sets"]
    print(f""" {card.name}
 -------------------------------------------""")
    print("", textwrap.fill(card.description, 120).replace("\n", "\n ").replace("●", "\n ●"))
    print(""" -------------------------------------------""")
    if "Monster" in card.type:
        print(f""" Type: {card.type}
 -------------------------------------------
 ATK: {card.attack} / DEF: {card.defense}""")
    elif "Spell" in card.type:
        print(f""" Type: {card.type}""")
    print(f""" From {card.cardmarket_price}€ on CardMarket
 From {card.tcgplayer_price}€ on TCGPlayer""")
    count = 1
    for set in card_sets:
        print(f" Set {count}: {set['set_name']}: {set['set_rarity']}")
        count += 1
    print()


if __name__ == '__main__':
    while True:
        os.system("cls")
        cardSearch = input("Enter a card name you're looking for: ")
        cardList = yugioh.get_cards_by_name(cardSearch).list
        list_hits(0, cardList)
        index = int(input("Choose a card from above list and enter the index for more information: "))
        os.system("cls")
        list_details(index, cardList)
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
        if choice == 'n':
            break
