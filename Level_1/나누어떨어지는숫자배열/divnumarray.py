def solution(arr, divisor):
    answer = []
    answer = [element for element in arr if element%divisor == 0]
    if not answer:
        answer.append(-1)
    answer.sort()
    return answer


