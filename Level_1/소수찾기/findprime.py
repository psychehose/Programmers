import math
def solution(n):
    answer = 0

    l = list(range(3,n+1,2))

    for i in l:

        for j in list(range(3,(round(math.sqrt(i))+1),2)):
            if i%j == 0:
                break

        else:
            answer += 1



    return answer + 1
