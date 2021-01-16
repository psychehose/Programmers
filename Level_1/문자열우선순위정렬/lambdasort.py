def solution(strings, n):
    
    answer = []
    result = []
    
    strings.sort()
    answer = sorted(strings, key = lambda x: x[n])    
    
        
    return answer