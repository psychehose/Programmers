def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()

    r = zip(participant,completion)
    print(list(r))
    
    for i,j in r:
        if i != j:
            return i


    return participant[-1]
    
    
    
    


par = ['leo', 'kiki', 'eden']
com = ['eden', 'kiki']

print(solution(participant=par,completion=com))

