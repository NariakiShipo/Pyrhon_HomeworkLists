# 將牌面轉換為點數
def card_to_point(card):
    if card == 'A':
        return 1.0
    elif card in ['J', 'Q', 'K']:
        return 0.5
    else:
        return float(card)

# 主程式
player_num = int(input())
bets = list(map(int, input().split()))
first_cards = input().split()

# 初始化莊家和玩家的手牌
computer_hand = [card_to_point(first_cards[0])]
players_hands = [[card_to_point(first_cards[i+1])] for i in range(player_num)]

# 玩家狀態：None=進行中, 'bust'=爆掉, 'win'=10.5, 'stop'=停牌
players_status = [None] * player_num  # type: ignore
players_total = [sum(players_hands[i]) for i in range(player_num)]

# 玩家要牌階段
for i in range(player_num):
    while players_status[i] is None:
        action = input().split()
        
        if action[0] == 'N':
            players_status[i] = 'stop'
            break
        
        if action[0] == 'Y':
            card = card_to_point(action[1])
            players_hands[i].append(card)
            players_total[i] = sum(players_hands[i])
            
            if players_total[i] > 10.5:
                players_status[i] = 'bust'
            elif abs(players_total[i] - 10.5) < 0.001:
                players_status[i] = 'win'

# 檢查是否所有玩家都已有結果（爆掉或10.5）
all_finished = all(status in ['bust', 'win'] for status in players_status)

# 莊家要牌階段
computer_total = sum(computer_hand)
if not all_finished:
    # 找出未爆掉玩家的最小點數
    active_players_totals = [players_total[i] for i in range(player_num) 
                             if players_status[i] not in ['bust']]
    
    if active_players_totals:
        min_active_total = min(active_players_totals)
        
        while computer_total <= min_active_total:
            card = card_to_point(input())
            computer_hand.append(card)
            computer_total = sum(computer_hand)
            
            if abs(computer_total - 10.5) < 0.001 or computer_total > 10.5:
                break

# 計算賺賠
computer_profit = 0
players_profit = [0] * player_num

for i in range(player_num):
    if players_status[i] == 'bust':
        # 玩家爆掉，玩家立賠
        players_profit[i] = -bets[i]
        computer_profit += bets[i]
    elif players_status[i] == 'win':
        # 玩家10.5，電腦立賠
        players_profit[i] = bets[i]
        computer_profit -= bets[i]
    else:
        # 比較點數
        if computer_total > 10.5:
            # 電腦爆掉，電腦立賠
            players_profit[i] = bets[i]
            computer_profit -= bets[i]
        elif abs(computer_total - 10.5) < 0.001:
            # 電腦10.5，玩家立賠
            players_profit[i] = -bets[i]
            computer_profit += bets[i]
        elif computer_total >= players_total[i]:
            # 電腦點數大於等於玩家，玩家賠
            players_profit[i] = -bets[i]
            computer_profit += bets[i]
        else:
            # 玩家點數大於電腦，電腦賠
            players_profit[i] = bets[i]
            computer_profit -= bets[i]

# 輸出結果
for i in range(player_num):
    if players_profit[i] >= 0:
        print(f"Player{i+1} +{players_profit[i]}")
    else:
        print(f"Player{i+1} {players_profit[i]}")

if computer_profit >= 0:
    print(f"Computer +{computer_profit}")
else:
    print(f"Computer {computer_profit}")