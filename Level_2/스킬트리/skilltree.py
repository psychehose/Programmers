def solution(skill, skill_trees):
    answer = 0
    result_list = []


    for index in range(len(skill_trees)):
        bp = 0

        result_list = [i for i in skill_trees[index] for j in skill if j == i]

        for i,j in enumerate(result_list) :
            if j != skill[i]:
                bp = 1
                break

        if bp == 0:
            answer +=1
        
        

    return answer




print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))