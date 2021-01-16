def solution(n):
    answer = ""
    
    while(True):
        i,j = divmod(n,3)
        if i == 0:
            answer += (str(j))
            break
        else:
            n = i
            answer += (str(j))
            
    answer = int(answer,3)
    return answer