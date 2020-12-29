# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def solution(s):
    str_len = len(s)
    max_slice = round(str_len / 2)
    final = s

    for length in range(1, max_slice + 1):
        slicing = [s[i:i + length] for i in range(0, len(s), length)]

        cursor = 0
        result = ''
        slicing_len = len(slicing)
        state = 0

        while True:
            if slicing_len - 1 == cursor:

                if state == 0:
                    result = result + slicing[cursor]

                else:
                    state += 1
                    result = result + str(state) + slicing[cursor]

                if len(final) >= len(result):
                    final = result

                break

            else:
                if slicing[cursor] == slicing[cursor + 1]:
                    cursor += 1
                    state += 1

                elif slicing[cursor] != slicing[cursor + 1]:
                    if state == 0:
                        result += slicing[cursor]

                    else:
                        # if length == 1:
                        state += 1
                        result = result + str(state) + slicing[cursor]
                        state = 0

                    cursor += 1

    answer = len(final)
    return answer

#
# def compress(text, tok_len):
#     words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
#     res = []
#     cur_word = words[0]
#     cur_cnt = 1
#     for a, b in zip(words, words[1:] + ['']):
#         if a == b:
#             cur_cnt += 1
#         else:
#             res.append([cur_word, cur_cnt])
#             cur_word = b
#             cur_cnt = 1
#     return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)
#
# def solution(text):
#     return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])
#
