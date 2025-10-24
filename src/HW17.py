from collections import Counter

# 步驟 0: 定義常量和輔助字典
HCP_MAP = {'A': 4, 'K': 3, 'Q': 2, 'J': 1}
SUIT_NAMES = {'S': 'Spade', 'H': 'Heart', 'D': 'Diamond', 'C': 'Club'}
# 花色等級: Spade(4) > Heart(3) > Diamond(2) > Club(1)
SUIT_RANK = {'S': 4, 'H': 3, 'D': 2, 'C': 1}

# 讀取輸入
try:
    # 讀取花色
    suits = input().split()
    # 讀取牌面
    ranks = input().split()
except EOFError:
    # 處理可能的輸入結束
    suits = []
    ranks = []

# 組合牌
cards = list(zip(suits, ranks))
# 假設輸入總是 5 張牌

# --- 步驟 1: 計算大牌點 (HCP) ---
# 使用列表推導式和 sum 進行計算
hcp = sum(HCP_MAP.get(rank, 0) for rank in ranks)


# --- 步驟 2 & 3: 計算花色張數 (Distribution)、牌長點 (Length Points) 和總點力 ---

# 計算花色分佈
suit_counts = Counter(suits)

s_count = suit_counts['S']
h_count = suit_counts['H']
d_count = suit_counts['D']
c_count = suit_counts['C']

# 牌長點: 某個花色有 5 張牌則加 2 分
# 由於總共只有 5 張牌，如果某個花色是 5 張，其他花色肯定是 0 張
length_points = 2 if (s_count == 5 or h_count == 5 or d_count == 5 or c_count == 5) else 0

total_points = hcp + length_points


# --- 步驟 4: 擋張分析 (Stopper Analysis) ---

# 統計每個花色中 A, K, Q 的數量
# 牌力統計: (花色, 牌面) -> 數量
power_card_counts = Counter(card for card in cards if card[1] in HCP_MAP)

# 判斷每個花色是否有擋張的輔助函數 (雖然在主體外，但用於避免在判斷時使用 loop)
def has_stopper(suit, count, power_counts):
    """根據規則判斷單一花色是否有擋張。"""
    # 規則:
    # 1. 擁有 A
    has_A = power_counts[(suit, 'A')] > 0
    # 2. 擁有 K，且該花色總張數 > 1
    has_K_and_2plus = power_counts[(suit, 'K')] > 0 and count > 1
    # 3. 擁有 Q，且該花色總張數 > 2
    has_Q_and_3plus = power_counts[(suit, 'Q')] > 0 and count > 2
    
    return has_A or has_K_and_2plus or has_Q_and_3plus

# 由於只有 4 個花色，我們直接判斷
is_s_stopped = has_stopper('S', s_count, power_card_counts)
is_h_stopped = has_stopper('H', h_count, power_card_counts)
is_d_stopped = has_stopper('D', d_count, power_card_counts)
is_c_stopped = has_stopper('C', c_count, power_card_counts)

# 建立擋張花色列表 (按 S, H, D, C 順序)
stopped_suits_list = []
if is_s_stopped:
    stopped_suits_list.append('S')
if is_h_stopped:
    stopped_suits_list.append('H')
if is_d_stopped:
    stopped_suits_list.append('D')
if is_c_stopped:
    stopped_suits_list.append('C')


# --- 步驟 5: 建議行動 (Opening Bid) ---

opening_bid = ""
if total_points < 8:
    opening_bid = "Pass"
elif total_points >= 15:
    opening_bid = "Strong Open"
else:  # 8 <= Total Points <= 14
    
    # 找出最長花色及其張數
    # 由於只有四個花色，我們直接比較，避免使用 max(suit_counts.items())
    
    # 找出最大張數
    max_count = max(s_count, h_count, d_count, c_count)
    
    # 找出所有最長花色
    longest_suits = []
    if s_count == max_count:
        longest_suits.append('S')
    if h_count == max_count:
        longest_suits.append('H')
    if d_count == max_count:
        longest_suits.append('D')
    if c_count == max_count:
        longest_suits.append('C')

    # 找出等級最高的花色
    best_suit = ''
    highest_rank = -1
    
    # 由於只有 4 個可能的花色，我們直接檢查順序
    # S > H > D > C
    if 'S' in longest_suits:
        best_suit = 'S'
    elif 'H' in longest_suits:
        best_suit = 'H'
    elif 'D' in longest_suits:
        best_suit = 'D'
    elif 'C' in longest_suits:
        best_suit = 'C'

    if best_suit:
        opening_bid = f"Open {SUIT_NAMES[best_suit]}"
    else:
        # 理論上不會發生，因為 max_count 至少為 5/4=1
        opening_bid = "Pass" # 錯誤處理


# --- 輸出結果 ---
print(f"HCP: {hcp}")
print(f"Total Points: {total_points}")
print(f"Distribution (S-H-D-C): {s_count}-{h_count}-{d_count}-{c_count}")
print(f"Stopped Suits: {stopped_suits_list}")
print(f"Opening Bid: {opening_bid}")