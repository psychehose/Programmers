
def solution(a, b):
    answer = ''
    day = {
        1:"FRI",
        2:"SAT",
        3:"SUN",
        4:"MON",
        5:"TUE",
        6:"WED",
        0:"THU"
    }
    num = 0
    
    months = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    for i in range(a-1):
        num += months[i]
        
    num += b
    
    return day[num%7]