
name =input()
id = input()
score_chinese = int(input())
score_progranm_theory = int(input())    
score_progranming = int(input())

print("Name:{}".format(name))
print("Id:{}".format(id))
print("Total:{}".format(score_chinese + score_progranm_theory + score_progranming))
print("Average:{}".format((score_chinese + score_progranm_theory + score_progranming)//3))
