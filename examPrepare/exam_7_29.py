def process_awf(article:list, change_column, change_place , new_word):
    article[change_column - 1].insert(change_place -1 , new_word)
    

def process_awa(article:list, change_column, change_place , new_word):
    article[change_column - 1].insert(change_place , new_word)

def process_asf(article:list, change_column, new_sentence):
    article[change_column - 1] = new_sentence + article[change_column - 1]

def process_asa(article:list, change_column, new_sentence):
     article[change_column - 1] = article[change_column - 1] + new_sentence

def process_if(article, key_word, new_word):
    for i in range(len(article)):
        indices = [idx for idx, word in enumerate(article[i]) if word == key_word]
        #倒敘插入避免index錯亂
        for index in reversed(indices):
            article[i].insert(index, new_word)
    #    for j in range(len(article[i]) - 1, -1 ,-1):
    #         if article[i][j] == key_word:
    #             article.insert(j, new_word)

def process_ia(article, key_word, new_word):
    for i in range(len(article)):
        indices = [idx for idx, word in enumerate(article[i]) if word == key_word]
        #倒敘插入避免index錯亂
        for index in reversed(indices):
            article[i].insert(index + 1, new_word)
        #  for j in range(len(article[i]) - 1, -1 ,-1):
        #      if article[i][j] == key_word:
        #         article.insert(j + 1, new_word)

def process_dw(article:list, change_column, del_word_num):
    article[change_column - 1].pop(del_word_num -1)

def process_dl(article, del_sentence_num):
    article.pop(del_sentence_num - 1)

def process_rp(article:list, be_replaced_word, replace_word):
    for i in range(len(article)):
        if be_replaced_word in article[i]:
            index = article[i].index(be_replaced_word)
            article[i][index] = replace_word


def process_c(article):
    counts = 0
    for i in article:
        counts += len(i)
    print(counts)

def main():
    #使用巢狀字典去減少多個if判斷
    command_codes = { 
        "awf" : process_awf,
        "awa" : process_awa,
        "asf" : process_asf,
        "asa" : process_asa,
        "if"  : process_if,
        "ia"  : process_ia,
        "dw"  : process_dw,
        "dl"  : process_dl,
        "rp"  : process_rp,
        "c"   : process_c,
                    }
    article_counts, command_counts = [int(m) for m in input().split()]
    article =list()
    for _ in range (article_counts):
        article.append([m for m in input().split()])
    for _ in range(command_counts):
        command = [m for m in input().split()]
        code = command[0]
        command_args = []
        if code == "asa" or code == "asf":  #asa asf因為要轉換成句子 因此需要特別判斷
            command_args = [int(command[1]) , command[2:]]
        else: command_args = command[1:]
        # 轉換參數類型：索引和數字轉為 int，其他保持為 str
        converted_args = []
        if code != "asa" and code != "asf": 
            for arg in command_args:
                try:
                    converted_args.append(int(arg))
                except ValueError:
                    converted_args.append(arg)
            command_args = converted_args
        command_codes[code](article, *command_args) #根據每個函式需要的參數量動態傳入變數
    #print(article)
    for sentence in article:
        for word in sentence:
            print(word, end=" ")
        print() 
if __name__ == "__main__":
    main()