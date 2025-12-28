def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def matchPre(dna, pre, position):
    if position + len(pre) > len(dna):
        return False
    for i in range(len(pre)):
        if pre[i] != '?' and dna[position + i] != pre[i]:
            return False
    return True
def hasPre(dna, pre):
    for i in range(len(dna) - len(pre) + 1):
        if matchPre(dna, pre, i):
            return i
    return -1
def hasPost(dna, endList, startPosition):
    if startPosition > len(dna):
        return -1
    for end in endList:
        if dna[startPosition:startPosition+len(end)] == end:
            return startPosition
    return hasPost(dna, endList, startPosition + 1)

def isValidGene(gene):
    count = 0
    if not isPrime(len(gene)):
        return False
    for c in gene:
        if c in 'ATCG':
            count += 1
    if count == len(gene):
        return True
    return False

def findGene(dna, pre, endList, geneList):
    prePosition = hasPre(dna, pre)
    if prePosition == -1 :return
    endPosition = hasPost(dna, endList, prePosition + len(pre))
    if endPosition == -1: return
    if isValidGene(dna[prePosition + len(pre):endPosition]):
        geneList.append(dna[prePosition + len(pre):endPosition])
    findGene(dna[endPosition + 1 :], pre, endList, geneList)
  

def main():
    preGene = input()
    postGene = input().split()
    dnaList = input()
    geneList = list()
    findGene(dnaList, preGene, postGene, geneList)
    if geneList:
        geneList.sort(key=lambda x: (len(x), x))
        for g in geneList:
            print(g)
    else:
        print("No gene")
if __name__ == "__main__":
    main()