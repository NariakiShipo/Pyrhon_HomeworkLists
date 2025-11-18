def get_card_rank(card: str):
    if card == "Joker":
        return "Joker"
    return card[1:]

def organize_hand(hand: list)-> list:
    num = [get_card_rank(card) for card in hand]
    repeatcard = set()
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if i not in repeatcard and j not in repeatcard:
                if num[i] == num[j]:
                    repeatcard.add(i)
                    repeatcard.add(j)
    repeatcard = sorted(repeatcard, reverse=True)
    for index in repeatcard:
        hand.pop(index)
    return hand
def draw_card(pickPlayer: list, bePickPlayer: list, card: str):
    pickPlayer.append(card)
    if card in bePickPlayer:
        bePickPlayer.remove(card)
    else:
        print("Error")
        exit()
    return organize_hand(pickPlayer), organize_hand(bePickPlayer)

def print_hand(hand: list):
    for card in hand:
        print(card, end=' ')
    print()
def main():
    player_1 = input().split()
    player_2 = input().split()
    computer = input().split()

    player_1 = organize_hand(player_1)
    player_2 = organize_hand(player_2)
    computer = organize_hand(computer)

    draw_card_1 = input()
    draw_card_2 = input()
    draw_card_3 = input()

    player_1, player_2 = draw_card(player_1, player_2, draw_card_1)
    player_2, computer = draw_card(player_2, computer, draw_card_2)
    computer, player_1 = draw_card(computer, player_1, draw_card_3)
    print_hand(player_1)
    print_hand(player_2)
    print_hand(computer)
main()
