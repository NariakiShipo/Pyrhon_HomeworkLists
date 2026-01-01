def id_check(id_str):
    if len(id_str) != 10 or not id_str[0].isalpha() or not id_str[0].isupper():
        return 'wrong area code'
    if id_str[1] not in '12':
        return 'wrong gender code'
    # 區域碼轉數字
    area_num = ord(id_str[0]) - ord('A') + 10
    area_digits = [area_num // 10, area_num % 10]
    nums = area_digits + [int(x) for x in id_str[1:]]
    weights = [1,9,8,7,6,5,4,3,2,1]
    total = sum(nums[i]*weights[i] for i in range(10))
    remainder = total % 10
    check_code = 0 if remainder == 0 else 10 - remainder
    if check_code != nums[10]:
        return 'illegal'
    return 'pass'

def password_strength(pw):
    lower = sum(c.islower() for c in pw)
    upper = sum(c.isupper() for c in pw)
    digit = sum(c.isdigit() for c in pw)
    special = sum(c in '~!@#$%^&*<>_+=' for c in pw)
    score = lower + 3*upper + 2*digit + 5*special
    # 5個以上數字且不相鄰
    if digit >= 5:
        digit_pos = [i for i, c in enumerate(pw) if c.isdigit()]
        if all(abs(digit_pos[i]-digit_pos[j])>1 for i in range(len(digit_pos)) for j in range(i+1,len(digit_pos))):
            score += 15
    return score

def parse_time(s):
    from datetime import datetime
    return datetime.strptime(s, '%Y/%m/%d %H:%M')

def time_diff_minute(t1, t2):
    return int((t2-t1).total_seconds()//60)

def main():
    limit = int(input())
    n = int(input())
    users = {}
    for _ in range(n):
        now = parse_time(input().strip())
        # 帳號合法檢查
        while True:
            uid = input().strip()
            res = id_check(uid)
            print(res)
            if res == 'pass':
                break
        # 密碼強度檢查
        while True:
            pw = input().strip()
            if password_strength(pw) < 30:
                print('not strong enough')
            else:
                print('ok good password')
                break
        # 新用戶
        if uid not in users:
            users[uid] = {'pw': pw, 'pw_hist': [pw], 'last': now}
            print('new')
            continue
        # 舊用戶
        while True:
            if pw != users[uid]['pw']:
                print('wrong')
                while True:
                    pw = input().strip()
                    if password_strength(pw) < 30:
                        print('not strong enough')
                    else:
                        print('ok good password')
                        break
            else:
                print('correct')
                break
        # 判斷是否需變更密碼
        diff = time_diff_minute(users[uid]['last'], now)
        if diff < limit:
            print('no need to change')
            continue
        else:
            print('need to change')
            while True:
                newpw = input().strip()
                if password_strength(newpw) < 30:
                    print('not strong enough')
                    continue
                else:
                    print('ok good password')
                if newpw in users[uid]['pw_hist'][-3:]:
                    print('same password')
                    continue
                users[uid]['pw'] = newpw
                users[uid]['pw_hist'].append(newpw)
                users[uid]['last'] = now
                print('password changed')
                break

if __name__ == '__main__':
    main()
