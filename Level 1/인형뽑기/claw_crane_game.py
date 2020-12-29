



def solution(board, moves):
    answer = 0
    board_stack = []

    moves = [i - 1 for i in moves]
    board_stack = list((zip(*board)))

    result_list = []

    # 리스트화
    board_stack_list = []
    for index in range(len(board_stack)):
        board_stack_list.append(list(board_stack[index]))

    for i in range(len(moves)):

        for j in range(len(board_stack_list[moves[i]])):

            if board_stack_list[moves[i]] == None:
                break

            pop_number = board_stack_list[moves[i]].pop(0)

            if pop_number != 0:

                if result_list == [] or result_list[-1] != pop_number:
                    result_list.append(pop_number)
                    break

                elif result_list[-1] == pop_number:
                    result_list.pop()
                    answer += 1
                    break

    return answer * 2


board = [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 3],
         [0, 2, 5, 0, 1],
         [4, 2, 4, 4, 2],
         [3, 5, 1, 3, 1]]

moves = [1, 5, 3, 5, 1, 2, 1, 4]


print(solution(board=board, moves=moves))
