def solution(array, commands):
    answer = []

    for command in commands:
        answer.append(cut_sort_indexk(array,command))

    return answer



def cut_sort_indexk(array,c):
    return (sorted(array[c[0]-1 : c[1]]))[c[2]-1]