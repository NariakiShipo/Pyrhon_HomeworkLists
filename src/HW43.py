

# 密碼合法字元
def get_valid_chars():
	return set('ABCDabcd0123456789@#$!_')
def get_special_chars():
	return set('@#$!_')
def get_upper_chars():
	return set('ABCD')

def is_valid_password(pw, valid_chars, special_chars, upper_chars):
	if not (3 <= len(pw) <= 5):
		return False
	if any(c not in valid_chars for c in pw):
		return False
	if len(set(pw)) != len(pw):
		return False
	if not any(c in special_chars for c in pw):
		return False
	if not any(c in upper_chars for c in pw):
		return False
	return True

def compare_passwords(pw1, pw2):
	A = sum(a == b for a, b in zip(pw1, pw2))
	used1 = [False] * len(pw1)
	used2 = [False] * len(pw2)
	# 先標記A
	for i in range(len(pw1)):
		if pw1[i] == pw2[i]:
			used1[i] = True
			used2[i] = True
	B = 0
	for i in range(len(pw1)):
		if used1[i]:
			continue
		for j in range(len(pw2)):
			if not used2[j] and pw1[i] == pw2[j] and i != j:
				used2[j] = True
				B += 1
				break
	return f"{A}A{B}B"

# 用遞迴產生所有長度 length 的不重複密碼
def all_possible_passwords(length, chars, exclude_chars=None):
	result = []
	if exclude_chars:
		chars = ''.join([c for c in chars if c not in exclude_chars])
	def dfs(path, used):
		if len(path) == length:
			result.append(''.join(path))
			return
		for i in range(len(chars)):
			if not used[i]:
				path.append(chars[i])
				used[i] = True
				dfs(path, used)
				path.pop()
				used[i] = False
	dfs([], [False]*len(chars))
	return result

def filter_passwords(candidates, guesses, valid_chars, special_chars, upper_chars):
	res = []
	for pw in candidates:
		if not is_valid_password(pw, valid_chars, special_chars, upper_chars):
			continue
		ok = True
		for guess, result in guesses:
			if compare_passwords(guess, pw) != result:
				ok = False
				break
		if ok:
			res.append(pw)
	return res



def main():
	valid_chars = get_valid_chars()
	special_chars = get_special_chars()
	upper_chars = get_upper_chars()
	chars = 'ABCDabcd0123456789@#$!_'
	mode = input().strip()
	n = int(input().strip())
	lines = []
	for _ in range(n):
		lines.append(input().strip())
	if mode == 'T':
		out = ''
		for pw in lines:
			out += 'T' if is_valid_password(pw, valid_chars, special_chars, upper_chars) else 'F'
		print(out)
	elif mode == 'S':
		for line in lines:
			pw1, pw2 = line.split()
			print(compare_passwords(pw1, pw2))
	elif mode == 'G':
		guess_dict = {}
		for line in lines:
			pw, result = line.split()
			l = len(pw)
			if l not in guess_dict:
				guess_dict[l] = []
			guess_dict[l].append((pw, result))
		for l in sorted(guess_dict.keys()):
			# 先根據 0A0B 規則排除字元
			exclude = set()
			for pw, res in guess_dict[l]:
				if res == '0A0B':
					exclude.update(pw)
			candidates = all_possible_passwords(l, chars, exclude)
			filtered = filter_passwords(candidates, guess_dict[l], valid_chars, special_chars, upper_chars)
			filtered.sort(key=lambda x: (len(x), [chars.index(c) for c in x]))
			print(' '.join(filtered))

if __name__ == '__main__':
	main()
