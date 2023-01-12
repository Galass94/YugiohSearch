import requests
import yugioh
import os
import textwrap


def list_hits(count, card_list):
    if count >= len(card_list):
        return 0
    for i, card in enumerate(card_list, 1):
        print(f"{i}: {card}")


def get_card_sets(card_name):
    url = f"https://db.ygoprodeck.com/api/v7/cardinfo.php?name={'%20'.join(card_name.split())}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['data'][0]['card_sets']


def list_details(index, card_list):
    card = yugioh.get_card(card_name=card_list[index - 1])
    card_sets = get_card_sets(card.name)
    separator = '-' * 40
    print(f"{card.name}\n{separator}")
    print(textwrap.fill(card.description, 120).replace("\n", "\n ").replace("●", "\n ●"))
    print(separator)
    if "Monster" in card.type:
        print(f"Type: {card.type}\n{separator}\nATK: {card.attack} / DEF: {card.defense}")
    elif "Spell" in card.type:
        print(f"Type: {card.type}")
    print(f"From {card.cardmarket_price}€ on CardMarket\nFrom {card.tcgplayer_price}€ on TCGPlayer")
    for i, card_set in enumerate(card_sets, 1):
        print(f"Set {i}: {card_set['set_name']}: {card_set['set_rarity']}")
    print()


def main():
    while True:
        os.system("cls")
        card_search = input("Enter a card name you're looking for: ")
        card_list = yugioh.get_cards_by_name(card_search).list
        list_hits(0, card_list)
        index = int(input("Choose a card from above list and enter the index for more information: "))
        os.system("cls")
        list_details(index, card_list)
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


if __name__ == '__main__':
    main()
