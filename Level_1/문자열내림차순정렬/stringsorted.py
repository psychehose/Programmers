def solution(s):
    answer = []
    answer = list(s)
    
    answer.sort(reverse = True)
    answer = ''.join(answer)
    return answer
