import math
import collections

def solution(answers):
    
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    
    e =  {'1':0,'2':0,'3':0}

    
    leng = len(answers)
    
    first = first * (round(leng/len(first))+1)
    second = second * (round(leng/len(second))+1)
    third = third * (round(leng/len(third))+1)
    
    ziplist = list(zip(first, second, third))
    
    for index, answer in enumerate(answers):
        i,j,k = ziplist[index]
        
        if i == answer:
            e['1'] +=1
        if j == answer:
            e['2'] += 1
        if k == answer:
            e['3'] += 1
    
    sorted_e = sorted(e.items(), key=lambda kv: kv[1],reverse = True)
    
    answers = []
    
    for t in orted_e:
        i,j = t
        
        if not answers:
            answers.append(i)
        elif e[answers[-1]] != j:
            break
        else:
            answers.append(i)
    
    answers = [int(i) for i in answers]
    
    return answerss
