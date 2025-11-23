
def awfFunc(prompt: list, content: list):
    i = int(prompt[1])
    n = int(prompt[2])
    content[i - 1].insert(n - 1, prompt[3])
    return content

def awaFunc(prompt: list, content:list):
    i = int(prompt[1])
    n = int(prompt[2])
    content[i - 1].insert(n, prompt[3])
    return content

def asfFunc(prompt: list, content: list):
    i = int(prompt[1])
    sentence = prompt[2:]
    
    content[i - 1] = sentence + content[i - 1]
    return content

def asaFunc(prompt: list, content: list):
    i = int(prompt[1])
    sentence = prompt[2:]
    
    for s in sentence:
        content[i - 1].append(s)
    return content

def ifKeyWord(prompt: list, content: list):
    key = prompt[1]
    word = prompt[2]
    for i in range(len(content)):
        for j in range(len(content[i]) -1 , -1, -1):
            if content[i][j] == key:
                content[i].insert(j,word)
                
    return content

def iaKeyWord(prompt: list, content: list):
    key = prompt[1]
    word = prompt[2]
    for i in range(len(content)):
        for j in range(len(content[i]) - 1, -1, -1):
            if content[i][j] == key:
                content[i].insert(j + 1,word)
                
    return content

def dwFunc(prompt: list,content: list):
    delLine = int(prompt[1])
    delWord = int(prompt[2])
    content[delLine - 1].pop(delWord - 1)
    
    if not content[delLine - 1]:
        content.pop(delLine - 1)
        
    return content

def dlFunc(prompt: list,content: list):
    delLine = int(prompt[1])
    content.pop(delLine - 1)
    return content

def rpFunc(prompt :list, content: list):
    beReplaceWord = prompt[1]
    replaceWord = prompt[2]
    for i in range(len(content)):
       for j in range(len(content[i])):
            if content[i][j] == beReplaceWord:
                content[i][j] = replaceWord
    return content

def cFunc(content: list):
    summary = 0
    for i in range(len(content)):
        num = len(content[i])
        summary += num
    print(summary)

def main():
    text= input().split()
    m = int(text[0])
    n = int(text[1])
    content = list()
    for _ in range(m):
        t = input().split()
        content.append(t)

    for _ in range(n):
        prompt = input().split()
        if prompt[0] == "awf":
            content = awfFunc(prompt, content)
        elif prompt[0] == "awa":
            content = awaFunc(prompt, content)
        elif prompt[0] == "asf":
            content = asfFunc(prompt, content)
        elif prompt[0] == "asa":
            content = asaFunc(prompt, content)
        elif prompt[0] == "if":
            content = ifKeyWord(prompt, content)
        elif prompt[0] == "ia":
            content = iaKeyWord(prompt, content)
        elif prompt[0] == "dw":
            content = dwFunc(prompt, content)
        elif prompt[0] == "dl":
            content = dlFunc(prompt, content)
        elif prompt[0] == "rp":
            content = rpFunc(prompt, content)
        elif prompt[0] == "c":
            cFunc(content)

    for line in content:
        if line:
            print(" ".join(line))
    
    
if __name__ == "__main__" :
    main()