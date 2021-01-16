def solution(n, lost, reserve):
    answer = 0
    
    answer = n - len(lost)
    intersection = set(lost) & set(reserve)
    answer += len(intersection)
    lost = list(set(lost) - intersection)
    reserve = list(set(reserve) - intersection)

    for l in lost:
        if l - 1 in reserve:
            answer +=1
            reserve.remove(l-1)
            
        elif l+1 in reserve:
            answer +=1
            reserve.remove(l+1)
    
    
    
    return answer
