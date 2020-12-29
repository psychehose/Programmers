import math


def solution(numbers, hand):

    answer = ''
    defalut = ''
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['l_start', 0, 'r_start']]
    lhand = [(3, 0)]
    rhand = [(3, 2)]

    for number in numbers:
        if number in [1, 4, 7]:

            lhand = [(i, j) for i in range(4)
                     for j in range(3) if keypad[i][j] == number]
            answer += 'L'

        elif number in [3, 6, 9]:
            rhand = [(i, j) for i in range(4)
                     for j in range(3) if keypad[i][j] == number]

            answer += 'R'

        else:
            target = [(i, j) for i in range(4)
                      for j in range(3) if keypad[i][j] == number]

            ltarget = tupSum(lhand[0], target[0])
            rtarget = tupSum(rhand[0], target[0])

            print(ltarget[0], ltarget[1], rtarget[0], rtarget[1])

            if abs(ltarget[0])+abs(ltarget[1]) > abs(rtarget[0])+abs(rtarget[1]):

                # (ltarget[0] * ltarget[0]) + (ltarget[1] * ltarget[1]) > (rtarget[0] * rtarget[0]) + (rtarget[1] * rtarget[1]):

                rhand = target
                answer += 'R'

            elif abs(ltarget[0])+abs(ltarget[1]) < abs(rtarget[0])+abs(rtarget[1]):

                # (ltarget[0] * ltarget[0]) + (ltarget[1] * ltarget[1]) < (rtarget[0] * rtarget[0]) + (rtarget[1] * rtarget[1]):
                lhand = target
                answer += 'L'
            else:
                if hand == 'right':
                    rhand = target
                    answer += 'R'

                elif hand == 'left':
                    lhand = target
                    answer += 'L'

    return answer


def tupSum(tupA, tupB):
    return tuple(sum(a - b) for a, b in zip(tupA, tupB))


def tupMul(tupA):
    return tuple(-1*elem for elem in tupA)


print(solution(numbers=[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], hand='left'))

# 지호 코드

# def solution(numbers, hand):

#     keypad = [[-1,7,4,1],[0,8,5,2],[-1,9,6,3]]

#     left = [0,0] # 시작 위치
#     right = [2,0] # 시작 위치
#     answer = ''
#     for n in numbers:
#         if n in keypad[0]:
#             answer += 'L'
#             left = [0,keypad[0].index(n)] # [0, n의 인덱스]
#         elif n in keypad[2]:
#             answer += 'R'
#             right = [2,keypad[2].index(n)] # [0, n의 인덱스]
#         else:
#             x = 1
#             y = keypad[1].index(n)
#             left_distance = abs(x-left[0]) + abs(y - left[1])
#             right_distance = abs(x - right[0]) + abs(y - right[1])
#             if left_distance < right_distance:
#                 answer += 'L'
#                 left = [1,y]
#             elif left_distance > right_distance:
#                 answer += 'R'
#                 right = [1,y]
#             else:
#                 if hand == 'right':
#                     answer += 'R'
