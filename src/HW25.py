cardColors = ['S', 'H', 'D', 'C']
cardRanks = {'J': 11, 'Q': 12, 'K': 13, 'A': 1}
cardTypeNumber = {"High Card": 1, "One Pair": 2, "Two Pairs": 3, "Three of a Kind": 4,"Straight": 5, "Flush": 6 , "Full House": 7, "Four of a Kind": 8, "Straight Flush": 9}
# Get card rank
def get_card_rank(card: str):
    if card[0:2].isdigit():
        return int(card[0:2])
    else:
        for item in cardRanks:
            if item == card[:1]:
                return cardRanks[item]
        if card[:1] not in cardRanks:
            print("Error input")
            exit()
    return int(card[:1])

# Get card color
def get_card_color(card: str):
    if len(card) == 3:
        if card[0:2].isdigit()== False:
            print("Error input")
            exit()
        else:
            if card[2:] not in cardColors:
                print("Error input")
                exit()
        return card[2:]
        
    else: 
        if card[1:] not in cardColors:
            print("Error input")
            exit()
    return card[1:]

# Check duplicate cards
def check_duplicate(cards: list) -> bool:
    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            if cards[i] == cards[j]:
                return True
    return False

# need to refactor
# Check pair 
def check_pair(cards: list) -> str:
    repeated = 0
    pairs = 0
    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            if get_card_rank(cards[i]) == get_card_rank(cards[j]):
                repeated += 1
        
        if repeated == 3:
            return "Three of a Kind"
        elif repeated >= 2:
            pairs = repeated // 2
            repeated = 0
    if pairs == 1:
        return "One Pair"
    elif pairs == 2:
        return "Two Pairs"
    else:
        return "High Card"

def check_kinds(cards: list) -> str:
    repeated = 0
    repeated_list = []
    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            if get_card_rank(cards[i]) == get_card_rank(cards[j]):
                repeated += 1
                repeated_list.append(j)
        if repeated >= 2:
            repeated_list.append(i)
        if repeated == 3:
            return "Four of a Kind"
        elif repeated == 2:
            return "Three of a Kind"
    return ""
# Check card type
def check_card_type(cards: list) -> int:
    card_colors = [get_card_color(card) for card in cards]
    cards_ranks = [get_card_rank(card) for card in cards]
    print(card_colors)
    print(cards_ranks)
    return 0
def main():
    cards = input().split()
    card_colors = [get_card_color(card) for card in cards]
    cards_ranks = [get_card_rank(card) for card in cards]
    cards_ranks.sort()
    print(card_colors)
    print(cards_ranks)
    if check_duplicate(cards):
        print("Duplicate deal")
        return
    else:
        pass
        #check_card_type(cards)
    
main()