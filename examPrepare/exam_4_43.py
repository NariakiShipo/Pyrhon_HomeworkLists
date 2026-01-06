def get_valid_chars():
    return set('ABCDabcd0123456789@#$!_')
def get_special_chars():
    return set('@#$!_')
def get_upper_chars():
    return set('ABCD')

def is_valid(pw,valid_chars,special_chars,upper_chars):
    if not (3<=len(pw)<=5):
        return False
    if any(c not in valid_chars for c in pw):
        return False
    if not any(c in valid_chars for c in pw):
        return False
    if len(set(pw)) != len(pw):
        return False
    if not any(c in special_chars for c in pw):
        return False
    return True

def main():
    valid_chars = get_valid_chars()
    special_chars = get_special_chars()
    upper_chars = get_upper_chars()
    mode = input().strip()
    count = int(input().strip())
    for i in range(count):
        pw = input().strip()
        if mode == 'T':
            result = ""
            result += 'T' if is_valid(pw, valid_chars, special_chars, upper_chars) else 'F'

      
if __name__ == "__main__":
    main()