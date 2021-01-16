import math
import itertools

def isPrimeNumber(n):

    try:
        if n <= 0:
            raise Exception

        elif n == 1:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        else:
            root = math.sqrt(n)
            root = round(root)

            for i in range(3, root+1, 2):
                if n % i == 0:
                    return False

        return True
    except Exception as e:
        print("not positive", e)
        return False


def solution(numbers):
    answer = 0
    finalresult = []
    
    for index in range(1,len(numbers)+1):

        result_list = list(numbers)
        
        result_list = list(map(''.join, itertools.permutations(result_list,index)))
        

        result_list = [int(i) for i in result_list]
        result_list = set(result_list)



        finalresult.extend(result_list)


    finalresult = set(finalresult)
    
    for num in finalresult:
        if isPrimeNumber(num):
            answer +=1

    return answer


print(solution("17"))
print(solution("011"))